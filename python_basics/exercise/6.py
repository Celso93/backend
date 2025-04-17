'''
Faca um programa que pergunte o preco de tres produtos
e informe qual produto voce deve comprar, sabendo que a 
decisao e sempre pelo mais barato
'''

produto_1 = float(input('Informe o preco do produto 1: '))
produto_2 = float(input('Informe o preco do produto 2: '))
produto_3 = float(input('Informe o preco do produto 3: '))

if produto_1 > produto_2 and produto_2 < produto_3:
    print(f'Voce selecionou o produto 2 com preco {produto_2}')
elif produto_2 > produto_3 and produto_3 < produto_2:
    print(f'Voce selecionou o produto 3 com preco {produto_3}')
elif produto_1 < produto_2 and produto_1 < produto_3:
    print(f'Voce selecionou o produto 1 com preco {produto_1}')
else:
    print('Produtos possuem preco iguais')
