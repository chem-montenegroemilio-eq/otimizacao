# ESTE _parser TRATA OS DADOS BRUTOS A SEREM CONVERTIDOS EM LISTAS A SEREM CALCULADAS PELO SIMPLEX


### Criando funcao para diferenciar componentes de equacao: coeficientes e variaveis
def funcao_coef_variaveis(string_equacao):
    # isto esta ok, e consiste em tirar os sinais positivos ou negativos dos coeficientes
    lista_sinal_coeficientes = []
    for elemento in string_equacao:
        if elemento == '+':
            lista_sinal_coeficientes.append(elemento)
        if elemento == '-':
            lista_sinal_coeficientes.append(elemento)
    # isto esta ok, e consiste em tirar os coeficientes e que a mesma dimensao da lista dos sinais concida com os coeficientes
    novo_string = string_equacao
    for i in range(1,100):
        for sep in ['x_', 's_', 'e_', 'a_']:
            novo_string = novo_string.replace(f'{sep}{i}', 'o')
    novo_string = novo_string.replace(' ', '').replace('+', '').replace('-', '')    
    while 'oo' in novo_string:
        novo_string = novo_string.replace('oo', 'o1o')
    lista_coeficiente = novo_string.split('o')    
    if '' in lista_coeficiente:
        lista_coeficiente.remove('')
    elif ' ' in lista_coeficiente:
        lista_coeficiente.remove(' ')
    # aqui separa pelos segmentos que contem coeficientes e x_ ou s_ ou e_
    separando_equacao = string_equacao.replace('-', '+').split('+')
    if '' in separando_equacao:
        separando_equacao.remove('')
    elif ' ' in separando_equacao:
        separando_equacao.remove(' ')
    dicionario_c={}
    # se utiliza a separacao em partes para criar um dicionario que outorgue coeficientes as respectivas variaveis 
    for i, elemento in enumerate(separando_equacao):
        if 'x' in elemento:
            coeficiente, variavel = elemento.split('x')
            dicionario_c[f'x{variavel.strip()}'] = float(f'{lista_sinal_coeficientes[i]}{lista_coeficiente[i].strip()}')
        elif 's' in elemento:
            coeficiente, variavel = elemento.split('s')
            dicionario_c[f's{variavel.strip()}'] = float(f'{lista_sinal_coeficientes[i]}{lista_coeficiente[i].strip()}')
        elif 'e' in elemento:
            coeficiente, variavel = elemento.split('e')
            dicionario_c[f'e{variavel.strip()}'] = float(f'{lista_sinal_coeficientes[i]}{lista_coeficiente[i].strip()}')
        elif 'a' in elemento:
            coeficiente, variavel = elemento.split('a')
            dicionario_c[f'a{variavel.strip()}'] = float(f'{lista_sinal_coeficientes[i]}{lista_coeficiente[i].strip()}')
    return dicionario_c


### Funcao para criar matriz de restricoes A, considerando variaveis folga, excedentes, e artificiais
def matriz_restricoes(lista_restricoes):
        # caso <=, entao adicionar s_i (variavel de folga)
    i = 1
    tupla_matriz_A = ()
    tupla_coef_b = ()
    for restricao in lista_restricoes:
        if '<=' in restricao:
            equacao_restricao, coef_b = restricao.split('<=') 
            equacao_restricao = equacao_restricao + f'+ 1s_{i}'
            equacao_restricao = funcao_tratamento_string_inicio_equacao(equacao_restricao)
        # caso >=, entao adicionar e_i (variavel excedente) e tambem a_i (variavel artificial)
        elif '>=' in restricao:
            equacao_restricao, coef_b = restricao.split('>=')
            equacao_restricao = equacao_restricao + f'- 1e_{i} '
            equacao_restricao = equacao_restricao + f'+ 1a_{i} '
            equacao_restricao = funcao_tratamento_string_inicio_equacao(equacao_restricao)
        # caso ==, entao adicionar a_i
        elif '==' in restricao:
            equacao_restricao, coef_b = restricao.split('==')
            equacao_restricao = equacao_restricao + f'+ 1a_{i} '
            equacao_restricao = funcao_tratamento_string_inicio_equacao(equacao_restricao)
        dicionario_restricao = funcao_coef_variaveis(equacao_restricao)  
        tupla_matriz_A += (dicionario_restricao, )
        tupla_coef_b += (float(coef_b.strip()), )
        
        i += 1
    return tupla_matriz_A, tupla_coef_b


### Funcao conversao dicionario de restricao em lista de restricoes
def funcao_conversao_dicionario_restricao_em_lista_restricao(tupla_restricoes, lista_todas_variaveis):
    lista_matriz_A = []
    lista_restricao = []
    for dicionario_restricao in tupla_restricoes:
        lista_restricao = []
        for variavel in lista_todas_variaveis:
            if variavel in dicionario_restricao:
                lista_restricao.append(dicionario_restricao[variavel])
            else:   
                lista_restricao.append(0)
        lista_matriz_A.append(lista_restricao)
    return lista_matriz_A


### Funcao conversao dicionario de funcao em lista de funcao
def funcao_conversao_dicionario_funcaoobjetivo_em_lista_funcaoobjetivo(dicionario_fo, lista_todas_variaveis):
    lista_fo = []
    for variavel in lista_todas_variaveis:
        if variavel in dicionario_fo:
            lista_fo.append(dicionario_fo[variavel])
        else:   
            lista_fo.append(0)
    return lista_fo


### Funcao que trata equacoes string que nao possuem simbolo e/ou numero no inicio
def funcao_tratamento_string_inicio_equacao(equacao):
    lista_teste  = [simbolo for simbolo in equacao]
    lista_salvar_para_comparar = [] # Esta lista viabiliza a analise antes do x
    equacao_tratada_string = ''
    # percorre cada elemento da lista (a ser analisado)
    for elemento in lista_teste:
        lista_salvar_para_comparar.append(elemento)
        # analisa a equacao assim que atingir o primeiro x
        if 'x' in elemento:
            # SE nao ha simbolo
            if not '+' in lista_salvar_para_comparar and not '-' in lista_salvar_para_comparar:
                # se analisa cada elemento antes do x e se valida se ha numeros
                analisar_lista_numeros = [True if elemento.isdigit() == True else False for elemento in lista_salvar_para_comparar]
                # condicional que detecta numero e simbolo
                if True in analisar_lista_numeros:
                    # CASO 2
                    lista_auxiliar_simbolo = ['+']
                    lista_auxiliar_simbolo.extend(lista_teste)
                    lista_equacao_tratada = lista_auxiliar_simbolo
                else:
                    # CASO 1
                    lista_auxiliar_simbolo = ['+', '1']
                    lista_auxiliar_simbolo.extend(lista_teste)
                    lista_equacao_tratada = lista_auxiliar_simbolo
            # SE ha simbolo
            else:
                # se analisa cada elemento antes do x e se valida se ha numeros
                analisar_lista_numeros = [True if elemento.isdigit() == True else False for elemento in lista_salvar_para_comparar]
                if not True in analisar_lista_numeros:
                    # considera o caso que haja '+' no inicio
                    # CASO 3
                    if '+' in lista_salvar_para_comparar:
                        posicao_do_mais = lista_salvar_para_comparar.index('+')
                        string_auxiliar = '+1'
                        lista_teste[posicao_do_mais] = string_auxiliar
                        lista_equacao_tratada = lista_teste
                    # considera o caso que haja '-' no inicio
                    elif '-' in lista_salvar_para_comparar:
                        posicao_do_menos = lista_salvar_para_comparar.index('-')
                        string_auxiliar = '-1'
                        lista_teste[posicao_do_menos] = string_auxiliar
                        lista_equacao_tratada = lista_teste
                else:
                    equacao_tratada_string = equacao
            break # quebra apos leitura do x (e analises posteriores)
            
    if equacao_tratada_string == equacao:
        pass
    else:
        equacao_tratada_string = ''
        for letra in lista_equacao_tratada:
            equacao_tratada_string+=letra        

    return equacao_tratada_string
