'''
Desafio 01
Converta o loop abaixo para uma compreensão de lista:
valores = [30, 50, 100, 120]
triplos = []
for valor in valores:
    triplo = valor * 3
    triplos.append(triplo)
    print(triplos)
'''

# Desafio 01
valores = [30, 50, 100, 120]

triplos = [
    valor * 3
    for valor in valores
]
print(triplos)



# Desafio 02
'''
Decomposicao
criar a lista de palavras
dicionário resultante
    chave deve estar em letra minuscula
    valor e a contagem de caracteres
        nao pode contar espaco em branco

#Posssibilidade:
#diccionario = 
#    posicao.diminuir: posicao(index.removerespacoem banco)
#    for posicao em lista
#      
'''
# https://www.w3schools.com/python/python_ref_string.asp
palavras = ['One piece', 'Hunter x Hunter', 'Naruto', 'Medalist', 'Golden Kamuy']
dict_caracteres = {
    manga.lower(): len(manga.replace(" ", ""))
    for manga in palavras
}

print(dict_caracteres)




# Desafio 03
'''
Desafio 03
Meus amigos possuem os seguintes interesses:
• Gostam de programação: Ricardo, Roberto, Pedro, Vinicius
• Gostam de jogar futebol: Mateus, Roberto, Paulo, Vinicius
• Estudam python: Ricardo, Mateus, Paulo, Pedro

Usando operações de conjunto, encontre o conjunto de amigos:
    que gostam de programação e estudam python
    mas que não gostam de jogar futebol

decompondo
criar as variaveis (conjutnos)
    progamacao = [Ricardo, Roberto, Pedro, Vinicius]
    futebol = [Mateus, Roberto, Paulo, Vinicius]
    python = [Ricardo, Mateus, Paulo, Pedro]

resultado final
    programacao e python
    mas nao gosta de futbol
'''
progamacao = {'Ricardo', 'Roberto', 'Pedro', 'Vinicius'}
futebol = {'Mateus', 'Roberto', 'Paulo', 'Vinicius'}
python = {'Ricardo', 'Mateus', 'Paulo', 'Pedro'}

gostam_programacao_python = progamacao.intersection(python)
nao_gosta_futebol = gostam_programacao_python.difference(futebol)

print(gostam_programacao_python)
print(nao_gosta_futebol)
