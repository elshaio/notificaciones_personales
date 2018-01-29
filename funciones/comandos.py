from funciones import notificaciones, funciones
from funciones.auxiliares import array_join
from sys import exit


def callback(text=None):
    if text is None:
        return
    else:
        notificaciones.mensaje(text)


def mensaje(args):
    text = array_join(" ", args.mensaje)
    callback(text)
    exit(0)


def pid(args):
    funciones.pid(args, callback)
    exit(0)


def lookapp(args):
    funciones.lookapp(args, callback)
    exit(0)
