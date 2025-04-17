'''
Faca um programa que itera em uma string e toda vez
que a uma vogal aparecer na sua string print o seu nome
entre as letras
'''

vogais = 'aeiou'
nome = input("Qual o seu nome?  ")

for letra in nome:
    if letra in vogais:
        print(nome)
    else:
        print(letra)
