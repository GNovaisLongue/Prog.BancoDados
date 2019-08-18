import math
#introducao_python_estrutura_sequencial_exercicios

# 1 Escreva um programa que obtém o salário de um funcionário, calcula e mostra o salário,
# sabendo que ele sofreu um aumento de 25%.

# salario = int(input("Digite seu salario: "))
# #25 por cent
# print( salario+(salario*0.25) )
# print()


# 2 Escreva um programa que recebe o salário base de um funcionário, calcula e mostra o salário a
# receber, sabendo-se que esse funcionário tem gratificação de 5% sobre o salário base e paga
# imposto de 7% sobre o salário base.

# salario = int(input("Digite seu salario: "))
# # +5 por cento
# # -7 por cento
# # print( salario+(salario*0.05) )
# # print( salario-(salario*0.07) )
# print( salario+(salario*0.05)-(salario*0.07) )
# print()


# 3 Escreva um programa que calcula e mostra a área de um círculo, uma vez que o usuário
# informe o raio. Use math.pi para obter um valor aproximado de pi. (Use import math antes).
# pi*r**2
# raio = float(input("Informe o raio de um circulo: "))
# print ("A área deste círculo é, aproximadamente: ", math.pi*(raio**2))


# 4 Sabe-se que:
# 1 pé = 12 polegadas
# 1 jarda = 3 pés = 36 polegadas
# 1 milha = 1.760 jardas = 5280 pés = 63360 polegadas
# Faça um programa que obtém uma medida em pés, e faz as conversões a seguir, mostrando os
# resultados logo ao final.
# a) polegadas
# b) jardas
# c) milhas
# feet = float(input("insira o tamanho do seu pé: "))
# print("Seu pé dá: ", (feet*12)," dedão(ões)(in).")
# print("Seu pé dá: ", (feet/3)," quintal(is) (yd).")
# print("Seu pé dá: ", (feet/5280)," pés de centurião(m).")