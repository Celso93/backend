'''
Programação orientada a objetos
E um Paradigma da programação.

Classes
- Forma de programar para CRIAR um novo tipo de dado
- Class tem Atributos e Ações (métodos).

Objeto é uma derivacao de uma Classe.
'''

class Exemplo:
  # metodos especiais
  # __init__ funcao de inicializacao
  # self : forma do python acessar os proprios elementos
  def __init__(self, parametro):
    self.exemplo_de_variavel = 'hellow'
    self.outro_exemplo_variavel = 20
    self.exemplo_parametro = parametro

  def say_hello(self):
    print(self.exemplo_de_variavel)

# instancia = objeto, criar uma variavel que recebe a classe
x = Exemplo('exemplo de parametro')
x.say_hello()
x.outro_exemplo_variavel
x.exemplo_parametro