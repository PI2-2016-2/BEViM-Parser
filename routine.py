#!/usr/bin/python

import threading
from parser import ParserData as Parser
from piserial import PiSerial as Piserial

class routine(threading.Thread):

    def __init__(self, threadID, name,flag):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print 'Starting ' + self.name + 'at ' + time.ctime()
        if self.flag

#Rotina responsável por pegar os sensores ativos
def get_sensors_routine(threadName,command):

    #Instanciação da porta serial
    piserial = Piserial()
    piserial.open_serialcom()

    #Instanciação do parser e definição dos sensores
    parser = Parser()
    parser.inserting_sensors(
        parser.total_sensors(
            parser.creating_tuple_data(0,
                piserial.data_output_list())))

    #Termino da Thread
    threadName.exit()

def parser_routine(threadName):

    piserial = Piserial()
    piserial.open_serialcom()






