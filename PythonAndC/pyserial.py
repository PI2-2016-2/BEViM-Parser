import serial
import thread
import sys
 
class PiSerial:
 
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
 
    def open_serialcom(self):
        self.ser = serial.Serial(self.port,self.baudrate,timeout=1)
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
        print 'Arduino: ' + self.output

    def data_monitor(self):
        while True:
            self.data_output()

    def data_raw_input(self):
        while True:
            data = raw_input('Entrada de dados do sistema: ')
            self.data_input(data)

    def data_input(self,data):
        print 'Raspberry PI: ' + data
        self.bytes_writen = self.ser.write(data +'\n')
        print str(self.bytes_writen) + ' bytes were sent!'

def inout_serial(flag):
    if int(flag) == 1:
        piserial = PiSerial('/dev/ttyACM0',9600)
        piserial.open_serialcom()
        thread.start_new_thread(piserial.data_monitor(), ("Thread-Monitor", 2, ))
    else:
        piserial = PiSerial('/dev/ttyACM0',9600)
        piserial.open_serialcom()
        thread.start_new_thread(piserial.data_raw_input(), ("Thread-Input", 2, ))

#Teste do Protocolo de Comunicacao
inout_serial(sys.argv[1]) 
