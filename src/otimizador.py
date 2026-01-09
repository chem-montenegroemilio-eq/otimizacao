from typing import List

from core import _parser  
from core import _determinador_fase
from core import _algoritmo_simplex

class Otimizador:

    def __init__(self, funcao_objetivo=None, restricoes=None):
        self.funcao_objetivo = "min. + 3000x_1 + 20000x_2 + 30000x_3 + 10000x_4"
        self.restricoes: List[str] = [
            '+ 1x_1 + 1x_2 + 1x_3 + 1x_4 == 20', 
            '+ 20x_1 + 5x_2 + 10x_3 + 2x_4 <= 200',
            '+ 10x_1 + 20x_2 + 20x_3 + 15x_4 >= 80' ]

    def adicionar_funcao_objetivo(self, funcao_objetivo):
        self.funcao_objetivo = funcao_objetivo

    def adicionar_restricao(self, nova_restricao):
        if self.restricoes[0]=='+ 1x_1 + 1x_2 + 1x_3 + 1x_4 == 20':
            self.restricoes = []
            self.restricoes.append(nova_restricao)
        else:
            self.restricoes.append(nova_restricao)

    # faz o tratamento dos dados brutos e retorna os dados prontos para serem analisados pela fase1
    def _tratamento_dados(self, funcao_objetivo, restricoes):
        # Definir a f.o.: min. ou max. e digite a funcao
        fo_min_max, fo_equacao = funcao_objetivo.split('.')
        fo_equacao.replace(' ', '')
        # Obter variaveis e coeficientes separados numa funcao
        dicionario_fo =  _parser.funcao_coef_variaveis(fo_equacao)
        # Definir as restricoes, tornar os coeficientes a direita positivos
        lista_restricoes = restricoes 
        # Procesamento para obtencao da matriz em forma de tupla(dicionarios)
        tupla_restricoes, tupla_coef_b = _parser.matriz_restricoes(lista_restricoes)
        # Organizando tudo em vetor/Tirar todas as chaves da tupla e organizar em order
        lista_todas_variaveis = []
        for dicionario in tupla_restricoes:
            lista_chaves = list(dicionario.keys())
            for chave in lista_chaves:
                if chave not in lista_todas_variaveis:
                    lista_todas_variaveis.append(chave)
        # Organizar cada restricao em forma de vetor, adicionar os 0s caso nao haja coeficiente
        lista_matriz_A = _parser.funcao_conversao_dicionario_restricao_em_lista_restricao(tupla_restricoes, lista_todas_variaveis)
        # Printar funcao objetivo, restricoes, e vetor b    
        lista_coef_b = list(tupla_coef_b)
        lista_fo = _parser.funcao_conversao_dicionario_funcaoobjetivo_em_lista_funcaoobjetivo(dicionario_fo, lista_todas_variaveis)
        return lista_todas_variaveis, lista_fo, lista_matriz_A, lista_coef_b

    def mostrar_problema(self):
        print('O problema tem a seguinte forma vetorial e matricial.')
        lista_todas_variaveis, lista_fo, lista_matriz_A, lista_coef_b = self._tratamento_dados(self.funcao_objetivo, self.restricoes)
        print(
            'VARIAVEIS:', lista_todas_variaveis,
            '\nVETOR FUNÇÃO OBJETIVO:', lista_fo,
            '\nMATRIZ A:' , [ linha for linha in lista_matriz_A],
            '\nVETOR b:', lista_coef_b
            )
    
    def mostrar_funcao_objetivo(self):
        print('FUNCAO OBJETIVO:\n{}'.format(self.funcao_objetivo))

    def mostrar_restricoes(self):
        print(f"RESTRIÇÕES: ")
        for restricao in self.restricoes:
            print(f"{restricao}")        
    
    def adicionar_1(self):
        self.contador += 1
        print(self.contador)

    def _determinador(self):
        lista_todas_variaveis, lista_fo, lista_matriz_A, lista_coef_b = self._tratamento_dados(self.funcao_objetivo, self.restricoes)
        # Determinando fase 1
        fase1_true_fase2_false = _determinador_fase.funcao_caso_haja_variaveis_artificias(lista_todas_variaveis)
        if fase1_true_fase2_false == True:
            return True
        else:
            return False

    def _calculo_simplex(self):
        lista_todas_variaveis, lista_fo, lista_matriz_A, lista_coef_b = self._tratamento_dados(self.funcao_objetivo, self.restricoes)
        # Metodo Simplex caso fase 1
        coeficiente_base_tableau_C_j, vetor_variaveis_C_B, vetor_coeficientes_C_B = _algoritmo_simplex.funcao_C_j_e_C_B(lista_todas_variaveis, lista_fo)
        ## AQUI DEVE COMECAR A FUNCAO PARA Z_j e C_j-Z_j
        vetor_Z_j, vetor_C_j_menos_Z_j = _algoritmo_simplex.funcao_calculo_Z_j_e_Z_j_menos_C_j(lista_todas_variaveis, lista_matriz_A, coeficiente_base_tableau_C_j, vetor_coeficientes_C_B)
        ## AQUI DEVE COMECAR O LOOP ATE C_j-Z_j <= 0
        _algoritmo_simplex.funcao_loop_C_jmenosZ_j_ate_menor_a_0(lista_matriz_A, lista_todas_variaveis, vetor_variaveis_C_B, vetor_coeficientes_C_B, coeficiente_base_tableau_C_j, vetor_C_j_menos_Z_j, lista_coef_b)


    def simplex(self):
        if not self.funcao_objetivo and not self.restricoes:
            print('Porque o problema possui restricoes de igualdade. \nSera resolvida a Fase 1:')
            self._calculo_simplex()
        else:
            if self._determinador() == True:
                print('Porque o problema possui restricoes de igualdade. \nSera resolvida a Fase 1:')
                self._calculo_simplex()


# Programa
otimizacao_emilio = Otimizador()
otimizacao_emilio.mostrar_funcao_objetivo()
otimizacao_emilio.mostrar_restricoes()
otimizacao_emilio.simplex()

otimizacao_emilio.adicionar_funcao_objetivo('max. + 0x_1 +  0x_3 + 0x_2 + 0x_4 + 1x_5')
otimizacao_emilio.adicionar_restricao('+ 3000x_1  + 30000x_3 + 20000x_2 + 10000x_4 + 37777x_5 <= 137777')
otimizacao_emilio.adicionar_restricao('+ 1x_1 +  1x_3 + 1x_2 + 1x_4 + 5x_5 == 25')
otimizacao_emilio.adicionar_restricao('+ 20x_1 +  10x_3 + 5x_2 + 2x_4 + 250x_5 <= 500')
otimizacao_emilio.adicionar_restricao('+ 10x_1  + 20x_3 + 20x_2 +  15x_4 - 50x_5 >= 50')
otimizacao_emilio.adicionar_restricao('+ 0x_1  + 0x_3 + 0x_2 + 0x_4 + 1x_5 <= 1')
# otimizacao_emilio.adicionar_restricao('+ 0x_1  + 0x_3  + 0x_2 + 0x_4 + 1x_5 >= 0')

# otimizacao_emilio.mostrar_funcao_objetivo()
# otimizacao_emilio.mostrar_restricoes()

# otimizacao_emilio.simplex()

