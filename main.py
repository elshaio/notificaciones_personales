import logging
import sys
from funciones.comandos import comandos

logging_format = '[%(asctime)s] %(levelname)s - %(message)s'
logging.basicConfig(format=logging_format, level=logging.DEBUG)


def main(argumentos):
    comandos(argumentos)


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
