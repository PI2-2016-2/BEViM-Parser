#!/usr/bin/python

import sqlite3
import logging

class ParserData:

    logging.basicConfig(format='%(asctime)s %(message)s', filename='parser.log', level=logging.INFO, datefmt='%d/%m/%Y %I:%M:%S %p')

    def __init__(self, filename):
        self.filename = filename
        self.sensors = (
            (1,'S1'),
            (2,'S2'),
            (3,'S3'),
            (4,'S4'),
            (5,'S5'),
            (6,'S6'),
        )

    def start_routine(self):
        self.connect_DB()
        self.schema()
        self.defining_sensors()
        self.open_file()
        self.inserting_acceleration()

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
                                                                                     'acceleration INTEGER,'
                                                                                     'timestamp TEXT,'
                                                                                     'FOREIGN KEY(sensor_id) REFERENCES Sensor(sensor_id))')
            self.cur.execute('CREATE TABLE Speed(sensor_id INTEGER NOT NULL,'
                                                                            'speed INTEGER,'
                                                                            'timestamp TEXT,'
                                                                            'FOREIGN KEY(sensor_id) REFERENCES Sensor(sensor_id))')
            self.cur.execute('CREATE TABLE Amplitude(sensor_id INTEGER NOT NULL,'
                                                                                  'amplitude INTEGER,'
                                                                                  'timestamp TEXT,'
                                                                                  'FOREIGN KEY(sensor_id) REFERENCES Sensor(sensor_id))')
            self.cur.execute('CREATE TABLE Frequency(sensor_id INTEGER NOT NULL,'
                                                                                  'frequency INTEGER,'
                                                                                  'timestamp TEXT,'
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

    def verification_sensor_number(self,value):
        if value == 's1':
            self.v1 = 1
        if value == 's2':
            self.v1 = 2
        if value == 's3':
            self.v1 = 3
        if value == 's4':
            self.v1 = 4
        if value == 's5':
            self.v1 = 5
        if value == 's6':
            self.v1 = 6

#Teste de funcionalidade da Classe de Parser
#test = ParserData('data')
#test.start_routine()
