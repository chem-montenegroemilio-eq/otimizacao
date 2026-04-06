# AINDA NAO ESSTA PRONTO

# SOLUCIONAR PROBLEMA DO HIMMELBLAU 
from otimizacao import Otimizador as otm
# Exemplo de otimizacao LP do Himmelblau
fo = 'min.    x_1 + 6x_2 - 7x_3 + 1x_4 + 5x_5'
restricao1 = '+ 5x_1 - 4x_2 + 13x_3 - 2x_4 + 1x_5 == 20'
restricao2 = '+ 1x_1 - 1x_2 + 5x_3 - 1x_4 + 1x_5 == 8'

teste = otm() 
teste.adicionar_funcao_objetivo(funcao_objetivo= fo)
teste.adicionar_restricao(restricao1)
teste.adicionar_restricao(restricao2)
teste.simplex(calculo_visivel=True)
