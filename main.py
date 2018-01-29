import logging
from Services import logHandler

from funciones.consoleHelp import create_help

logging_format = '[%(asctime)s] %(levelname)s - %(message)s'
logging.basicConfig(format=logging_format, level=logging.INFO)

if __name__ == '__main__':
    args = create_help()
    logHandler.set_loggers()
