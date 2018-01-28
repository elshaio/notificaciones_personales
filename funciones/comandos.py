import logging

from funciones import notificaciones, funciones
from funciones.auxiliares import array_join
from sys import exit


def callback(mensaje=None):
    if mensaje is None:
        return
    else:
        notificaciones.mensaje(mensaje)


def comandos(argumentos):
    if len(argumentos) < 1:
        logging.info("No se ha declarado un comando")
        exit(1)

    comando = argumentos[0]
    if comando == 'mensaje':
        mensaje = array_join(" ", argumentos[1:])
        logging.info(mensaje)
        callback(mensaje)
        exit(0)
    elif comando == 'pid':
        funciones.pid(argumentos[1:], callback)
        exit(0)
    elif comando == 'lookapp':
        funciones.lookapp(argumentos[1:], callback)
        exit(0)
