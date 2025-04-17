'''
Faca um programa que peca 2 numeros inteiros e um numero float.
Calcule e mostre.

O produto do dobro do primeiro com a metade do segundo.
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
'''

numero_um = int(input("digite seu primeiro numero inteiro: "))
numero_dois = int(input("digite seu segundo numero inteiro: "))
numero_float = float(input("digite seu numero float inteiro: "))

def first_exercise():
    # O produto do dobro do primeiro com a metade do segundo.
    # (primeiro*2) + (segundo/2)
    calc1 = numero_um*2
    calc2 = numero_dois/2
    result = calc1 * calc2
    print(result)

def second_exercise():
    # A soma do triplo do primeiro com o terceiro.
    calc1 = numero_um*3
    result = calc1 + numero_float
    print(result)

def third_exercise():
    result = numero_float**3
    print(result)

first_exercise()
second_exercise()
third_exercise()