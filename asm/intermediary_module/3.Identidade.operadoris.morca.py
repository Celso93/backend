# Identidade e o operador is
# O operador == verifica se os valores são iguais e o is verifica se os objetos têm a mesma identidade (mesma referência na memória)

bolo1 = {
    'sabo': 'chocolate',
    'tamanho': 'grande',
    'preço': 50,
}

bolo2 = {
    'sabo': 'chocolate',
    'tamanho': 'grande',
    'preço': 50,
}

# tem o mesmos elementos, porém são objetos diferentes
print(bolo1 is bolo2)

# caso de uso em objetos python
True is True # true
None is None # true
False is False # true
True is False # False

# outro exemplo
valor = 10

if valor is None:
  print('Valor retornado é nulo')
else:
  print('continue oque voce estava fazendo!')



########################################################################
# operador morsa :=
# Expressao de atribuicao
# Não é muito utilizado, e particulamente acho confuso
# é atribuir um valor a uma variável como parte de uma expressão.
n = 5
while n > 0:
  n -= 1
  print(n)

# com operador morsa
n = 5
while (n := n-1) > 0:
  print(n)