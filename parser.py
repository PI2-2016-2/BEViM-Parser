#!/usr/bin/python

import sqlite3
import logging
from piserial import PiSerial as Serial

class ParserData:

    logging.basicConfig(format='%(asctime)s %(message)s', filename='parser.log', level=logging.INFO, datefmt='%d/%m/%Y %I:%M:%S %p')

    def __init__(self, filename):
        self.filename = filename

    def start_routine(self):
        self.connect_DB()
        self.schema()
        #self.defining_sensors()
        self.open_file()
        self.inserting_acceleration()

    #ISSUE -- Conectar com a classe comunicação para receber o total de sensores ativos
    def defining_sensors(self,total):
        self.sensors_list = []
        for x in xrange(1,total):
            self.temp_sensor = (x,'S' + str(x))
            self.sensors_list.append(self.temp_sensor)
        self.sensors = tuple(self.sensors_list)

    def connect_DB(self):
        self.con = sqlite3.connect('sensor_data.db')
        self.cur = self.con.cursor()
        logging.info('Database connected')

    def schema(self):
        logging.info('Verifying schema')
        self.info = self.cur.execute('PRAGMA table_info(Sensor)')
        if len(self.info.fetchall()) == 0:
            self.cur.execute('CREATE TABLE Sensor(sensor_id INTEGER PRIMARY KEY NOT NULL,'
                                                                             'name VARCHAR(3))')
            self.cur.execute('CREATE TABLE Acceleration(sensor_id INTEGER NOT NULL,'
                                                                                     'acceleration_x DECIMAL(2,2),'
                                                                                     'acceleration_y DECIMAL(2,2),'
                                                                                     'acceleration_z DECIMAL(2,2),'
                                                                                     'timestamp INTEGER,'
                                                                                     'FOREIGN KEY(sensor_id) REFERENCES Sensor(sensor_id))')
            self.cur.execute('CREATE TABLE Speed(sensor_id INTEGER NOT NULL,'
                                                                            'speed_x DECIMAL(2,2),'
                                                                            'speed_y DECIMAL(2,2),'
                                                                            'speed_z DECIMAL(2,2),'
                                                                            'timestamp INTEGER,'
                                                                            'FOREIGN KEY(sensor_id) REFERENCES Sensor(sensor_id))')
            self.cur.execute('CREATE TABLE Amplitude(sensor_id INTEGER NOT NULL,'
                                                                                  'amplitude_x DECIMAL(2,2),'
                                                                                  'amplitude_y DECIMAL(2,2),'
                                                                                  'amplitude_z DECIMAL(2,2),'
                                                                                  'timestamp INTEGER,'
                                                                                  'FOREIGN KEY(sensor_id) REFERENCES Sensor(sensor_id))')
            self.cur.execute('CREATE TABLE Frequency(sensor_id INTEGER NOT NULL,'
                                                                                  'frequency_x DECIMAL(2,2),'
                                                                                  'frequency_y DECIMAL(2,2),'
                                                                                  'frequency_z DECIMAL(2,2),'
                                                                                  'timestamp INTEGER,'
                                                                                  'FOREIGN KEY(sensor_id) REFERENCES Sensor(sensor_id))')
            logging.info('Schema created')
        else:
            logging.info('Schema was already created')

    def defining_sensors(self):
        logging.info('Verifying Sensors table info')
        if len(self.cur.execute('SELECT * FROM Sensor').fetchall()) == 0:
            self.cur.executemany("INSERT INTO Sensor VALUES(?, ?);", self.sensors)
            self.con.commit()
            logging.info('Info about sensors inserted')
        else:
            logging.info('Sensors table info already exists')

    def open_file(self):
        self.file = open(self.filename,'r')
        self.lines = self.file.readlines()
        self.creating_list_tuple(self.lines)
        self.file.close()

    def creating_list_tuple(self,lines):
        self.brute_data = []
        for line in lines:
            self.temp = line.split(',')
            self.verification_sensor_number(self.temp[0])
            self.temp[0] = self.v1
            self.temp[1] = int(self.temp[1])
            self.temp.pop()
            self.brute_data.append(tuple(self.temp))
        self.tuple_data = tuple(self.brute_data)

    def inserting_acceleration(self):
        logging.info('Inserting Acceleration Data')
        print self.tuple_data
        self.cur.executemany("INSERT INTO Acceleration VALUES(?, ?, ?);", self.tuple_data)
        self.con.commit()
        logging.info('Acceleration Data loaded to Database')

    #FIXME - Falta testar
    def verification_sensor_number(self,value):
        self.split_temp = value.split('')
        self.v1 = int(self.split_temp[1])

#Teste de funcionalidade da Classe de Parser
#test = ParserData('data')
#test.start_routine()
