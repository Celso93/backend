'''
Faca um programa que: dada um lista
[1,2,3,4,5,6,7,8,9,10] e um numero inteiro
imprima a tabuada desse numero
'''
tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = int(input("Qual tabuda inteira voce quer saber ? "))

for multiplicador in tabuada:
    print(multiplicador * numero)