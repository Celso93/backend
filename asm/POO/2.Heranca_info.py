'''
[Heranca]
Class herdada (filho) de outra Class (pai)
'''

class Animal:
  def __init__(self):
    print("Animal criado")

  def quem_sou_eu(self):
    print("eu sou um animal")


class Gato(Animal):
  def __init__(self):
    Animal.__init__(self) # chamando os atributos do pai
    print("adicionando mais atributo ao filho")

  # metodo sobreescrito
  def quem_sou_eu(self):
    print("eu sou um Gato")

exemplo1 = Animal()
exemplo2 = Gato()

exemplo1.quem_sou_eu()
exemplo2.quem_sou_eu()

# Outros metodos especiais
# __str__ : é oque vai sair no print
# __len__ : tamanho da class
# __del__ : deleta o objeto