mensagem_em_edicao = '''
Voce acaba de rodar o .Simplex() sem definir:

.adicionar_funcao_objetivo('min. + c_1 x_1 + c_1 x_2 '), em que c_j é o coeficientes das variáveis x_j respectivas.

e sem: 

.adicionar_restricao('+ a_12 x_1 + + a_22 x_2 <= 10'), em que a1,j é o coeficiente da primeira restrição (i=1) das variaveis x_j respectivas. Em que j pertence a { 1,2,3,4 }.

Segue um exemplo que consiste em conhecer o custo minimo entre quatro tecnologias diferentes (infravermelho, laser, ultrassonico e fotoacústico) com precos diferentes sendo US$ 3000, US$ 20000, US$ 30000 e US$ 10000, respectivamente. As tecnolocias possuem um tempo de deteccao (conhecido como T_90) de 20, 5, 10, e 2 segundos, respectivamente. Tambem um tempo de vida util de 10, 20, 20, e 15 anos. Isso tudo se encontra definido como restricoes. A quantidade total de detectores a comprar eh de 20, com tempo medio limite desejado de 10 segundos, pelo qual sua media ponderada eh de 20 detectores*(10 segundos/detector)=200 segundos. O tempo medio limite de vida util eh 80 segundos.
  
Qual o custo otimo? quantos de cada tecnologia?'''

mensagem  = '''Sera resolvido um pequeno problema.'''

# SOLUCIONAR PROBLEMA SIMPLEX COM RESULTADOS LP 
def executar():
    print(mensagem_em_edicao)
    fo= 'min. + 3000x_1 + 20000x_2 + 30000x_3 + 10000x_4 '
    restricoes= ['+ 1x_1 + 1x_2 + 1x_3 + 1x_4 == 20',
                '+ 20x_1 + 5x_2 + 10x_3 + 2x_4 <= 200',
                '+ 10x_1 + 20x_2 + 20x_3 + 15x_4 >= 80']
    return fo, restricoes