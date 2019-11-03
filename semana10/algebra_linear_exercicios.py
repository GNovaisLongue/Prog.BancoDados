import math
import random

# 1 Escreva uma função que calcula a covariância entre idade e número de amigos.

def dot(v, w):
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])

def variance(v):
    mean = sum(v) / len(v)
    return [v_i - mean for v_i in v]

#Covariancia
def covariance(x,y):
    return dot (variance(x), variance(y)) / (len(x) - 1)

# 2 Escreva uma função que calcula a correlação entre idade e número de amigos.

def sum_dot_squares(v):
    return dot(v, v)

#Correlacao
def correlation (x, y):
    desvio_padrao_x = math.sqrt(sum_dot_squares(variance(x)) / (len(x) - 1))
    desvio_padrao_y = math.sqrt(sum_dot_squares(variance(y)) / (len(y) - 1))
    if desvio_padrao_x > 0 and desvio_padrao_y > 0:
        return covariance(x, y) / desvio_padrao_y / desvio_padrao_x
    else:
        return 0


# 3 Escreva uma função que devolve uma tupla de duas listas.
# A primeira lista contém quantidades de amigos que cada usuário da rede tem. 
# A segunda, quantidades de minutos passados em média na rede por cada usuário. 
# Cada lista tem tamanho n, sendo n um valor recebido como parâmetro.
# Os dados devem ser gerados aleatoriamente. Faça três versões.

# 3.1 Gere dados aleatoriamente garantindo correlação próxima de 1.
def gera__listas_1(qtd_pessoas):
    l_amigos = []
    l_tempo = []
    for _ in range(qtd_pessoas):
        amigos = random.randrange(10, 500, 10)#min,max,passo
        l_amigos.append(amigos)

        # tempo = random.randrange(1, amigos/2)
        tempo = random.randrange(amigos*.5, amigos, 1)
        l_tempo.append(tempo)
    return l_amigos, l_tempo

def test_correlation_1():
    lista = gera__listas_1(5)
    print(f'lista: {lista}')
    print(f'Correlacao: {correlation(lista[0], lista[1])}')

# 3.2 Gere dados aleatoriamente garantindo correlação próxima de -1.
def gera__listas__1(qtd_pessoas):
    l_amigos = []
    l_tempo = []
    for _ in range(qtd_pessoas):
        amigos = random.randrange(10, 500, 10)#min,max,passo
        l_amigos.append(amigos)

        # tempo = random.randrange(1, amigos/2)
        tempo = random.randrange(amigos//4, amigos//2,10)
        l_tempo.append(tempo)
    return l_amigos, l_tempo

def test_correlation__1():
    lista = gera__listas__1(5)
    print(f'lista: {lista}')
    print(f'Correlacao: {correlation(lista[0], lista[1])}')

# 3.3 Gere dados aleatoriamente garantindo correlação próxima de 0. 
# 
# 4 Escreva uma função de teste que mostra que os dados gerados no Exercício 3 estão de 
# acordo com o solicitado.
def main():
    test_correlation_1()
    # test_correlation__1()

main()
