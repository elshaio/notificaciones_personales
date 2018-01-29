import auxiliares.pid

from funciones.auxiliares import array_join


def pid(args, callback=None):
    if args.mensaje:
        auxiliares.pid.monitorear_pid(args.pid,
                                      array_join(' ', args.mensaje),
                                      callback)
    else:
        auxiliares.pid.monitorear_pid(args.pid,
                                      'El proceso con PID: {0!s} ha terminado.'.format(args.pid),
                                      callback)


def lookapp(args, callback=None):
    auxiliares.pid.monitorear_app(array_join(" ", args.app), callback)
