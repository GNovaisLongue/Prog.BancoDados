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
#class Kmeans

def restricoes(x_min, x_max, y_min, y_max):
    x = random.randint(x_min, x_max)
    y = random.randint(y_min, y_max)
    return x, y

def gera_base(n):
    l = []
    for i in range(n):
        if i < n//3:
            l.append(restricoes(-50, -40, 0, 10))
        elif i < (n//3)*2:
            l.append(restricoes(-45, -35, 5, 20))
        else:
            l.append(restricoes(20, 30, 20, 30))
    return l
    
def exibe_grafico(base):
    for i, e in enumerate(base):
        if i < len(base)//3:
            plt.plot(e[0], e[1], marker='$.$', color='green')
        elif i < (len(base)//3)*2 :
            plt.plot(e[0], e[1], marker='$.$', color='red')
        else:
            plt.plot(e[0], e[1], marker='$.$', color='black')
    r1 = mpatches.Patch(color='green', label='primeiro parte')
    r2 = mpatches.Patch(color='red', label='segundo parte')
    r3 = mpatches.Patch(color='black', label='terceiro parte')
    base = mpatches.Patch(label=f'base = {len(base)}') 
    # plt.legend(handles=[h, b])
    plt.legend(handles=[r1, r2, r3, base], bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)

def desenha_representantes(ctd):
    for _, e in enumerate(ctd):
        plt.plot(e[0], e[1],marker='$+$', color='blue', zorder=10)

def exibe_grafico_e_representantes (base):
    kmeans = KMeans(3)#numero de grupos
    kmeans.train(base)#executar KMeans
    print('Representantes:', kmeans.means)
    exibe_grafico(base)#exibir base
    desenha_representantes(kmeans.means)#exibir representantes

def teste_grafico():
    base = gera_base(50)
    for i, e in enumerate(base):
        print(f'{i}: {e}')
    exibe_grafico(base)
    plt.show()

def teste_grafico_e_representantes():
    n = int(input('Insira um valor inteiro: '))
    base = gera_base(n)#base de dados
    exibe_grafico_e_representantes(base)
    plt.show()

def main():
    # teste_grafico()
    teste_grafico_e_representantes()

main()