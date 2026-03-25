### Funcao valores C_j e vetor C_B
        # 1 Define-se os valores de todas as variaveis base do tableau C_j (consideram-se todas as variaveis) 
def funcao_C_j_e_C_B(lista_todas_variaveis, lista_fo):
    M = 10 
    coeficiente_base_tableau_C_j = []
    for i, variavel in enumerate(lista_todas_variaveis):
        if 'x' in variavel:
            coeficiente_base_tableau_C_j.append(lista_fo[i])
        elif 'a' in variavel:
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
            vetor_coeficientes_C_B.append(coeficiente_base_tableau_C_j[i])
    print('vetor_coeficientes_C_B: ', vetor_coeficientes_C_B)
    return coeficiente_base_tableau_C_j, vetor_variaveis_C_B, vetor_coeficientes_C_B

### Funcao calculo iteracoes
def funcao_calculo_iteracoes(lista_todas_variaveis, coeficiente_base_tableau_C_j, lista_matriz_A, vetor_variaveis_C_B, vetor_coeficientes_C_B, lista_coef_b, coluna_pivo):
    indice_coluna_pivo = lista_todas_variaveis.index(coluna_pivo) # lembrando que eh o valor da coluna que substitui o valor da fila
    indice_fila_pivo = vetor_variaveis_C_B.index(coluna_pivo)
    valor_pivo = lista_matriz_A[indice_fila_pivo][indice_coluna_pivo]
    print('valor pivo',valor_pivo)
    for j, elemento_fila in enumerate(lista_matriz_A[indice_fila_pivo]):
        valor_pivo_substituir = float(elemento_fila / valor_pivo)
        lista_matriz_A[indice_fila_pivo][j] = valor_pivo_substituir
    lista_coef_b[indice_fila_pivo] = lista_coef_b[indice_fila_pivo] / valor_pivo
    for i, fila_matriz in enumerate(lista_matriz_A):        
        # Tratando matriz A
        if i != indice_fila_pivo:
            # print('fila matriz',fila_matriz)
            valor_a_eliminar = fila_matriz[indice_coluna_pivo]
            for j, elemento_fila in enumerate(fila_matriz):
                valor_a_substituir_em_fila = (lista_matriz_A[indice_fila_pivo][j] * (-valor_a_eliminar) ) + lista_matriz_A[i][j]
                lista_matriz_A[i][j] = valor_a_substituir_em_fila
        # Tratando vetor b
            valor_a_substituir_em_vetor_b = lista_coef_b[indice_fila_pivo] * (-valor_a_eliminar) + lista_coef_b[i] 
            lista_coef_b[i] = valor_a_substituir_em_vetor_b
    return lista_matriz_A, lista_coef_b, vetor_coeficientes_C_B

### Funcao para calculo de Z_j e Z_j-C_j
def funcao_calculo_Z_j_e_Z_j_menos_C_j(lista_todas_variaveis, lista_matriz_A, coeficiente_base_tableau_C_j, vetor_coeficientes_C_B):
    vetor_Z_j = []
    vetor_C_j_menos_Z_j = []
    for i, variavel in enumerate(lista_todas_variaveis):
        Z = 0
        for k, elemento in enumerate(vetor_coeficientes_C_B):
            valor_A_j = lista_matriz_A[k][i] 
            Z += elemento*valor_A_j
        vetor_Z_j.append(Z)
        C_j_menos_Z_j = 0    
        C_j_menos_Z_j = coeficiente_base_tableau_C_j[i]-vetor_Z_j[i]
        vetor_C_j_menos_Z_j.append(C_j_menos_Z_j)
    return vetor_Z_j, vetor_C_j_menos_Z_j

### Funcao loop (while) até C_j menos Z_j ser <=0
def funcao_loop_C_jmenosZ_j_ate_menor_a_0(lista_matriz_A, lista_todas_variaveis, vetor_variaveis_C_B, vetor_coeficientes_C_B, coeficiente_base_tableau_C_j, vetor_C_j_menos_Z_j, lista_coef_b):
    lista_C_j_Z_j_evitar_infinito = []
    k=0
    while any(e > 0 for e in vetor_C_j_menos_Z_j):
        print('-------------------------------------------------------------------------------------')
        print(f'# Inicia loop n°{k+1}')
        # Caso se calcula a base que entra-sai, entao comeca-se por definir o maior valor de C_j-Z_j, e define-se a coluna a utilizar (.index()) e a variavel
        # ALTERACAO PARA EVITAR LOOP INFINITO - TESTE
        print('vetor C_j_menos_Z_j', vetor_C_j_menos_Z_j)
        lista_C_j_Z_j_evitar_infinito.append(tuple(vetor_C_j_menos_Z_j))
        if len(set(lista_C_j_Z_j_evitar_infinito)) == len(lista_C_j_Z_j_evitar_infinito):
            maior_valor_C_j_Z_j = max(vetor_C_j_menos_Z_j)
        else:
            print('Parece que entramos em loop infinito, vamos corrijir para C_j-Z_j!')
            vetor_C_j_menos_Z_j[vetor_C_j_menos_Z_j.index(max(vetor_C_j_menos_Z_j))] = vetor_C_j_menos_Z_j[vetor_C_j_menos_Z_j.index(max(vetor_C_j_menos_Z_j))] - 1
            maior_valor_C_j_Z_j = max(vetor_C_j_menos_Z_j)
        
        indice_maior_valor_C_j_Z_j = vetor_C_j_menos_Z_j.index(maior_valor_C_j_Z_j) # INDICE COLUNA PIVO
        # print('indice_maior_valor_C_j_Z_j', indice_maior_valor_C_j_Z_j)
        coluna_pivo = lista_todas_variaveis[indice_maior_valor_C_j_Z_j]

        # Depois, se calcula a razao entre a coluna pivo e o seu correspondente b (vetor_b ou lista_coef_b)
            # Caso o valor da razao sea positivo, eh considerado no vetor razao
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
            # O valor minimo do vetor razao vai definir qual elemento sai da variaveis base, e qual elemento entra 
        vetor_razao_sem0 = vetor_razao[:]
        vetor_razao_sem0 = list(filter(lambda x: x != 0, vetor_razao))
        
        print('vetor_razao', vetor_razao)
        menor_valor_razao = min(vetor_razao_sem0)    
        print('menor_valor_razao:',menor_valor_razao)
        indice_menor_valor_razao = vetor_razao.index(menor_valor_razao)
        fila_pivo =  vetor_variaveis_C_B[indice_menor_valor_razao] 
            # Se troca a variavel que sai pela que entra
        print('vetor variaveis C_B:', vetor_variaveis_C_B)
        print('vetor_coeficientes_C_B:', vetor_coeficientes_C_B)    
        vetor_variaveis_C_B[vetor_variaveis_C_B.index(fila_pivo)] = coluna_pivo
            # Atualizando vetor C_B
        for i, variavel_C_B in enumerate(vetor_variaveis_C_B):
            # if variavel_C_B in lista_todas_variaveis:
            indice_a_ser_considerado = lista_todas_variaveis.index(variavel_C_B)
            valor_a_ser_substituido_em_C_B = coeficiente_base_tableau_C_j[indice_a_ser_considerado]       
            vetor_coeficientes_C_B[i] = valor_a_ser_substituido_em_C_B

        print('novo vetor variaveis C_B:', vetor_variaveis_C_B)
        print('novo vetor C_B:', vetor_coeficientes_C_B)
        print('matriz_A:\n', '\n'.join( '\t'+str(fila) for fila in lista_matriz_A))
        print('vetor b:\n \t' + ''.join(str(lista_coef_b)))
        print('\n     # Inicia iteracao')
        lista_matriz_A, lista_coef_b, vetor_coeficientes_C_B = funcao_calculo_iteracoes(
            lista_todas_variaveis, 
            coeficiente_base_tableau_C_j, 
            lista_matriz_A, 
            vetor_variaveis_C_B, 
            vetor_coeficientes_C_B, 
            lista_coef_b,
            coluna_pivo
            )

        print('matriz A tratada:\n' + '\n'.join('\t'+str(fila) for fila in lista_matriz_A))
        print('vetor_b tratado:\n \t' + ''.join(str(lista_coef_b)))    
        print('\n     # Inicia calculo Z_j_e_Z_j_menos_C_j')
        vetor_Z_j, vetor_C_j_menos_Z_j = funcao_calculo_Z_j_e_Z_j_menos_C_j(lista_todas_variaveis, lista_matriz_A, coeficiente_base_tableau_C_j, vetor_coeficientes_C_B)

        # print('vetor_Z_j', vetor_Z_j) 
        print('vetor_C_j_menos_Z_j', vetor_C_j_menos_Z_j)
        if k==10:
            break
        k+=1
    otimo_fo = sum(elemento_C_B*lista_coef_b[i] for i, elemento_C_B in enumerate(vetor_coeficientes_C_B) )

    texto_fim_loop = f'''
    -------------------------------------------------------
    -------------------------------------------------------
    Fim do loop:
    otimo da fo: {-otimo_fo}
    valores f.o. fase1: {coeficiente_base_tableau_C_j}
    matriz_A:\n {'\n'.join( '\t' + str(linha) for linha in lista_matriz_A)}
    vetor_b:\n \t {''.join(str(lista_coef_b))}'''   
    [print(lista) for lista in lista_C_j_Z_j_evitar_infinito]
    print(texto_fim_loop)
    return coeficiente_base_tableau_C_j, lista_matriz_A, lista_coef_b 