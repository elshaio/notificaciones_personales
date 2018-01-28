import logging
import auxiliares.pid

from funciones.auxiliares import array_join
from sys import exit


def pid(args, callback=None):
    length = len(args)
    if length == 0:
        logging.error('No se ha establecido un pid a monitorear')
        exit(1)
    elif length == 1:
        auxiliares.pid.monitorear_pid(args[0],
                                      'El proceso con PID:' + args[0] + ' ha terminado.',
                                      callback)
    else:
        auxiliares.pid.monitorear_pid(args[0],
                                      array_join(' ', args[1:]),
                                      callback)


def lookapp(args, callback=None):
    length = len(args)
    if length == 0:
        logging.error('No se ha establecido un nombre a buscar para monitorear')
        exit(1)
    else:
        auxiliares.pid.monitorear_app(args[0], callback)
