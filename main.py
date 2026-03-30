import logging
import time
import sys
from otimizacao import Otimizador

logging.Formatter.converter = time.gmtime

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger('__name__')

def main():
    otim = Otimizador()
    otim.mostrar_problema()
    return


if __name__ == "__main__":
    logger.info("Inicializando a biblioteca de otimização...")
    main()

