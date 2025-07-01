# Crie um codigo que implementa a cifra de cesa, isto e, que
# transforma  um string movendo cada letra um certo numero de
# passos no alfabeto. O numero de passos e dado por uma chave.
# letra com acentos, espacos e pontuacao permanecem iguais

# exemplo:
# "abc" com 1 = "bcd"
# "ABCDE" com 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"
# "Ola mundo!" com chave 3 = "Roa Pxqgr"

#dica: construa 2 strings com as letras do alfabeto em ordem,
# um para letra minusculas e outra para maiusculas, e use este
# string para guiar as substituicoes

'''
Decompondo

pegar o entrada
verificar se existe letra maiuscula ou minuscula
    Percorrer o input
    pular o alfabeto de acordo com o tamanho da letra
        se for minusculo, 
            leia o alfabeto_minusculo
            preciso saber por onde comecar.. 
            pule o numero de chave
        se for maiusculo, 
            leia e alfabeto_maiusculo 
            pule o numerod e chave
        se nao for nenhum do dois, nao faca nada

'''

# entrada = "Olá mundo!"
entrada = "Zelda"
chave = 2
alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
resultado = []

for letra in entrada:
    position = 0
    if letra in alfabeto_minusculo:
        position = alfabeto_minusculo.index(letra) + chave
        resultado += alfabeto_minusculo[position]
    elif letra in alfabeto_maiusculo:
        position = alfabeto_maiusculo.index(letra) + chave
        resultado += alfabeto_maiusculo[position]
    else:
        resultado += letra

resultado = "".join(resultado)

print(resultado)
