### Funcao que calcula a razao entre a coluna pivo e o seu correspondente b (vetor_b ou lista_coef_b) sendo b_{i}/A_{i,coluna_pivo} somente para valores>0. Valores<0 sao definidos como '0'.
def calculo_vetor_razao(lista_matriz_A, lista_coef_b, indice_maior_valor_C_j_Z_j, vetor_variaveis_C_B): 
    vetor_razao = []
    for i, dividendo in enumerate(lista_coef_b):
        divisor = lista_matriz_A[i][indice_maior_valor_C_j_Z_j]
        if divisor == 0:
            vetor_razao.append(0)
        else:
            razao = dividendo / divisor
            if razao >= 0:
                vetor_razao.append(razao)
            else:
                vetor_razao.append(0)
    # O minimo valor positivo define qual elemento sai da variaveis base, e qual variavel entra em C_B (fila pivo)
    vetor_razao_sem0 = vetor_razao[:] # cria uma copia da lista_razao_sem0 principal
    fun_valores_diferentes_de_zero = lambda x: x != 0 # considera somente valores diferentes de zero
    vetor_razao_sem0 = list(filter(fun_valores_diferentes_de_zero, vetor_razao))
    menor_valor_razao = min(vetor_razao_sem0)    
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
    return vetor_variaveis_C_B, vetor_coeficientes_C_B


### Funcao valores C_j e vetor C_B
# 1 Define-se os valores de todas as variaveis base do tableau C_j (consideram-se todas as variaveis) 
def funcao_C_j_e_C_B(definir_min_max, lista_todas_variaveis, lista_fo):
    M = 100
    coeficiente_base_tableau_C_j = []
    for i, variavel in enumerate(lista_todas_variaveis):
        if 'x' in variavel:
            coeficiente_base_tableau_C_j.append(lista_fo[i])
        elif 'a' in variavel:
            if 'max' in definir_min_max:
                coeficiente_base_tableau_C_j.append(M)
            else:
                coeficiente_base_tableau_C_j.append(-M)
        else:
            coeficiente_base_tableau_C_j.append(0)
    print('coeficiente_base_tableau_C_j: ', coeficiente_base_tableau_C_j)
# 2. Cria-se vetor C_B que contenha as variaveis s_i, e a_i
    vetor_variaveis_C_B = []  
    for variavel in lista_todas_variaveis:
        if 's' in variavel:
            vetor_variaveis_C_B.append(variavel)
        elif 'a' in variavel:
            vetor_variaveis_C_B.append(variavel)
    print('vetor_variaveis_C_B: ', vetor_variaveis_C_B)
# 3 Define-se o vetor valores C_B baseado nos valores de s_i, e a_i
    vetor_coeficientes_C_B = []
    for i, variavel in enumerate(lista_todas_variaveis):
        if variavel in vetor_variaveis_C_B:
            vetor_coeficientes_C_B.append(-coeficiente_base_tableau_C_j[i])
    print('vetor_coeficientes_C_B: ', vetor_coeficientes_C_B)
    return coeficiente_base_tableau_C_j, vetor_variaveis_C_B, vetor_coeficientes_C_B


### Funcao calculo iteracoes
def funcao_calculo_iteracoes(lista_todas_variaveis, lista_matriz_A, lista_coef_b, vetor_variaveis_C_B, vetor_coeficientes_C_B, coluna_pivo):
# 1 Define fila e coluna pivo, e define o valor pivo (vira divisor)
    indice_coluna_pivo = lista_todas_variaveis.index(coluna_pivo) # lembrando que eh o valor da coluna que substitui o valor da fila
    indice_fila_pivo = vetor_variaveis_C_B.index(coluna_pivo)
    valor_pivo = lista_matriz_A[indice_fila_pivo][indice_coluna_pivo]
    print('valor pivo',valor_pivo)
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
        vetor_C_j_menos_Z_j):
    lista_C_j_Z_j_evitar_infinito = []
    k=0
# 1 Condicional que precisa todos os valores de C_j_menos_Z_j ser <= 0 para parar (otimizacao tipo maximizacao)
    while any(e > 0 for e in vetor_C_j_menos_Z_j):
        print('-------------------------------------------------------------------------------------')
        print(f'# Inicia loop n°{k+1}')
        # PRECISA REDEFINIR (CRIAR FUNCAO?) - Evita loop infinito e outorga maior valor positivo de C_j-Z_j 
        print('vetor C_j_menos_Z_j', vetor_C_j_menos_Z_j)
        lista_C_j_Z_j_evitar_infinito.append(tuple(vetor_C_j_menos_Z_j))
        if len(set(lista_C_j_Z_j_evitar_infinito)) == len(lista_C_j_Z_j_evitar_infinito):
            maior_valor_C_j_Z_j = max(vetor_C_j_menos_Z_j)
        else:
            print('Parece que entramos em loop infinito, vamos corrijir para C_j-Z_j!')
            vetor_C_j_menos_Z_j[vetor_C_j_menos_Z_j.index(max(vetor_C_j_menos_Z_j))] = vetor_C_j_menos_Z_j[vetor_C_j_menos_Z_j.index(max(vetor_C_j_menos_Z_j))] - 1
            maior_valor_C_j_Z_j = max(vetor_C_j_menos_Z_j)
        # Pega indice de maior valor positivo para definir coluna pivo
        indice_maior_valor_C_j_Z_j = vetor_C_j_menos_Z_j.index(maior_valor_C_j_Z_j) 
        coluna_pivo = lista_todas_variaveis[indice_maior_valor_C_j_Z_j]
# 2 Obtencao do vetor razao e consequentemente fila pivo 
        vetor_razao, menor_valor_razao, fila_pivo = calculo_vetor_razao(lista_matriz_A, lista_coef_b, indice_maior_valor_C_j_Z_j, vetor_variaveis_C_B)
        print('vetor_razao', vetor_razao)
        print('menor_valor_razao:', menor_valor_razao)
        print('vetor variaveis C_B:', vetor_variaveis_C_B)
        print('vetor_coeficientes_C_B:', vetor_coeficientes_C_B)    
# 3 Atualizam-se as variaveis e valores do vetor C_B        
        vetor_variaveis_C_B, vetor_coeficientes_C_B = atualizacao_coef_vetor_C_B(lista_todas_variaveis, coeficiente_base_tableau_C_j, vetor_variaveis_C_B, vetor_coeficientes_C_B, fila_pivo, coluna_pivo)
        print('novo vetor variaveis C_B:', vetor_variaveis_C_B)
        print('novo vetor C_B:', vetor_coeficientes_C_B)
        print('matriz_A:\n', '\n'.join( '\t'+str(fila) for fila in lista_matriz_A))
        print('vetor b:\n \t' + ''.join(str(lista_coef_b)))
        print('\n     # Inicia iteracao')
# 3 Atualiza-se a matriz A e vetor b
        lista_matriz_A, lista_coef_b, vetor_coeficientes_C_B = funcao_calculo_iteracoes(
            lista_todas_variaveis, 
            lista_matriz_A, 
            lista_coef_b, 
            vetor_variaveis_C_B, 
            vetor_coeficientes_C_B, 
            coluna_pivo
            # lista_todas_variaveis, 
            # coeficiente_base_tableau_C_j, 
            # lista_matriz_A, 
            # vetor_variaveis_C_B, 
            # vetor_coeficientes_C_B, 
            # lista_coef_b,
            # coluna_pivo
            )
        print('matriz A tratada:\n' + '\n'.join('\t'+str(fila) for fila in lista_matriz_A))
        print('vetor_b tratado:\n \t' + ''.join(str(lista_coef_b)))    
        print('\n     # Inicia calculo Z_j_e_Z_j_menos_C_j')
# 4 Calcula Z_j e C_j-Z_j baseado nas variaveis e coeficientes da f.o. (C_j), na matriz A, e vetor C_B 
        vetor_Z_j, vetor_C_j_menos_Z_j = funcao_calculo_Z_j_e_Z_j_menos_C_j(
            lista_todas_variaveis, 
            lista_matriz_A, 
            coeficiente_base_tableau_C_j, 
            vetor_coeficientes_C_B)
        print('vetor_C_j_menos_Z_j', vetor_C_j_menos_Z_j)
        if k==10: # !!??? nao lembro por que fiz isto
            break
        k+=1
# 5 Calcula otimo da f.o.= c_{j}*x_{j}
    otimo_fo = sum(lista_coef_b[i]*elemento_C_B for i, elemento_C_B in enumerate(vetor_coeficientes_C_B) )
    texto_fim_loop = f'''
    -------------------------------------------------------
    -------------------------------------------------------
    Fim do loop:
    otimo da fo: {-otimo_fo}
    valores f.o. fase1: {coeficiente_base_tableau_C_j}
    matriz_A:\n {'\n'.join( '\t' + str(linha) for linha in lista_matriz_A)}
    vetor_b:\n \t {''.join(str(lista_coef_b))}
    vetor_variaveis_C_B: {''.join(str(vetor_variaveis_C_B))} ## APAGAR?
    vetor_variaveis_C_B: {''.join(str(vetor_coeficientes_C_B))} ## APAGAR? 
    vetor_Z_j: {''.join(str(vetor_Z_j))} ## APAGAR?
    vetor_C_j_menos_Z_j: {''.join(str(vetor_C_j_menos_Z_j))} ## APAGAR? '''
    [print(lista) for lista in lista_C_j_Z_j_evitar_infinito]
    print(texto_fim_loop)
    return lista_matriz_A, lista_coef_b, coeficiente_base_tableau_C_j, vetor_variaveis_C_B, vetor_coeficientes_C_B, vetor_C_j_menos_Z_j 


### Funcao loop minimizar (while) até C_j menos Z_j ser >=0
def funcao_minimizar_loop_C_jmenosZ_j_ate_maior_a_0(
        lista_todas_variaveis,
        coeficiente_base_tableau_C_j,
        lista_matriz_A, 
        lista_coef_b, 
        vetor_variaveis_C_B, 
        vetor_coeficientes_C_B, 
        vetor_C_j_menos_Z_j, 
        ):
    lista_C_j_Z_j_evitar_infinito = []
    k=0
# 1 Condicional que precisa todos os valores de C_j_menos_Z_j ser <= 0 para parar (otimizacao tipo maximizacao)
    while any(e < 0 for e in vetor_C_j_menos_Z_j):
        print('-------------------------------------------------------------------------------------')
        print(f'# Inicia loop n°{k+1}')
        # PRECISA REDEFINIR (CRIAR FUNCAO?) - Evita loop infinito e outorga maior valor negativo de C_j-Z_j 
        print('vetor C_j_menos_Z_j', vetor_C_j_menos_Z_j)
        lista_C_j_Z_j_evitar_infinito.append(tuple(vetor_C_j_menos_Z_j))
        if len(set(lista_C_j_Z_j_evitar_infinito)) == len(lista_C_j_Z_j_evitar_infinito):
            menor_valor_C_j_Z_j = min(vetor_C_j_menos_Z_j)
        else:
            print('Parece que entramos em loop infinito, vamos corrijir para C_j-Z_j!')
            vetor_C_j_menos_Z_j[vetor_C_j_menos_Z_j.index(max(vetor_C_j_menos_Z_j))] = vetor_C_j_menos_Z_j[vetor_C_j_menos_Z_j.index(max(vetor_C_j_menos_Z_j))] - 1
            menor_valor_C_j_Z_j = min(vetor_C_j_menos_Z_j)
        # Pega indice de maior valor positivo para definir coluna pivo
        indice_menor_valor_C_j_Z_j = vetor_C_j_menos_Z_j.index(menor_valor_C_j_Z_j) 
        coluna_pivo = lista_todas_variaveis[indice_menor_valor_C_j_Z_j]
# 2 Obtencao do vetor razao e consequentemente fila pivo 
        print('COLUNA PIVO', coluna_pivo)
        vetor_razao, menor_valor_razao, fila_pivo = calculo_vetor_razao(lista_matriz_A, lista_coef_b, indice_menor_valor_C_j_Z_j, vetor_variaveis_C_B)
        print('vetor_razao', vetor_razao)
        print('menor_valor_razao:', menor_valor_razao)
        print('vetor variaveis C_B:', vetor_variaveis_C_B)
        print('vetor_coeficientes_C_B:', vetor_coeficientes_C_B)    
# 3 Atualizam-se as variaveis e valores do vetor C_B        
        vetor_variaveis_C_B, vetor_coeficientes_C_B = atualizacao_coef_vetor_C_B(lista_todas_variaveis, coeficiente_base_tableau_C_j, vetor_variaveis_C_B, vetor_coeficientes_C_B, fila_pivo, coluna_pivo)
        print('novo vetor variaveis C_B:', vetor_variaveis_C_B)
        print('novo vetor C_B:', vetor_coeficientes_C_B)
        print('matriz_A:\n', '\n'.join( '\t'+str(fila) for fila in lista_matriz_A))
        print('vetor b:\n \t' + ''.join(str(lista_coef_b)))
        print('\n     # Inicia iteracao')
# 3 Atualiza-se a matriz A e vetor b
        lista_matriz_A, lista_coef_b, vetor_coeficientes_C_B = funcao_calculo_iteracoes(
            lista_todas_variaveis, 
            lista_matriz_A, 
            lista_coef_b, 
            vetor_variaveis_C_B, 
            vetor_coeficientes_C_B, 
            coluna_pivo
            # lista_todas_variaveis, 
            # coeficiente_base_tableau_C_j, 
            # lista_matriz_A, 
            # vetor_variaveis_C_B, 
            # vetor_coeficientes_C_B, 
            # lista_coef_b,
            # coluna_pivo
            )
        print('matriz A tratada:\n' + '\n'.join('\t'+str(fila) for fila in lista_matriz_A))
        print('vetor_b tratado:\n \t' + ''.join(str(lista_coef_b)))    
        print('\n     # Inicia calculo Z_j_e_Z_j_menos_C_j')
# 4 Calcula Z_j e C_j-Z_j baseado nas variaveis e coeficientes da f.o. (C_j), na matriz A, e vetor C_B 
        vetor_Z_j, vetor_C_j_menos_Z_j = funcao_calculo_Z_j_e_Z_j_menos_C_j(
            lista_todas_variaveis, 
            lista_matriz_A, 
            coeficiente_base_tableau_C_j, 
            vetor_coeficientes_C_B)
        print('vetor_C_j_menos_Z_j', vetor_C_j_menos_Z_j)
        if k==10: # !!??? nao lembro por que fiz isto
            break
        k+=1
# 5 Calcula otimo da f.o.= c_{j}*x_{j}
    otimo_fo = sum(lista_coef_b[i]*elemento_C_B for i, elemento_C_B in enumerate(vetor_coeficientes_C_B) )
    texto_fim_loop = f'''
    -------------------------------------------------------
    -------------------------------------------------------
    Fim do loop:
    otimo da fo: {-otimo_fo}
    valores f.o. fase1: {coeficiente_base_tableau_C_j}
    matriz_A:\n {'\n'.join( '\t' + str(linha) for linha in lista_matriz_A)}
    vetor_b:\n \t {''.join(str(lista_coef_b))}
    vetor_variaveis_C_B: {''.join(str(vetor_variaveis_C_B))} ## APAGAR?
    vetor_variaveis_C_B: {''.join(str(vetor_coeficientes_C_B))} ## APAGAR? 
    vetor_Z_j: {''.join(str(vetor_Z_j))} ## APAGAR?
    vetor_C_j_menos_Z_j: {''.join(str(vetor_C_j_menos_Z_j))} ## APAGAR? '''
    [print(lista) for lista in lista_C_j_Z_j_evitar_infinito]
    print(texto_fim_loop)
    return lista_matriz_A, lista_coef_b, coeficiente_base_tableau_C_j, vetor_variaveis_C_B, vetor_coeficientes_C_B, vetor_C_j_menos_Z_j 