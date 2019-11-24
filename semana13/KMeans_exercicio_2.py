import math
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def scalar_multiply(escalar, vetor):
    return [escalar * i for i in vetor]

def vector_sum(vetores):
    resultado = vetores[0]
    for vetor in vetores[1:]:
        resultado = [resultado[i] + vetor[i] for i in range(len(vetor))]
    return resultado

def vector_mean(vetores):
    return scalar_multiply(1/len(vetores), vector_sum(vetores))

def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def sum_of_squares(v):
    return dot(v, v)

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance (v, w):
    return math.sqrt(squared_distance(v, w))

class KMeans:
    def __init__(self, k, means=None):
        self.k = k
        self.means = means

    def classify (self, ponto):
        return min (range (self.k), key = lambda i: squared_distance(ponto, self.means[i]))

    def train (self, pontos):
        self.means = random.sample(pontos, self.k) if self.means == None else self.means
        assignments = None
        while True:
            new_assignments = list(map (self.classify, pontos))
            if new_assignments == assignments:
                return
            assignments = new_assignments
            for i in range (self.k):
                i_points = [p for p, a in zip (pontos, assignments) if a == i]
                if i_points:
                    self.means[i] = vector_mean (i_points)
#class Kmeans

def gera_base (n):    
    base = []    
    for _ in range(n // 3):
        x = random.randint(-50, -40)
        y = random.randint(0, 10)
        while (x, y) in base:
            x = random.randint(-50, -40)
            y = random.randint(0, 10)
        base.append((x, y))
    for _ in range(n // 3):
        x = random.randint(-40, -10)
        y = random.randint(-10, 0)
        while (x, y) in base:            
            x = random.randint(-40, -10)            
            y = random.randint(-10, 0)        
        base.append((x, y))    
    for _ in range(n // 3):        
        x = random.randint(10, 20)        
        y = random.randint(10, 20)        
        while (x, y) in base:            
            x = random.randint(10, 20)            
            y = random.randint(10, 20)        
        base.append((x, y))     
    return base

def calcula_somatorio_de_distancias (base, kmeans):
    soma = 0
    for b in base:
        dist = distance (b, kmeans.means[0])
        for representante in kmeans.means[1:]:
            if distance (b, representante) < dist:
                dist = distance (b, representante)
        soma += dist
    return soma

def exibe_grafico (base, representantes=[], distancia=-1):
    g1_x = [v[0] for v in base[:len(base)//3]]
    g1_y = [v[1] for v in base[:len(base)//3]]

    g2_x = [v[0] for v in base[len(base)//3: len(base)//3 * 2 ]]
    g2_y = [v[1] for v in base[len(base)//3: len(base)//3 * 2 ]]

    g3_x = [v[0] for v in base[len(base)//3 * 2: len(base)]]
    g3_y = [v[1] for v in base[len(base)//3 * 2: len(base)]]

    plt.scatter (g1_x, g1_y, marker='8')
    plt.scatter (g2_x, g2_y, marker='D')
    plt.scatter (g3_x, g3_y, marker='^')
    for r in representantes:
        plt.scatter (r[0], r[1], marker="+")

    plt.title(f'Somatório de distâncias: {distancia:.2f}')
    plt.show()

def test_final ():
    base = gera_base (120)#max 363
    kmeans = KMeans (3)
    kmeans.train(base)
    distancia = calcula_somatorio_de_distancias(base, kmeans)
    exibe_grafico (base, kmeans.means, distancia)



# Implemente a seguinte função. 
# Para cada valor de k (a partir de 2), ela executa o algoritmo KMeans  i  vezes e 
# utiliza a função da aula de cálculo de distâncias, a fim de obter a distância média, m. 
# Ela deve devolver o menor valor de k tal que m < limiar.

def calcula_media_distancias(base, k, i):
    media = 0
    kmeans = KMeans(k)
    while i > 0:
        kmeans.train(base)# gerar agrupamentos e representantes
        media += calcula_somatorio_de_distancias(base,kmeans)
        media /= i 
        i-=1 # i até 0
    # print(f'media = {media} com K = {k}')
    return media

def obtem_melhor_k (base, i, limiar):#100,20,30
    k = 2
    media = limiar
    while media >= limiar:
        k_limiar = k
        media = calcula_media_distancias(base, k, i)
        # while i >= 0:#20 até 0
        #     kmeans.train(base)# gerar agrupamentos e representantes
        #     media += calcula_somatorio_de_distancias(base,kmeans)
        #     media = media / i 
        #     i-=1 # Contador --    
        # print(f'media = {media} com K = {k}')
        k+=1
    return k_limiar


def teste_obtem_melhor_k():
    base = gera_base(100)
    print(obtem_melhor_k(base, 10, 90))


def main():
    teste_obtem_melhor_k()

main()