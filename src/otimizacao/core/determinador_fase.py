def funcao_caso_haja_variaveis_artificias(lista_todas_variaveis):
    variaveis_artificiais = []
    teste_a = 'a_'
    for i, variavel in enumerate(lista_todas_variaveis):
        variacao_teste_a = f'{teste_a}{i}'
        if variacao_teste_a in lista_todas_variaveis:
            variaveis_artificiais.append(variacao_teste_a)
    if len(variaveis_artificiais) > 0: 
        return variaveis_artificiais
    else:
        return False