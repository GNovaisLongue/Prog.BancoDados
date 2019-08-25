#Desvio Condicional

#1. Faça um Programa que peça dois números e imprima o maior deles.
a,b = [float(x) for x in input("Entre com dois valores: (n1 n2)\n").split()]
if a>b:
    print(f"a={a} > b={b}.")
else:
    print(f"b={b} > a={a}.")

print("")
# 1. Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# - A mensagem "Reprovado", se a média for menor do que sete;
# - A mensagem "Aprovado com Distinção", se a média for igual a dez.
n1,n2 = [float(x) for x in input("Entre com as notas n1 e n2: [n1 n2]\n").split()]
media =(n1+n2)/2
if media == 10:
    print("Aluno Aprovado com distinção")
elif media >= 7:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado") 

print("")
# 2. Faça um programa que lê as duas notas parciais obtidas 
# por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:  
# Média de Aproveitamento  Conceito  
# Entre 9.0 e 10.0        A  
# Entre 7.5 e 9.0         B  
# Entre 6.0 e 7.5         C  
# Entre 4.0 e 6.0         D  
# Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e 
# a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1,n2 = [float(x) for x in input("Entre com as notas n1 e n2: [n1 n2]\n").split()]
media =(n1+n2)/2
print("\nnota 1 = ",n1,"\nnota 2 = ",n2,f"\nmedia = {media}")
if media <= 10 and media >= 9:
    print("\nConceito: A")
elif media <= 9 and media >= 7.5:
    print("\nConceito: B")
elif media <= 7.5 and media >= 6:
    print("\nConceito: C")
elif media <= 6 and media >= 4:
    print("\nConceito: D")
else:
    print("\nConceito: E")
if media >=6:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado") 

print("")
# 3. Faça um Programa que peça um número correspondente a um determinado ano e 
# em seguida informe se este ano é ou não bissexto.
#multiplo de 4, exceto multiplo de 100 mas não de 400
ano = 1
while ano !=0:
    ano = int(input("Insira um ano no formato yyyy: (0 para sair do loop)"))
    if ano == 0:
        pass
    elif ano%4==0 and ano%100!=0 or ano%400==0:
        print("Ano Bissexto")
    else:
        print("Não é um ano Bissexto!")
else:
    print("saindo do while")

print("")
# 4. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#  par ou ímpar;
def par_impar(n):
    if n > 0 and n % 2 == 0:
        return "é par"
    else:
        return "é ímpar"
# positivo ou negativo;
def pos_neg(n):
    if n > 0:
        return "é positivo"
    else:
        return "é negativo"
# inteiro ou decimal.
def int_dec(n):
    if n % 1 != 0:
        return "é decimal"
    else:
        return "é inteiro"
# #------------------------------------------------
n1 = float(input("Digite valor 1: "))
n2 = float(input("Digite valor 2: "))
op = int(
    input("insira o digito que corresponda à operação desejada:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão(real)\n5-Divisão(Inteiro)\n6-Divisão(Resto)\n7-Potência\n")
)
#Dicionario
# "Switch-CASE"
res = 0.0
def soma():
    res = n1 + n2
    return print(f"Resultado = {res}.\nO valor",par_impar(res),",",pos_neg(res),",",int_dec(res),".")
def Subtração():
    res = n1 - n2
    return print(f"Resultado = {res}.\nO valor ",par_impar(res),", ",pos_neg(res),", ",int_dec(res),".")
def Multiplicação():
    res = n1 * n2
    return print(f"Resultado = {res}.\nO valor ",par_impar(res),", ",pos_neg(res),", ",int_dec(res),".")
def Divisão():
    res = n1 / n2
    return print(f"Resultado = {res}.\nO valor ",par_impar(res),", ",pos_neg(res),", ",int_dec(res),".")
def div_int():
    res = n1 // n2
    return print(f"Resultado = {res}.\nO valor ",par_impar(res),", ",pos_neg(res),", ",int_dec(res),".")
def Resto():
    res = n1 % n2
    return print(f"Resultado = {res}.\nO valor ",par_impar(res),", ",pos_neg(res),", ",int_dec(res),".")
def Potência():
    res = n1 ** n2
    return print(f"Resultado = {res}.\nO valor ",par_impar(res),", ",pos_neg(res),", ",int_dec(res),".")

switch = {1:soma,2:Subtração,3:Multiplicação,4:Divisão,5:div_int,6:Resto,7:Potência}
#Não pode armazenar tuplas
def operandos(op):
    if op in switch:
        func = switch.get(op)
        return func()
    else:
        print("Valor invalido inserido")
operandos(op)#verifica o valor atribuido pelo usuario em 'op' e verifica o valor no dicionario chamado 'switch'

print("")
# 5. Faça um Programa que leia um número e exiba o dia correspondente da semana. 
#   (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valorinválido.
dias = ["Domingo" , "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado"]
d = int(input("Insira um digito de 1 até 7: "))
nums = [x for x in range (1, 8)]
map = dict(zip(nums, dias))
if d < 8 and d >=1:
    print(map[d])
else:
    print("Valor invalido inserido")

print("")
# 6. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. 
# Confira:             Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por K
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: 
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

dict_carne={1: ["File Duplo",4.90], 2: ["Alcatra",5.90], 3: ["Picanha",6.90]} #carnes
tipo_carne = int(input(
    "Selecione o tipe da carne:\n1-File Duplo\n2-Alcatra\n3-Picanha\n")
    )
while tipo_carne > 3 or tipo_carne < 1: # 1 2 3
    print("valor invalido inserido. Insira um valor valido")
else:
    quant_carne = int(input("Insira a quantidade, em Kg, a ser comprada: "))
    #se comprar mais de 5kg
    if quant_carne > 5:
        preco = (dict_carne[tipo_carne][-1] + 0.90) * quant_carne 
    # se comprar menos
    elif quant_carne > 0 and quant_carne <=5: 
        preco = (dict_carne[tipo_carne][-1]) * quant_carne 
    else:
        preco = 0
        print("Valor invalido inserido.")

    cartao = int(input("Compra feita no cartao? (desconto 5%)\n1-Sim\n2-Não\n"))
    if cartao == 1: #desconto
        print("Cupom Fiscal:")
        print(
            "Tipo da carne: ",dict_carne[tipo_carne][0],
            "Quantidade (Kg): ", quant_carne,
            "Preco por quilograma: ",dict_carne[tipo_carne][-1],
            f"\npreco: {preco:.4g}",
            "\npagamento: Cartao Tabajara",
            f"\nValor desconto: {(preco*0.05):.4g}",
            "\nValor a pagar: ", preco - preco * 0.05 )
    else: #mesmo que não seja '2'/não
        print("Cupom Fiscal:")
        print(
            "\nTipo da carne: ",dict_carne[tipo_carne][0],
            "Quantidade (Kg): ", quant_carne,
            "Preco por quilograma: ",dict_carne[tipo_carne][-1],
            f"\npreco: {preco:.4g}",
            "\npagamento: dinheiro",
            "\nValor desconto: ", 0,
            f"\nValor a pagar: {preco:.4g}" )
        

    