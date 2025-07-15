# o bloco with
# gerenciador de contexto (coloca close() implicitamente)
# as vezes e usado no banco de dados

# exemplo sem
# arquivo = open('texte.txt', 'w')
# arquivo.write('Exemplo de escrita')
# arquivo.close()

# exemplo com with 
# coloca o close() implicitamente
with open('texte.txt', 'w') as arquivo:
    arquivo.write('Exemplo de escrita com with')



# match case 
# semelhante ao switch case do ruby
# python 3.10

exemplo = 1
match exemplo:
    case 1:
        print('Caiu no case 1')
    case 2:
        print('Caiu no case 2')
    case _: # semelhante ao else
        print('Caiu no case 2')

# exemplo avancado
produtos = {
    'Pao': 10,
    'cafe': 30,
    'leite': 8
}

match produtos:
    case {'cafe': 30}:
        print('Cafe ta caro ein')
    case _:
        print('Nada esta caro')

match produtos:
    case {'leite': _}:
        print('leite esta presente na lista, entao execute tal acao')
    case _:
        print('nao faca nada')