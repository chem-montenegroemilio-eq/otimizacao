def funcao_caso_haja_variaveis_artificias(lista_todas_variaveis):
    variaveis_artificiais = []
    teste_a = 'a_'
    for i in range(1, 20):
        variacao_teste_a = f'{teste_a}{i}'
        if variacao_teste_a in lista_todas_variaveis:
            variaveis_artificiais.append(variacao_teste_a)
    if len(variaveis_artificiais) > 0:
        print('Existem variaveis artificiais:\n', variaveis_artificiais) 
        return True
    else:
        return False