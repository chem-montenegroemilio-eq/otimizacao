import logging
import time
import sys
from src import Otimizador

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
    otim.funcao_objetivo('min. + 3000x_1 + 20000x_2 + 30000x_3 + 10000x_4')
    otim.adicionar_restricao('+ 1x_1 + 1x_2 + 1x_3 + 1x_4 == 20')
    otim.adicionar_restricao('+ 20x_1 + 5x_2 + 10x_3 + 2x_4 <= 200')
    otim.adicionar_restricao('+ 10x_1 + 20x_2 + 20x_3 + 15x_4 >= 80')

    otim.mostrar_funcao_objetivo()
    otim.mostrar_restricoes()
    return


if __name__ == "__main__":
    # logger.info("Inicializando a biblioteca de otimização...")
    main()


Otimizador.funcao_objetivo('min. xxx xxx x x')
Otimizador.adicionar_restricao('Asx xxx xxxx')



