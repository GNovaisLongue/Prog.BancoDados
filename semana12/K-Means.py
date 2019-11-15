import math
import random


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


class KMeans:
    def __init__(self, k, means=None):
        self.k = k
        self.means = means

    def classify (self, ponto):
        return min (range (self.k), key = lambda i: squared_distance(ponto, self.means[i]))

    def train (self, pontos):
        # escolha de k elementos
        self.means = random.sample(pontos, self.k) if self.means == None else self.means
        # nenhuma atribuição, para começar
        assignments = None
        while True:
            # associa cada instância a um inteiro 0 <= i < k
            new_assignments = list(map (self.classify, pontos))
            # se não houver mudança, termina
            if new_assignments == assignments:
                return
            # atribuição atual se torna a nova
            assignments = new_assignments
            # cálculo das novas médias
            for i in range (self.k):
                # pontos associados ao agrupamento i
                # note que pontos e assignments estão na ordem
                # por exemplo pontos = [1, 2, 3] e assignments = [1, 2, 2]
                # indicam que a primeira instância está no grupo 1 e as demais
                # no grupo 2
                i_points = [p for p, a in zip (pontos, assignments) if a == i]
                # tem alguém nesse grupo?
                if i_points:
                    self.means[i] = vector_mean (i_points)
#class


def test_k_means ():
    dados = [[1], [3], [6], [7], [10], [11]]
    kmeans = KMeans(3, [[1], [3], [11]])
    kmeans.train(dados)
    print (kmeans.means)

def test_k_means_rand ():
    dados = [[1], [3], [6], [7], [10], [11]]
    kmeans = KMeans(3)
    kmeans.train(dados)
    print (kmeans.means)

def main():
    # test_k_means()
    test_k_means_rand()

main()
#Adapte o algoritmo para que seja possível verificar cada um dos grupos.
