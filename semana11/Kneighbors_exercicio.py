import random
import math
import matplotlib.patches as mpatches
from collections import Counter
from matplotlib import pyplot as plt

class Pessoa:
    def __init__(self, idade, sexo, salario, intencao_de_voto):
        self.idade = idade
        self.sexo = sexo
        self.salario = salario
        self.intencao_de_voto = intencao_de_voto
    # string format

    def __str__(self):
        return f'idade: {self.idade}, sexo: {self.sexo}, salario: {self.salario},intencao_de_voto: {self.intencao_de_voto}'

    def __eq__(self, other):
        return self.intencao_de_voto == other.intencao_de_voto

    def __hash__(self):
        return 1


def gera_base(n):
    l = []
    for _ in range(n):
        # aleatorio no intervalo [a, b]
        idade = random.randint(18, 35)
        sexo = random.choice(['M', 'F'])
        # aleatorio no intervalo [0.0, 1.0)
        salario = 1200 + random.random() * 1300
        intencao_de_voto = random.choice(['H', 'B'])
        p = Pessoa(idade, sexo, salario, intencao_de_voto)
        l.append(p)
    return l


def distancia(p1, p2):
    idade = math.pow((p1.idade - p2.idade), 2)
    sexo = math.pow((1 if p1.sexo == 'M' else 0) -
                    (1 if p2.sexo == 'M' else 0), 2)
    salario = math.pow((p1.salario - p2.salario), 2)
    return math.sqrt(idade + sexo + salario)


def rotulo_de_maior_frequencia_sem_empate(pessoas):
    frequencias = Counter(pessoas)
    rotulo, frequencia = frequencias.most_common(1)[0]
    qtde_mais_frequentes = len([
        count
        for count in frequencias.values()
        if count == frequencia
    ])
    if qtde_mais_frequentes == 1:
        # print("K: ", len(pessoas))
        return rotulo
    return rotulo_de_maior_frequencia_sem_empate(pessoas[:-1])


def knn(k, observacoes_rotuladas, nova_observacao):
    ordenados_por_distancia = sorted(
        observacoes_rotuladas, key=lambda obs: distancia(obs, nova_observacao))
    k_mais_proximo = ordenados_por_distancia[:k]
    resultado = rotulo_de_maior_frequencia_sem_empate(k_mais_proximo)
    return k_mais_proximo, resultado.intencao_de_voto


def cross_validation_leave_one_out(base):
    acertos = 0
    erros = 0
    for tupla in enumerate(base):
        instancia_a_rotular = tupla[1]
        base_a_ser_usada = base[0:tupla[0]] + base[tupla[0] + 1:]
        # print("Base a ser usada: " + str(base_a_ser_usada))
        k_mais_proximo, resultado = knn(5, base_a_ser_usada, instancia_a_rotular)
        if resultado == instancia_a_rotular.intencao_de_voto:
            acertos += 1
        else:
            erros += 1
    desenha_ctd(k_mais_proximo)
    print(f'Intencao de Voto: {instancia_a_rotular.intencao_de_voto}\nAcertos: {acertos}, Erros: {erros}')

def desenha_pontos(lista_classificada):
    for i in lista_classificada:
        if i.intencao_de_voto == 'H':
            plt.plot(i.idade, i.salario, marker='$.$', color='blue', label="H")
        else:
            plt.plot(i.idade, i.salario, marker='$.$', color='red', label="B")
    h = mpatches.Patch(color='blue', label='H')
    b = mpatches.Patch(color='red', label='B')
    # plt.legend(handles=[h, b])
    plt.legend(handles=[h, b], bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)

def desenha_ctd(ctd):
    for i in ctd:
        plt.plot(i.idade,i.salario,marker='$P$',color='black', zorder=10)


def main():
   base = gera_base(100)
   cross_validation_leave_one_out(base)
   desenha_pontos(base)
   plt.show()

main()
