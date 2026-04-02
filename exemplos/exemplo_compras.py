# from otimizacao import Otimizador
from otimizacao import Otimizador

# SOLUCIONAR PROBLEMA SIMPLEX COM RESULTADOS LP 
# otimizacao_emilio = Otimizador()
# otimizacao_emilio.adicionar_funcao_objetivo('min. + 3000x_1 + 20000x_2 + 30000x_3 + 10000x_4 ')
# otimizacao_emilio.adicionar_restricao('+ 1x_1 + 1x_2 + 1x_3 + 1x_4  == 20')
# otimizacao_emilio.adicionar_restricao('+ 20x_1 + 5x_2 + 10x_3 + 2x_4 <= 200')
# otimizacao_emilio.adicionar_restricao('+ 10x_1 + 20x_2 + 20x_3 + 15x_4 >= 80')
# otimizacao_emilio.simplex(calculo_visivel=False)


# VERSAO FLP
otimizacao_emilio = Otimizador()
otimizacao_emilio.adicionar_funcao_objetivo('max. + 0x_1 +  0x_3 + 0x_2 + 0x_4 + 1x_5')
otimizacao_emilio.adicionar_restricao('+ 3000x_1  + 30000x_3 + 20000x_2 + 10000x_4 + 37777x_5 <= 137777')
otimizacao_emilio.adicionar_restricao('+ 1x_1 +  1x_3 + 1x_2 + 1x_4 + 5x_5 == 25')
otimizacao_emilio.adicionar_restricao('+ 20x_1 +  10x_3 + 5x_2 + 2x_4 + 250x_5 <= 500')
otimizacao_emilio.adicionar_restricao('+ 10x_1  + 20x_3 + 20x_2 +  15x_4 - 50x_5 >= 50')
otimizacao_emilio.adicionar_restricao('+ 0x_1  + 0x_3 + 0x_2 + 0x_4 + 1x_5 <= 1')
otimizacao_emilio.simplex(calculo_visivel=False)