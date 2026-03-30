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
    otim.mostrar_problema()
    return


if __name__ == "__main__":
    logger.info("Inicializando a biblioteca de otimização...")
    main()


# Programa
# otimizacao_emilio = Otimizador()

# otimizacao_emilio.adicionar_funcao_objetivo('max. + 0x_1 +  0x_3 + 0x_2 + 0x_4 + 1x_5')
# otimizacao_emilio.adicionar_restricao('+ 3000x_1  + 30000x_3 + 20000x_2 + 10000x_4 + 37777x_5 <= 137777')
# otimizacao_emilio.adicionar_restricao('+ 1x_1 +  1x_3 + 1x_2 + 1x_4 + 5x_5 == 25')
# otimizacao_emilio.adicionar_restricao('+ 20x_1 +  10x_3 + 5x_2 + 2x_4 + 250x_5 <= 500')
# otimizacao_emilio.adicionar_restricao('+ 10x_1  + 20x_3 + 20x_2 +  15x_4 - 50x_5 >= 50')
# otimizacao_emilio.adicionar_restricao('+ 0x_1  + 0x_3 + 0x_2 + 0x_4 + 1x_5 <= 1')
# otimizacao_emilio.simplex()

# EXEMPLO YOUTUBE
# otimizacao_emilio.adicionar_funcao_objetivo('max. + 6x_1 - 7x_2 - 4x_3')
# otimizacao_emilio.adicionar_restricao('+ 2x_1 + 5x_2 - 1x_3 <= 18')
# otimizacao_emilio.adicionar_restricao('- 1x_1 + 1x_2 + 2x_3 >= 14')
# otimizacao_emilio.adicionar_restricao('+ 3x_1 +  2x_2 + 2x_3 == 26')
# otimizacao_emilio.mostrar_problema()
# otimizacao_emilio.simplex()

# TESTE DO PROBLEMA DO GUT
# otimizacao_emilio.adicionar_funcao_objetivo('max. + 0.062x_1 + 0.074x_2')
# otimizacao_emilio.adicionar_restricao('+ 1x_1 + 1x_2 <= 10')
# otimizacao_emilio.adicionar_restricao('- 1x_1 + 0x_2 <= 0')
# otimizacao_emilio.adicionar_restricao('+ 0x_1 - 1x_2 <= 0')
# otimizacao_emilio.mostrar_problema()
# otimizacao_emilio.simplex() 

# SOLUCIONAR PROBLEMA SIMPLEX COM RESULTADOS LP 
# otimizacao_emilio.adicionar_funcao_objetivo('min. + 3000x_1 + 20000x_2 + 30000x_3 + 10000x_4 ')
# otimizacao_emilio.adicionar_restricao('+ 1x_1 + 1x_2 + 1x_3 + 1x_4  == 20')
# otimizacao_emilio.adicionar_restricao('+ 20x_1 + 5x_2 + 10x_3 + 2x_4 <= 200')
# otimizacao_emilio.adicionar_restricao('+ 10x_1 + 20x_2 + 20x_3 + 15x_4 >= 80')
# otimizacao_emilio.mostrar_problema()
# otimizacao_emilio.simplex()

# SOLUCIONAR PROBLEMA SIMPLEX COM RESULTADOS LP OBTIDOS PARA FASE 2
# otimizacao_emilio.adicionar_funcao_objetivo('min. + 3000x_1 + 20000x_2 + 30000x_3 + 10000x_4 + 0x_5 + 0x_6')
# otimizacao_emilio.adicionar_restricao('+ 10x_1 + 0x_2 + 0x_3 + 5x_4 + 0x_5 + 1x_6 <= 320')
# otimizacao_emilio.adicionar_restricao('+ 10x_1 - 5x_2 + 0x_3 - 8x_4 + 1x_5 + 0x_6 <= 0')
# otimizacao_emilio.adicionar_restricao('+ 1x_1 + 1x_2 + 1x_3 + 1x_4 + 0x_5 + 0x_6 <= 20')
# otimizacao_emilio.mostrar_problema()
# otimizacao_emilio.simplex()

