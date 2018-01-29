import logging

from funciones.consoleHelp import create_help

logging_format = '[%(asctime)s] %(levelname)s - %(message)s'
logging.basicConfig(format=logging_format, level=logging.DEBUG)

if __name__ == '__main__':
    args = create_help()
