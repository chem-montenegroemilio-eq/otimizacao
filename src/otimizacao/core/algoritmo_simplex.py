import logging
logger = logging.getLogger(__name__)

### Funcao que calcula a razao entre a coluna pivo e o seu correspondente b (vetor_b ou lista_coef_b) sendo b_{i}/A_{i,coluna_pivo} somente para valores>0. Valores<0 sao definidos como '0'.
def calculo_vetor_razao(lista_matriz_A, lista_coef_b, indice_maior_valor_C_j_Z_j, vetor_variaveis_C_B): 
    vetor_razao = []
    for i, dividendo in enumerate(lista_coef_b):
        divisor = lista_matriz_A[i][indice_maior_valor_C_j_Z_j]
        if divisor == 0:
            vetor_razao.append('desconsiderar')
        else:
            razao = dividendo / divisor
            vetor_razao.append(razao)
    # O minimo valor positivo define qual elemento sai da variaveis base, e qual variavel entra em C_B (fila pivo)
    vetor_razao_semnegativo_sem0 = vetor_razao[:] # cria uma copia da lista_razao_sem0 principal
    vetor_razao_semstring = vetor_razao[:]
    fun_valores_maiores_zero_sem_string = lambda x: isinstance(x, (int, float)) and x > 0 # considera valores maiores a 0 e que nao sejam string 
    vetor_razao_semnegativo_sem0 = list(filter(fun_valores_maiores_zero_sem_string, vetor_razao))
    fun_valores_sem_string = lambda x: not isinstance(x,  (str)) 
    vetor_razao_semstring = list(filter(fun_valores_sem_string, vetor_razao))
    if len(vetor_razao_semnegativo_sem0) > 0: 
        menor_valor_razao = min(vetor_razao_semnegativo_sem0)    
        indice_menor_valor_razao = vetor_razao.index(menor_valor_razao)
        fila_pivo =  vetor_variaveis_C_B[indice_menor_valor_razao] 
    # caso de degeneração (vetor com 0's ou valores negativos. Pega o menos negativo)
    # AINDA FALTA ADICIONAR REGRA DE BLAND: https://www.youtube.com/watch?v=tvYNdl9ssCM
    else:
        # AQUI SE PEGA O MENOS NEGATIVO (0 tem preferencia)
        menor_valor_razao = max(vetor_razao_semstring)    
        indice_menor_valor_razao = vetor_razao.index(menor_valor_razao)
        fila_pivo =  vetor_variaveis_C_B[indice_menor_valor_razao]
    return vetor_razao, menor_valor_razao, fila_pivo


### Funcao que atualiza o vetor das variaveis e coeficientes C_B 
def atualizacao_coef_vetor_C_B(lista_todas_variaveis, coeficiente_base_tableau_C_j, vetor_variaveis_C_B, vetor_coeficientes_C_B, fila_pivo, coluna_pivo):
    # Se subtitui a nova variavel da coluna pivo no vetor C_B (atualiza C_B)
    vetor_variaveis_C_B[vetor_variaveis_C_B.index(fila_pivo)] = coluna_pivo
    for i, variavel_C_B in enumerate(vetor_variaveis_C_B):
        indice_a_ser_considerado = lista_todas_variaveis.index(variavel_C_B)
        valor_a_ser_substituido_em_C_B = coeficiente_base_tableau_C_j[indice_a_ser_considerado]       
        vetor_coeficientes_C_B[i] = valor_a_ser_substituido_em_C_B
        # logger.info(f'Variavel {vetor_variaveis_C_B.index(fila_pivo)} eh substituida pela variavel')
    return vetor_variaveis_C_B, vetor_coeficientes_C_B


### Funcao que valida existencia e continuacao da Fase 1
def funcao_valida_cotinuacao_fase1(lista_todas_variaveis, vetor_variaveis_C_B):
    lista_com_artificiais = [artificiais for artificiais in lista_todas_variaveis if 'a' in artificiais]
    if len(lista_com_artificiais) > 0:
        lista_com_artificiais_C_B = [artificiais_CB for artificiais_CB in vetor_variaveis_C_B if 'a' in artificiais_CB]
        if len(lista_com_artificiais_C_B) > 0:
            return True
        else:
            return False
    else:
        return True
    
### Funcao valores C_j e vetor C_B
# 1 Define-se os valores de todas as variaveis base do tableau C_j (consideram-se todas as variaveis) 
def funcao_C_j_e_C_B(definir_min_max, lista_todas_variaveis, lista_fo):
    M = 100000000
    coeficiente_base_tableau_C_j = []
    for i, variavel in enumerate(lista_todas_variaveis):
        if 'x' in variavel:
            if 'max' in definir_min_max:
                coeficiente_base_tableau_C_j.append(lista_fo[i])
            else:
                coeficiente_base_tableau_C_j.append(-lista_fo[i])
        elif 'a' in variavel:
            coeficiente_base_tableau_C_j.append(-M)
        else:
            coeficiente_base_tableau_C_j.append(0)
    if 'min' in definir_min_max:
        logger.info('''\nO algoritmo é de maximizacao. 
Para minimizacao, invertem-se os sinais dos coeficientes das variaves decisao.''')
    logger.info(f'''Lista de todas as variaveis:  
    {'  '.join( f"{round(coeficiente_base_tableau_C_j[i], 2)}{variavel}" if not 'a' in variavel else f'-M{variavel}' for i, variavel in enumerate(lista_todas_variaveis))}''')
# 2. Cria-se vetor C_B que contenha as variaveis s_i, e a_i
    vetor_variaveis_C_B = []  
    for variavel in lista_todas_variaveis:
        if 's' in variavel:
            vetor_variaveis_C_B.append(variavel)
        elif 'a' in variavel:
            vetor_variaveis_C_B.append(variavel)
# 3 Define-se o vetor valores C_B baseado nos valores de s_i, e a_i
    vetor_coeficientes_C_B = []
    for i, variavel in enumerate(lista_todas_variaveis):
        if variavel in vetor_variaveis_C_B:
            vetor_coeficientes_C_B.append(coeficiente_base_tableau_C_j[i])
    logger.info(f'''Vetor C_B:
    {'  '.join(f"{variavel_CB}:{round(vetor_coeficientes_C_B[i],2)}" if not 'a' in variavel_CB else f"{variavel_CB}:-M"for i, variavel_CB in enumerate(vetor_variaveis_C_B))},   em que M é um valor muito grande (escolheu-se 100000000) ''')
    return coeficiente_base_tableau_C_j, vetor_variaveis_C_B, vetor_coeficientes_C_B


### Funcao calculo iteracoes
def funcao_calculo_iteracoes(lista_todas_variaveis, lista_matriz_A, lista_coef_b, vetor_variaveis_C_B, vetor_coeficientes_C_B, coluna_pivo):
# 1 Define fila e coluna pivo, e define o valor pivo (vira divisor)
    indice_coluna_pivo = lista_todas_variaveis.index(coluna_pivo) # lembrando que eh o valor da coluna que substitui o valor da fila
    indice_fila_pivo = vetor_variaveis_C_B.index(coluna_pivo)
    valor_pivo = lista_matriz_A[indice_fila_pivo][indice_coluna_pivo]
    logger.info(f'Valor pivo: {round(valor_pivo,2)} da fila {indice_fila_pivo+1} coluna {indice_coluna_pivo+1}')
# 2 Percorre a fila pivo atualizando-a (o elemento pivo deve virar '1')
    for j, elemento_fila in enumerate(lista_matriz_A[indice_fila_pivo]):
        valor_pivo_substituir = float(elemento_fila / valor_pivo)
        lista_matriz_A[indice_fila_pivo][j] = valor_pivo_substituir
    lista_coef_b[indice_fila_pivo] = lista_coef_b[indice_fila_pivo] / valor_pivo
# 3 Atualizada a matriz A e vetor b mediante os calculos, eliminando os correspondentes da coluna pivo das filas nao-pivo
    for i, fila_matriz in enumerate(lista_matriz_A):        
        # Tratando matriz A: Entra nas filas que nao sao pivo para atualizar os valores eliminando a coluna pivo
        if i != indice_fila_pivo:
            valor_a_eliminar = fila_matriz[indice_coluna_pivo]
            for j, elemento_fila in enumerate(fila_matriz):
                # Calculo de valor a eliminar (para zerar a fila nao-pivo da coluna pivo)
                valor_a_substituir_em_fila = (lista_matriz_A[indice_fila_pivo][j] * (-valor_a_eliminar) ) + lista_matriz_A[i][j]
                lista_matriz_A[i][j] = valor_a_substituir_em_fila
        # Tratando vetor b: Calculo de valor a eliminar (para zerar a fila nao-pivo da coluna vetor b)
            valor_a_substituir_em_vetor_b = lista_coef_b[indice_fila_pivo] * (-valor_a_eliminar) + lista_coef_b[i] 
            lista_coef_b[i] = valor_a_substituir_em_vetor_b
    return lista_matriz_A, lista_coef_b, vetor_coeficientes_C_B

### Funcao para calculo de Z_j e Z_j-C_j
def funcao_calculo_Z_j_e_Z_j_menos_C_j(lista_todas_variaveis, lista_matriz_A, coeficiente_base_tableau_C_j, vetor_coeficientes_C_B):
    vetor_Z_j = []
    vetor_C_j_menos_Z_j = []
# 1 Percorre a matriz A para calcular Z_j que eh produto escalar (e.g., C_B \cdot A_{x_1}) e tbm C_j-Z_j
    for i, coluna in enumerate(lista_todas_variaveis):
        Z = 0
        C_j_menos_Z_j = 0    
        for k, elemento in enumerate(vetor_coeficientes_C_B):
            valor_A_j = lista_matriz_A[k][i] 
            Z += elemento*valor_A_j
        vetor_Z_j.append(Z)
        C_j_menos_Z_j = coeficiente_base_tableau_C_j[i]-vetor_Z_j[i]
        vetor_C_j_menos_Z_j.append(C_j_menos_Z_j)
    return vetor_Z_j, vetor_C_j_menos_Z_j


### Funcao loop maximizar (while) até C_j menos Z_j ser <=0
def funcao_maximizar_loop_C_jmenosZ_j_ate_menor_a_0(
        lista_todas_variaveis, 
        coeficiente_base_tableau_C_j, # coeficientes do vetor c^{T}_{j}
        lista_matriz_A, 
        lista_coef_b,
        vetor_variaveis_C_B, 
        vetor_coeficientes_C_B, 
        vetor_C_j_menos_Z_j,
        min_ou_max=str,
        ):
    lista_C_j_Z_j_evitar_infinito = []
    k=0
    historico_lista_razao = set()
# 1 Condicional que precisa todos os valores de C_j_menos_Z_j ser <= 0 para parar (otimizacao tipo maximizacao)
    while any(e > 0 for e in vetor_C_j_menos_Z_j):
        logger.info(f'''\n---------------------------------------------------------------------------------------------------
\t\t\t\t\tINICIA LOOP n°{k+1}
---------------------------------------------------------------------------------------------------''')
        if k == 0:
            logger.info(f'''Vetor C_j menos Z_j: 
\t{[round(numero,2) for numero in vetor_C_j_menos_Z_j]}''')
        else:
            pass
#   {'  '.join(str(valor) for valor in vetor_C_j_menos_Z_j)}''')
        # PRECISA REDEFINIR (CRIAR FUNCAO?) - Evita loop infinito e outorga maior valor positivo de C_j-Z_j 
        lista_C_j_Z_j_evitar_infinito.append(tuple(vetor_C_j_menos_Z_j))
        maior_valor_C_j_Z_j = max(vetor_C_j_menos_Z_j)
        # Pega indice de maior valor positivo para definir coluna pivo
        indice_maior_valor_C_j_Z_j = vetor_C_j_menos_Z_j.index(maior_valor_C_j_Z_j) 
        coluna_pivo = lista_todas_variaveis[indice_maior_valor_C_j_Z_j]
        logger.info(f'Coluna pivo: {coluna_pivo}')
# 2 Obtencao do vetor razao e consequentemente fila pivo 
        vetor_razao, menor_valor_razao, fila_pivo = calculo_vetor_razao(lista_matriz_A, lista_coef_b, indice_maior_valor_C_j_Z_j, vetor_variaveis_C_B)
        # Evitando infinito
        if k==11:
            break
        
        estado = tuple(vetor_razao)
        if estado in historico_lista_razao:
            logger.info(f'''
                  \tINFINITO DETECTADO!
                  ''')
            break
        historico_lista_razao.add(estado)
        vetor_razao_printar = [round(numero, 2) if not isinstance(numero,str) else 'desconsiderar'for numero in vetor_razao]
        logger.info(f'''Vetor razao: {vetor_razao_printar}, com menor valor razao de {round(menor_valor_razao, 2)}
Das variaveis C_B tem-se {' '.join(f'{variavel}:{vetor_coeficientes_C_B[i]},'if not 'a' in variavel else f'{variavel}:M,' for i, variavel in enumerate(vetor_variaveis_C_B) )}''')    
# 3 Atualizam-se as variaveis e valores do vetor C_B        
        vetor_variaveis_C_B, vetor_coeficientes_C_B = atualizacao_coef_vetor_C_B(lista_todas_variaveis, coeficiente_base_tableau_C_j, vetor_variaveis_C_B, vetor_coeficientes_C_B, fila_pivo, coluna_pivo)
        if fila_pivo == coluna_pivo:
            pass
        else:
            logger.info(f'A variavel {fila_pivo} eh substituida pela variavel {coluna_pivo}')
            logger.info(f'Novo vetor variaveis C_B: \n\t{vetor_variaveis_C_B}')
        # logger.info(f'Novo vetor C_B: {vetor_coeficientes_C_B}')
        if funcao_valida_cotinuacao_fase1(lista_todas_variaveis, vetor_variaveis_C_B) is False:
            logger.info('As variáveis "a" sairam da base C_B. Finaliza a fase 1.')
            break
        matriz_A_formatada = '\n'.join( '\t'+str([round(elemento, 2) for elemento in fila]) for fila in lista_matriz_A)
        logger.info(f'''Matriz A:\n{matriz_A_formatada})
Vetor b:\n \t{[round(coef,2) for coef in lista_coef_b]}
\t\t\t\t\t----------------
\t\t\t\t\tINICIA ITERACAO:
\t\t\t\t\t----------------''')
# 3 Atualiza-se a matriz A e vetor b
        lista_matriz_A, lista_coef_b, vetor_coeficientes_C_B = funcao_calculo_iteracoes(
            lista_todas_variaveis, 
            lista_matriz_A, 
            lista_coef_b, 
            vetor_variaveis_C_B, 
            vetor_coeficientes_C_B, 
            coluna_pivo
            )
        matriz_A_formatada = '\n'.join('\t'+str([round(elemento,2)for elemento in fila]) for fila in lista_matriz_A)
        logger.info(f'''Matriz A tratada:\n{matriz_A_formatada}
Vetor b tratado:\n \t{[round(coef, 2) for coef in lista_coef_b]})
\t\t\t\t----------------------------------
\t\t\t\tINICIA CALCULO Z_j e Z_j menos C_j
\t\t\t\t----------------------------------''')
# 4 Calcula Z_j e C_j-Z_j baseado nas variaveis e coeficientes da f.o. (C_j), na matriz A, e vetor C_B 
        vetor_Z_j, vetor_C_j_menos_Z_j = funcao_calculo_Z_j_e_Z_j_menos_C_j(
            lista_todas_variaveis, 
            lista_matriz_A, 
            coeficiente_base_tableau_C_j, 
            vetor_coeficientes_C_B)
        logger.info(f'Vetor Z_j:\n\t{[round(valor,2) for valor in vetor_Z_j]}')
        logger.info(f'Vetor C_j menos Z_j:\n\t{[round(valor,2) for valor in vetor_C_j_menos_Z_j]}')

        k+=1
# 5 Calcula otimo da f.o.= c_{j}*x_{j}
    otimo_fo = sum(lista_coef_b[i]*elemento_C_B for i, elemento_C_B in enumerate(vetor_coeficientes_C_B) )
    if 'max' in min_ou_max:
        coeficientes_fo = [coeficiente for coeficiente in coeficiente_base_tableau_C_j]
    elif 'min' in min_ou_max:
        otimo_fo = -otimo_fo
        coeficientes_fo = [-coeficiente for coeficiente in coeficiente_base_tableau_C_j]
    # VALIDANDO SE FASE 1 OU 2
    validador = None
    lista_artificiais = [variavel for variavel in lista_todas_variaveis if 'a' in variavel]
    if len(lista_artificiais):
        validador = True
    else: 
        False
    
    dicionario_variaveis_coeficientes_C_B = {}
    for i, variaveis in enumerate(vetor_variaveis_C_B):
        dicionario_variaveis_coeficientes_C_B[variaveis] = lista_coef_b[i]
    matriz_A_formatada = '\n\t\t\t'.join( '  ' + str([round(elemento,2) for elemento in linha]) for linha in lista_matriz_A)
    texto_fim_loop_fase1 = f'''
\t\t\t-------------------------------------------------------
\t\t\t-------------------------------------------------------
\t\t\t\t\tFIM DO LOOP DA FASE 1:
\t\t\t-------------------------------------------------------
\t\t\t-------------------------------------------------------
\t\t\tValores variaveis: \n\t\t\t\t {'  '.join(str(variavel)+':'+str(round(dicionario_variaveis_coeficientes_C_B[variavel],2)) for i, variavel in enumerate(dicionario_variaveis_coeficientes_C_B))}
\t\t\tMatriz A:\n\t\t\t{matriz_A_formatada}
\t\t\tVetor b:\n\t\t\t  {''.join(str([round(coef,3) for coef in lista_coef_b]))}
\t\t\tVariaveis junto com os coeficientes c_j:\n\t\t\t  {''.join(str(lista_todas_variaveis))}
\t\t {''.join(str(coeficiente_base_tableau_C_j))}
* Estao sendo incluidas as colunas das variaveis artificiais. Para Simplex Fase 2 devem ser tiradas.
'''

    texto_fim_loop_fase2 = f'''
\t\t\t-------------------------------------------------------
\t\t\t-------------------------------------------------------
\t\t\t\t\tFIM DO LOOP DA FASE 2:
\t\t\t-------------------------------------------------------
\t\t\t-------------------------------------------------------
\t\t\tOtimo da fo: {round(otimo_fo,2)}
\t\t\tVetor decisao otimo: \n\t\t\t  {' '.join(str(vetor_variaveis_C_B[::-1][i])+'='+str(round(coeficiente,2))+',' for i, coeficiente in enumerate(lista_coef_b[::-1])) }
\t\t\t  {' '.join(str(variavel)+'='+ '0' +',' for variavel in lista_todas_variaveis if variavel not in vetor_variaveis_C_B  ) }
\t\t\tMatriz_A:\n\t\t\t{matriz_A_formatada}
\t\t\tVetor_b:\n\t\t\t  {''.join(str([round(coef,2) for coef in lista_coef_b]))}'''
    if validador == True:
        logger.info(texto_fim_loop_fase1)    
    else: 
        logger.info(texto_fim_loop_fase2)
    return lista_matriz_A, lista_coef_b, coeficiente_base_tableau_C_j, vetor_variaveis_C_B, vetor_coeficientes_C_B, vetor_C_j_menos_Z_j 
