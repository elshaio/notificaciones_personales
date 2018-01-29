import argparse
from funciones import comandos


def create_help():
    parser = argparse.ArgumentParser(description='Conjunto de herramientas de mi interés para usar en el sistema')

    sp = parser.add_subparsers()

    sp_mensaje = sp.add_parser('mensaje', help='Envía un mensaje al Telegram establecido en la configuración')
    sp_mensaje.add_argument('mensaje', help='Mensaje a ser enviado', type=str, nargs='+')
    sp_mensaje.set_defaults(func=comandos.mensaje)

    sp_pid = sp.add_parser('pid', help='Notifica cuando un pid haya terminado su trabajo')
    sp_pid.add_argument('pid', help='pid a esperar', type=int)
    sp_pid.add_argument('mensaje', help='Mensaje a enviar al terminar el proceso', type=str, nargs='*')
    sp_pid.set_defaults(func=comandos.pid)

    sp_lookapp = sp.add_parser('lookapp', help='Inicia un asistente para buscar una aplicación y avisar cuando ésta '
                                               'haya terminado')
    sp_lookapp.add_argument('app', help='Nombre de la aplicación a buscar', type=str, nargs='+')
    sp_lookapp.set_defaults(func=comandos.lookapp)

    args = parser.parse_args()

    try:
        args.func(args)
    except AttributeError:
        parser.print_help()

