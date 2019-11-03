import math
import random
import string

# ADD


def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def test_vector_add():
    v = [1, 5, 7, 9]
    w = [1, 1, 2, 3]
    print('v: ' + str(v))
    print('w: ' + str(w))
    print('v + w: ' + str(vector_add(v, w)))

# SUB


def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def test_vector_subtract():
    v = [1, 5, 7, 9]
    w = [1, 1, 2, 3]
    print('v: ' + str(v))
    print('w: ' + str(w))
    print('v - w: ' + str(vector_subtract(v, w)))

# SUM


def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result


def test_vector_sum():
    v = [1, 2, 3, 4]
    w = [5, 6, 7, 2]
    z = [6, 5, 4, 1]
    soma = vector_sum([v, w, z])
    print('v ' + str(v))
    print('w ' + str(w))
    print('z ' + str(z))
    print('soma ' + str(soma))

# ESCALAR MULT


def scalar_multiply(c, v):
    return [c * v_i for v_i in v]


def test_scalar_multiply():
    c = 5
    v = [1, 3, 4, 5, 6]
    print('c ' + str(c))
    print('v ' + str(v))
    print('c * v ' + str(scalar_multiply(c, v)))

# VECTOR MEAN


def vector_mean(vectors):
    n = len(vectors)
    # SUM([2, 4, 5, 6, 7]) / n
    return scalar_multiply((1 / n), vector_sum(vectors))


def test_vector_mean():
    v = [2, 3, 7, 6]
    w = [4, 3, 2, 1]
    z = [7, 6, 8, 1]
    print('v ' + str(v))
    print('w ' + str(w))
    print('z ' + str(z))
    print('media ' + str(vector_mean([v, w, z])))

# dot product - produto escalar


def dot(v, w):
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])


def test_dot():
    v = [1, 2, 7, 8]
    w = [4, 1, 2, 3]
    print('v ' + str(v))
    print('w ' + str(w))
    print('v.w ' + str(dot(v, w)))

# SUM SQUARES


def sum_dot_squares(v):
    return dot(v, v)


def test_sum_dot_squares():
    v = [1, 2, 7, 8]
    print('v ' + str(v))
    print('v^2 ' + str(sum_dot_squares(v)))

# MAGNITUDE


def magnitude(v):
    return math.sqrt(sum_dot_squares(v))


def test_magnitude():
    v = [1, 2, 3, 4]
    print('v ' + str(v))
    print('magnitude(v)' + str(magnitude(v)))

# SQUARED DISTANCE - DISTANCIA EUCLIDIANA


def squared_distance(v, w):
    return sum_dot_squares(vector_subtract(v, w))


def distance(v, w):
    return math.sqrt(squared_distance(v, w))


def test_distance():
    v = [2, 1]
    w = [3, 3]
    print('v ' + str(v))
    print('w ' + str(w))
    print('distance(v,w) ' + str(distance(v, w)))


# 1. gerar uma base de 10 pessoas com: idade, sexo, salario.
# https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits?rq=1
# 2. As pessoas devem ter idade entre 16 e 40 anos.
# 3. Os valores de sexo para M e F.
# 4. O salario deve ser algo entre 1000 e 5000.
def gerar_base(qtd_pessoas):
    dict = {}
    for p in range(qtd_pessoas):
        idade = random.randrange(16, 40)
        sexo_num = ord(random.choice(['M', 'F']))  # 77 ou 70
        sexo = sexo_num * sexo_num / 2
        salario = random.randrange(1000, 5000, 100)
        dict[p] = [idade, sexo, salario]
    return dict

# 5. Escrever uma função que, dada duas pessoas, calcula e devolve a distancia.


def distance_a_to_b(p1_values, p2_values):
    return math.sqrt(
        squared_distance(
            p1_values,
            p2_values
        )
    )


def test_distance_a_to_b():  # ord
    dict = gerar_base(10)
    print(dict)
    print('primeiro ' + str(dict[0]))
    print('segundo ' + str(dict[1]))
    print('Distancia entre eles ' + str(distance_a_to_b(dict[0], dict[1])))


# --------------29/10/2019

#VARIANCIA, COVARIANCIA E CORRELAÇÃO
def qtde_amigos_minutos_passados ():
    return ([1, 10, 50, 2, 150], [5, 200, 350, 17, 1])


#Variancia
def variance(v):
    mean = sum(v) / len(v)
    return [v_i - mean for v_i in v]

def test_variance():
    v = [1,2,3]
    print('variance ' + str(variance(v)))

#Covariancia
def covariance(x,y):
    return dot (variance(x), variance(y)) / (len(x) - 1)

def test_covariance():
    #teste 1
    x = [3, 12, 3]
    y = [1, 7, 4]
    print('variance x ' + str(variance(x)))
    print('variance y ' + str(variance(y)))
    print(f'covariance: {covariance(x, y)}')
    #teste 2
    x = [-1, 8, 11]
    y = [8, 2, 2]
    print('variance x ' + str(variance(x)))
    print('variance y ' + str(variance(y)))
    print (f'covariance: {covariance(x, y)}')
    #teste 3
    x = [8, 6, 4]
    y = [2, 6, 4]
    print('variance x ' + str(variance(x)))
    print('variance y ' + str(variance(y)))
    print (f'covariance: {covariance(x, y)}')

#Correlacao
def correlation (x, y):
    desvio_padrao_x = math.sqrt(sum_dot_squares(variance(x)) / (len(x) - 1))
    desvio_padrao_y = math.sqrt(sum_dot_squares(variance(y)) / (len(y) - 1))
    if desvio_padrao_x > 0 and desvio_padrao_y > 0:
        return covariance(x, y) / desvio_padrao_y / desvio_padrao_x
    else:
        return 0

def test_correlation():
    listas = [
        ([3,12,13], [1,7,4]),#0.8170571691028833
        ([-1,8,11], [8,2,2]),#-0.9707253433941511
        ([8,6,4], [2,6,4])#-0.5
    ]
    for i, elemento in enumerate(listas):
        print('Teste ' + str(i))
        print(f'Correlacao: {correlation(elemento[0], elemento[1])}')

def test_correlacao_com_outlier():
    data = qtde_amigos_minutos_passados()
    print(f'Correlacao com outlier: {correlation(data[0], data[1])}')

def test_correlacao_sem_outlier():
    data = qtde_amigos_minutos_passados()
    print(f'Correlacao sem outlier: {correlation( data[0][ :len(data[0]) -1 ], data[1][ :len(data[1]) -1 ] ) }')





# 6. Escrever uma função que calcula a distância entre todas as pessoas, duas a duas.
def distance_base(dict):
    pass

def main():
    # test_vector_add()
    # test_vector_subtract()
    # test_vector_sum()
    # test_scalar_multiply()
    # test_vector_mean()
    # test_dot()
    # test_sum_dot_squares()
    # test_magnitude()
    # test_distance()
    # test_distance_a_to_b()


    # --------------29/10/2019
    # test_variance()
    # test_covariance()
    test_correlation()
    # test_correlacao_com_outlier()
    # test_correlacao_sem_outlier()
    # pass

main()

