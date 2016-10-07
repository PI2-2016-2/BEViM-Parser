#!/usr/bin/python

import time
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
        if flag == 1:
            parser_routine(self.name)
        else:
            inserting_command(self.name)

#Rotina responsavel por pegar os sensores ativos - FALTA TESTAR
def get_sensors_routine(threadName,command):

    #Instanciação da porta serial
    piserial = Piserial()
    piserial.open_serialcom()

    #Instanciacao do parser e definicao dos sensores
    parser = Parser()
    parser.inserting_sensors(
        parser.total_sensors(
            parser.creating_data_tuple(0,
                piserial.data_output_list())))

    #Termino da Thread
    threadName.exit()


def parser_routine(threadName):

    piserial = Piserial()
    piserial.open_serialcom()

    parser = Parser()
    parser.inserting_acceleration(
        parser.creating_data_tuple(1,
            piserial.data_output_list()))

    print 'Finishing Parser Routine'
    #Termino da Thread
    threadName.exit()

#Funcao para teste da rotina de Parser
def inserting_command(threadName):

    piserial = Piserial()
    piserial.open_serialcom()
    piserial.data_input('-1')
    piserial.data_input('50')
    time.sleep(5)
    piserial.data_input('-1')
    piserial.close_serialcom()

    print 'Finishing Command Routine'
    threadName.exit()

thread_parser = routine(1,'Thread-Parser-Routine',1)
thread_command = routine(1,'Thread-Command-Routine',0)

thread_command.start()
thread_parser.start()

print 'Exiting Main thread'







