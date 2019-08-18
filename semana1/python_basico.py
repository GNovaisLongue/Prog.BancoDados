#1
import math
print ("hello, Python 3!")

#2
# val1 = int( input ("Digite o primeiro valor: ")) #considerar para tipo inteiro um valor inserido
# val2 = int( input ("Digite o segundo valor: "))
# val3 = int( input ("Digite o terceiro valor: "))
# soma = val1+val2+val3
# print (soma)
# print()

#3
#https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
# v1, v2, v3 = [int(x) for x in input("Entre com tres valores: ").split()]
# print (v1+v2+v3)
# print()

#4
# salario = int(input("Digite seu salario: "))
# #32 por cent
# print( salario+(salario*0.32) )
# print()

#5
#https://www.geeksforgeeks.org/python-math-function-sqrt/
#baskhara delta = b**2 -4*a*c
#raiz positiva -> ( -b + sqrt(delta) )/2*a
#raiz negativa -> ( -b - sqrt(delta) )/2*a
#a*x**2 + b*x + c
#delta > 0 -> duas raízes; = 0 -> uma raiz; < 0 -> não há raiz

# a, b, c = [int(x) for x in input("Entre com tres valores para coeficientes: ").split()]
# delta = (b**2)-(4*a*c)
# if delta > 0:
#     #1 -2 -3
#     print("Tem duas raizes")
#     print("Raiz positiva: ", (-b + (math.sqrt(delta))) / (2*a) )
#     print("Raiz negativa: ", (-b - (math.sqrt(delta))) / (2*a) )
# elif delta == 0:
#     #1 8 16
#     print("Tem apenas uma raiz")
#     print("Raiz positiva: ", (-b + (math.sqrt(delta))) / (2*a) )
#     print("Raiz negativa: ", (-b - (math.sqrt(delta))) / (2*a) )
# else:
#     #1 8 17
#     print("Não há raizes")

#6
# ano_nasc = int(input("Insira seu ano de nascimento: (aaaa) "))
# print("Voce tem ", (2019-ano_nasc), " anos.")
# print("Voce viveu, aproximadamente, ", ((2019-ano_nasc)*365), " dias.")
# print("Voce tera", (2052-ano_nasc), " anos em 2052.")
# if ano_nasc != 0:
#     ano_escolha = int(input("Digite um ano qualquer depois de seu nascimento: "))
#     if ano_escolha>ano_nasc:
#         print("Voce tinha/terá ", (ano_escolha-ano_nasc), " anos.")
#     else:
#         print("ano inserido menor que idade de nascimento")

#7
# peso = int(input("insira o peso em quilos: "))
# comida = int(input("quanto de comida, em gramas, voce dá diariamente para cada um de seus gatos? "))
# print("Restará ", ((peso*1000)-(comida*2*5)), " gramas de ração após 5 dias.")
