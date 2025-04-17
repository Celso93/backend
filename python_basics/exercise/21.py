'''
Dada uma lista de entradas de usuarios de numerios inteiros,
construa um dicionario com a lista padrao
a lista dos valores elevados ao quadrado
e a lista dos valores elevados ao cubo
'''

numeros_usuarios = input('Coloque uma lista de numeros inteiros separados por virguas: ').split(',')
print(numeros_usuarios)

dicionario_matematico = {
    'padrao': numeros_usuarios,
    'quadrado': [],
    'cubo': []
}

for i in range(len(numeros_usuarios)):
    numeros_usuarios[i] = int(numeros_usuarios[i])
    dicionario_matematico['quadrado'].append(numeros_usuarios[i] ** 2)
    dicionario_matematico['cubo'].append(numeros_usuarios[i] ** 3)

print(dicionario_matematico)