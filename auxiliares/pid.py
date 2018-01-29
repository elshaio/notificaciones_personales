import psutil
import logging
import shlex
import subprocess

from funciones.auxiliares import array_join


class PsAux():
    def __init__(self, arrInfo):
        self.usuario = arrInfo[0]
        self.pid = int(arrInfo[1])
        self.perc_cpu = float(arrInfo[2])
        self.perc_mem = float(arrInfo[3])
        self.vsz = int(arrInfo[4])
        self.rss = int(arrInfo[5])
        self.tty = arrInfo[6]
        self.stat = arrInfo[7]
        self.start = arrInfo[8]
        self.time = arrInfo[9]
        self.command = array_join(" ", arrInfo[10:])


def monitorear_pid(pid, mensage, callback=None):
    pid = int(pid)
    p = psutil.Process(pid)
    logging.info('Iniciando monitoreo del pid %s', str(pid))
    while p.is_running():
        continue
    callback(mensage)


def monitorear_app(app, callback=None):
    comando = 'ps aux --columns 1000 | grep -i {0!s} | grep -v grep'
    comando = str.format(comando, app)

    procesos = execute_command(comando)

    length = len(procesos)

    if length == 0:
        logging.error('No se ha encontrado una aplicación con ese nombre')
        exit(1)

    for proceso, index in zip(procesos, range(length)):
        proceso = shlex.split(proceso)
        proceso = PsAux(proceso)
        logging.info('%s - PID: %s, COMMAND: %s',
                     str(index + 1),
                     proceso.pid,
                     proceso.command)

    while True:
        try:
            logging.info('Opción a monitorear?[1-%s]:', str(length))
            opcion = input()
            opcion = int(opcion)
            if opcion > length:
                raise ValueError
            break
        except ValueError:
            logging.error("Opción inválida")
            continue
        except KeyboardInterrupt:
            exit(1)

    proceso = PsAux(shlex.split(procesos[opcion - 1]))

    logging.info('Mensaje a enviar[opcional]:')
    mensaje = input() or 'El proceso con PID: {0!s} ha terminado'.format(proceso.pid)

    monitorear_pid(proceso.pid, mensaje, callback)


def execute_command(command=''):
    if command == '':
        return ''

    commands = command.split("|")
    stdout = execute_command_on_pipe(commands)

    response = []

    for line in stdout:
        cleanline = str(line).replace("b'", "").replace("\\n'", "")
        response.append(cleanline)

    return response


def execute_command_on_pipe(commands_to_execute, stdin=None):
    if len(commands_to_execute) == 0:
        return ''

    args = shlex.split(commands_to_execute[0])
    p = subprocess.Popen(args, stdin=stdin, stdout=subprocess.PIPE)

    if len(commands_to_execute) > 1:
        return execute_command_on_pipe(commands_to_execute[1:], p.stdout)
    else:
        return p.stdout
