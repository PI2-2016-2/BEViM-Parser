#!/usr/bin/python

import serial
import thread
import sys

class PiSerial:

    def __init__(self):
        self.initialization()

    def initialization(self):
        self.port = '/dev/ttyACM0'
        self.baudrate = 9600
        self.timeout = 1

    def open_serialcom(self):
        self.ser = serial.Serial(self.port,self.baudrate,timeout=self.timeout)
        if self.ser.isOpen():
            print 'Port opened with success!'
        else:
            print 'Error: Couldnt open this port, verify if the same is busy at the moment.'

    def close_serialcom(self):
        self.ser.close()
        if self.ser.isOpen():
            print 'Error in closing the port. Maybe something is stuck?'
        else:
            print 'Port closed with success'

    def data_output(self):
        self.output = self.ser.readline()
        return self.output

    def data_output_list(self):
        self.data_list = []
        self.counter = 0
        while True:
            self.incoming_data  = self.data_output()
            if self.incoming_data == '-1\r\n':
                self.counter += 1
            if self.counter == 2:
                break;
            if  len(self.incoming_data) > 20 and len(self.incoming_data) < 100:
                self.data_list.append(self.incoming_data)
        self.close_serialcom()
        return self.data_list

    #OBS - Funcao nao sera utilizada
    def data_input(self,data):
        self.bytes_writen = self.ser.write(data+'\n')
