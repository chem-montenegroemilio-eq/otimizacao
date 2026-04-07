# AINDA NAO ESTA PRONTO

# SOLUCIONAR PROBLEMA DO HIMMELBLAU EX. 12.1 Coluna de destilação 
from otimizacao import Otimizador as otm
# Exemplo de otimizacao LP do Himmelblau
fo = ''
restricao1 = ''
restricao2 = ''

teste = otm() 
teste.adicionar_funcao_objetivo(fo)
teste.adicionar_restricao(restricao1)
teste.adicionar_restricao(restricao2)
# teste.mostrar_problema()
teste.mostrar_funcao_objetivo()
# teste.simplex(calculo_visivel=False)
