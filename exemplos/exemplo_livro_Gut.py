from otimizacao import Otimizador

# TESTE DO PROBLEMA DO GUT
teste_otimizar = Otimizador()
teste_otimizar.adicionar_funcao_objetivo('max. + 0.062x_1 + 0.074x_2')
teste_otimizar.adicionar_restricao('+ 1x_1 + 1x_2 <= 10')
teste_otimizar.adicionar_restricao('- 1x_1 + 0x_2 <= 0')
teste_otimizar.adicionar_restricao('+ 0x_1 - 1x_2 <= 0')
# otimizacao_emilio.mostrar_problema()
teste_otimizar.simplex() 