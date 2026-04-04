from otimizacao import Otimizador

otimizacao_youtube = Otimizador()
# EXEMPLO YOUTUBE: https://www.youtube.com/watch?v=btjxqq-vMOg&t=300s
otimizacao_youtube.adicionar_funcao_objetivo('max. + 6x_1 - 7x_2 - 4x_3')
otimizacao_youtube.adicionar_restricao('+ 2x_1 + 5x_2 - 1x_3 <= 18')
otimizacao_youtube.adicionar_restricao('- 1x_1 + 1x_2 + 2x_3 >= 14')
otimizacao_youtube.adicionar_restricao('+ 3x_1 +  2x_2 + 2x_3 == 26')
# otimizacao_emilio.mostrar_problema()
teste = otimizacao_youtube.simplex(calculo_visivel=True)
