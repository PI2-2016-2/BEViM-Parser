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
        #print 'Arduino: ' + self.output
        return self.output

    def data_output_list(self):
        self.data_list
        while True:
            self.incoming_data  = self.data_output()
            if len(incoming_data) == 0:
                break;
            if len(incoming_data) != 0:
                self.data_list.append(incoming_data)
        self.close_serialcom()
        return self.data_list

    #OBS - Funcao nao sera utilizada
    def data_input(self,data):
        print 'Raspberry PI: ' + data
        self.bytes_writen = self.ser.write(data+'\n')
        print str(self.bytes_writen) + ' bytes were sent!'

#def inout_serial(flag):
#    if int(flag) == 1:
#        piserial = PiSerial('/dev/ttyACM0',9600)
#        piserial.open_serialcom()
#        thread.start_new_thread(piserial.data_monitor(), ("Thread-Monitor", 2, ))
#    else:
#        piserial = PiSerial('/dev/ttyACM0',9600)
#        piserial.open_serialcom()
#        thread.start_new_thread(piserial.data_raw_input(), ("Thread-Input", 2, ))

#Teste do Protocolo de Comunicacao
#intout_serial(sys.argv[0])