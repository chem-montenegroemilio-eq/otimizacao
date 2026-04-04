from typing import List
import logging
from .core import parser  
from .core import determinador_fase
from .core import algoritmo_simplex
from .exemplo_Simplex import executar

def configuracao_logging(calculo_visivel: bool):
    level = logging.INFO if calculo_visivel else logging.WARNING
    logging.basicConfig(
        level = level,
        format="%(message)s"
    )
logger = logging.getLogger(__name__)

class Otimizador:
    """
    Classe principal que chama os metodos para tratar problemas de otimizacao.
    """
    def __init__(self, 
                funcao_objetivo=None,
                restricoes=None,
                fo_min_max = None,
                ):
        """
        Args:
            funcao_objetivo (str): funcao objetivo a minimizar ou maximizar.
            restricoes (str): restricoes do problema a otimizar.
            """
        self.funcao_objetivo = None
        self.restricoes: List[str] = []
        self.fo_min_max = None

    def adicionar_funcao_objetivo(self, 
                                  funcao_objetivo:str):
        """Coloca a funcao objetivo no sistema."""
        self.funcao_objetivo = funcao_objetivo


    def adicionar_restricao(self, 
                            nova_restricao: str):
        """Adiciona a restricao para uma lista que sera tratada no sistema."""
        self.restricoes.append(nova_restricao)


    def _tratamento_dados(self, 
                          funcao_objetivo: str,
                          restricoes: str):
        """Faz tratamento dos strings e converte-os em vetores e matrices para resolver o problema de otimizacao"""
        # Define-se a f.o.: min. ou max. e separa do string da equacao
        logger.info(f'''Funcao objetivo:
        {funcao_objetivo}''')
        substituir_ponto = funcao_objetivo.find('.')
        funcao_objetivo = funcao_objetivo[:substituir_ponto] + '|' + funcao_objetivo[substituir_ponto+1:]
        self.fo_min_max, fo_equacao = funcao_objetivo.split('|')
        fo_equacao = fo_equacao.replace(' ', '')
        # Obtem-se variaveis e coeficientes separados numa funcao
        dicionario_fo =  parser.funcao_coef_variaveis(fo_equacao)
        # Define-se as restricoes, tornando os coeficientes à direita positivos
        lista_restricoes = restricoes 
        # Procesamento para obtencao da matriz em forma de tupla(dicionarios)
        tupla_restricoes, tupla_coef_b = parser.matriz_restricoes(lista_restricoes)
        # Organizando tudo em vetor/Tirar todas as chaves da tupla e organizar em ordem
        lista_todas_variaveis = []
        for dicionario in tupla_restricoes:
            lista_chaves = list(dicionario.keys())
            for chave in lista_chaves:
                if chave not in lista_todas_variaveis:
                    lista_todas_variaveis.append(chave)
        self.lista_todas_variaveis = lista_todas_variaveis[:]
        # Organizar cada restricao em forma de vetor, adicionando os zeros (0s) caso nao haja coeficiente
        lista_matriz_A = parser.funcao_conversao_dicionario_restricao_em_lista_restricao(tupla_restricoes, self.lista_todas_variaveis)
        # Printar funcao objetivo, restricoes, e vetor b    
        lista_coef_b = list(tupla_coef_b)
        self.lista_fo = parser.funcao_conversao_dicionario_funcaoobjetivo_em_lista_funcaoobjetivo(dicionario_fo, self.lista_todas_variaveis)
        return lista_matriz_A, lista_coef_b


    def mostrar_problema(self):
        """Apresenta o problema em listas, na sua forma vetorial e matricial"""
        print('O problema tem a seguinte forma vetorial e matricial.')
        lista_matriz_A, lista_coef_b = self._tratamento_dados(self.funcao_objetivo, self.restricoes)
        matriz_A_formatada = '\n'.join( '\t'+str(linha) for linha in lista_matriz_A)
        print(
            f'''VARIAVEIS:, {self.lista_todas_variaveis},
            \nVETOR FUNÇÃO OBJETIVO:, {self.lista_fo},
            \nMATRIZ A:{matriz_A_formatada},
            \nVETOR b:{''.join(str(lista_coef_b))}'''
            )
    

    def mostrar_funcao_objetivo(self):
        """Apresenta somente a funcao objetivo."""
        print('FUNCAO OBJETIVO:\n{}'.format(self.funcao_objetivo))


    def mostrar_restricoes(self):
        """Apresenta somente as restricoes"""
        print(f"RESTRIÇÕES: ")
        for restricao in self.restricoes:
            print(f"{restricao}")        


    def _determinador(self):
        """Baseado nas variaveis artificiais, determina se precisa passar pela fase 1 (True) ou nao (False)."""
        fase1_true_fase2_false = determinador_fase.funcao_caso_haja_variaveis_artificias(self.lista_todas_variaveis)
        if fase1_true_fase2_false != False:
            logger.info(f'\nExistem {len(fase1_true_fase2_false)} variaveis artificiais: {' '.join(f"{variavel_artificial}," if len(fase1_true_fase2_false) != (fase1_true_fase2_false.index(variavel_artificial)+1) else f"{variavel_artificial}." for i, variavel_artificial in enumerate(fase1_true_fase2_false) )}') 
            return True
        else:
            return False


    def _calculo_simplex_fase1(self):
        """Utilizando as listas dos vetores/matrices resolve o problema simplex de vertice otimo."""
        logger.info('''
\t\t\t\t   -------------------------
\t\t\t\t   -------------------------
\t\t\t\t       INICIALIZA FASE 1
\t\t\t\t   -------------------------
\t\t\t\t   -------------------------
                                  ''')
        # Trata os dados para converter string em vetores e matrices
        lista_matriz_A, lista_coef_b = self._tratamento_dados(self.funcao_objetivo, self.restricoes)
        # Define os coeficientes e valores C_j e C_B
        coeficiente_base_tableau_C_j, vetor_variaveis_C_B, vetor_coeficientes_C_B = algoritmo_simplex.funcao_C_j_e_C_B(self.fo_min_max, self.lista_todas_variaveis, self.lista_fo)
        # Comeca a funcao para Z_j e C_j-Z_j
        vetor_Z_j, vetor_C_j_menos_Z_j = algoritmo_simplex.funcao_calculo_Z_j_e_Z_j_menos_C_j(self.lista_todas_variaveis, lista_matriz_A, coeficiente_base_tableau_C_j, vetor_coeficientes_C_B)
        # Comeca o loop ate C_j-Z_j. <= 0 caso max. >=0 caso min.
        if 'max' in self.fo_min_max:
            lista_nova_A, lista_novo_b, lista_fo, vetor_variaveis_C_B, vetor_coeficientes_C_B, vetor_C_j_menos_Z_j = algoritmo_simplex.funcao_maximizar_loop_C_jmenosZ_j_ate_menor_a_0(
                self.lista_todas_variaveis, 
                coeficiente_base_tableau_C_j, # coeficientes do vetor c^{T}_{j}
                lista_matriz_A, 
                lista_coef_b,
                vetor_variaveis_C_B, 
                vetor_coeficientes_C_B, 
                vetor_C_j_menos_Z_j,
                self.fo_min_max, 
                )
        else:
            lista_nova_A, lista_novo_b, lista_fo, vetor_variaveis_C_B, vetor_coeficientes_C_B, vetor_C_j_menos_Z_j = algoritmo_simplex.funcao_maximizar_loop_C_jmenosZ_j_ate_menor_a_0(
                self.lista_todas_variaveis, 
                coeficiente_base_tableau_C_j, # coeficientes do vetor c^{T}_{j}
                lista_matriz_A, 
                lista_coef_b,
                vetor_variaveis_C_B, 
                vetor_coeficientes_C_B, 
                vetor_C_j_menos_Z_j,
                self.fo_min_max, 
                )
        return lista_nova_A, lista_novo_b, lista_fo, vetor_variaveis_C_B, vetor_coeficientes_C_B, vetor_C_j_menos_Z_j
    

    def _calculo_simplex_fase2(
        self, 
        lista_nova_A, 
        lista_novo_b, 
        lista_nova_fo, # -> coeficiente_base_tableau_C_j
        vetor_variaveis_C_B, 
        vetor_coeficientes_C_B, 
        vetor_C_j_menos_Z_j,
        ):
        logger.info('''
\t\t\t\t   -------------------------
\t\t\t\t   -------------------------
\t\t\t\t       INICIALIZA FASE 2
\t\t\t\t   -------------------------
\t\t\t\t   -------------------------
              ''') 
        # Encontra indices de 'a' que precisam ser elimados nas colunas das lista (tanto em vetores quanto em matrices)
        lista_indices_a = []
        if any('a' in item for item in self.lista_todas_variaveis):
            for i, item in enumerate(self.lista_todas_variaveis):
                if 'a' in item:
                    lista_indices_a.append(i)
            # Elimina indices de 'a' das filas 
            for indices_eliminar in sorted(lista_indices_a, reverse=True):
                self.lista_todas_variaveis.pop(indices_eliminar)
                lista_nova_fo.pop(indices_eliminar)
                vetor_C_j_menos_Z_j.pop(indices_eliminar)
                for i, fila in enumerate(lista_nova_A):
                    fila.pop(indices_eliminar)
                    lista_nova_A[i] = fila
            if 'min' in self.fo_min_max:
                # lista_nova_fo = [-coeficiente for coeficiente in lista_nova_fo]
                mat_A, vet_b, coef_fo, var_CB, coef_CB, Cj_menos_Zj = algoritmo_simplex.funcao_maximizar_loop_C_jmenosZ_j_ate_menor_a_0(
                    self.lista_todas_variaveis,
                    lista_nova_fo, #-> coeficiente_base_tableau_C_j
                    lista_nova_A, 
                    lista_novo_b, 
                    vetor_variaveis_C_B, 
                    vetor_coeficientes_C_B, 
                    vetor_C_j_menos_Z_j,
                    self.fo_min_max,  
                    )
            else:
                mat_A, vet_b, coef_fo, var_CB, coef_CB, Cj_menos_Zj = algoritmo_simplex.funcao_maximizar_loop_C_jmenosZ_j_ate_menor_a_0(
                    self.lista_todas_variaveis,
                    lista_nova_fo, #-> coeficiente_base_tableau_C_j
                    lista_nova_A, 
                    lista_novo_b, 
                    vetor_variaveis_C_B, 
                    vetor_coeficientes_C_B, 
                    vetor_C_j_menos_Z_j,
                    self.fo_min_max,  
                    )
        # Resolve para o caso que somente haja variaveis tipo 's'
        else:
            if 'min' in self.fo_min_max:
                mat_A, vet_b, coef_fo, var_CB, coef_CB, Cj_menos_Zj = algoritmo_simplex.funcao_maximizar_loop_C_jmenosZ_j_ate_menor_a_0(
                    self.lista_todas_variaveis,
                    lista_nova_fo, #-> coeficiente_base_tableau_C_j
                    lista_nova_A, 
                    lista_novo_b, 
                    vetor_variaveis_C_B, 
                    vetor_coeficientes_C_B, 
                    vetor_C_j_menos_Z_j,
                    self.fo_min_max, 
                    )
            else:
                mat_A, vet_b, coef_fo, var_CB, coef_CB, Cj_menos_Zj = algoritmo_simplex.funcao_maximizar_loop_C_jmenosZ_j_ate_menor_a_0(
                    self.lista_todas_variaveis,
                    lista_nova_fo, #-> coeficiente_base_tableau_C_j
                    lista_nova_A, 
                    lista_novo_b, 
                    vetor_variaveis_C_B, 
                    vetor_coeficientes_C_B, 
                    vetor_C_j_menos_Z_j, 
                    self.fo_min_max, 
                    ) 
        otimo_fo = sum(vet_b[i]*elemento_C_B for i, elemento_C_B in enumerate(coef_CB) )
        dicionario_variaveis_coeficientes_C_B = {}
        for i, variaveis in enumerate(var_CB):
            dicionario_variaveis_coeficientes_C_B[variaveis] = coef_CB[i]
        valores_variaveis =  [str(variavel)+':'+str(dicionario_variaveis_coeficientes_C_B[variavel]) for i, variavel in enumerate(dicionario_variaveis_coeficientes_C_B)]
        dicionario_resultados_otimos = {'otimo f.o.=':otimo_fo, 'vetor decisao=': valores_variaveis, 'matriz A=': mat_A, 'vetor b=':vet_b, 'vetor c=':coef_fo}
        return dicionario_resultados_otimos


    def simplex(self, calculo_visivel=True):
        if self.funcao_objetivo is None and self.restricoes == []:
            self.funcao_objetivo, self.restricoes = executar()
        elif self.funcao_objetivo is not None and self.restricoes == []:
            raise ValueError('Faltou adicionar função objetivo.')
        elif self.funcao_objetivo is None and self.restricoes != []:
            raise ValueError('Faltou adicionar restricoes.')
        """Determina a fase e retorna os valores resolvidos pelo metodo simplex."""
        self._tratamento_dados(self.funcao_objetivo, self.restricoes)
        # Para exibir os calculos
        configuracao_logging(calculo_visivel)
        ## Caso possua variaveis artificias (tipo == e/ou >=)
        if self._determinador() == True:    
            mensagem_sobre_artificiais = '''
Porque o problema possui restricoes "=" ou ">=", então será resolvida a Fase 1, com variaveis artificiais "a".
Depois pela Fase 2.'''  
            logger.info(mensagem_sobre_artificiais)
            # Resolve o Simplex e obtem os valores atualizados para posterior calculo da fase 2  
            lista_nova_A, lista_novo_b, lista_nova_fo, vetor_variaveis_C_B, vetor_coeficientes_C_B, vetor_C_j_menos_Z_j = self._calculo_simplex_fase1()
            # Pedido de continuação
            pedido_continuacao = input('Finalizo a Fase 1. Deseja continuar para Fase2?(S/N)')
            if pedido_continuacao.lower()  == 's':
                pass
            else:
                exit()
            # Calculo da fase 2
            dicionario_resultados = self._calculo_simplex_fase2(
                lista_nova_A, 
                lista_novo_b, 
                lista_nova_fo, # -> coeficiente_base_tableau_C_j
                vetor_variaveis_C_B, 
                vetor_coeficientes_C_B, 
                vetor_C_j_menos_Z_j,
                )
        ## Caso possua somente variaveis de folga (tipo <=)
        else:     
            logger.info('''\t\t-------------------------------------------------------------------
\t\t|\t\t     Restricoes do tipo '<='.                     |
\t\t|\tO problema precisa ser resolvido apenas pela Fase 2.      |
\t\t-------------------------------------------------------------------''')    
            # print(self.__dict__)
            lista_matriz_A, lista_coef_b = self._tratamento_dados(self.funcao_objetivo, self.restricoes)
            coeficientes_fo, vetor_variaveis_C_B, vetor_coeficientes_C_B = algoritmo_simplex.funcao_C_j_e_C_B(self.fo_min_max, self.lista_todas_variaveis, self.lista_fo)
            vetor_Z_j, vetor_C_j_menos_Z_j = algoritmo_simplex.funcao_calculo_Z_j_e_Z_j_menos_C_j(self.lista_todas_variaveis, lista_matriz_A, coeficientes_fo, vetor_coeficientes_C_B)
            dicionario_resultados = self._calculo_simplex_fase2(
                lista_matriz_A, 
                lista_coef_b, 
                coeficientes_fo, # -> coeficiente_base_tableau_C_j
                vetor_variaveis_C_B, 
                vetor_coeficientes_C_B, 
                vetor_C_j_menos_Z_j,
                )
        return dicionario_resultados
