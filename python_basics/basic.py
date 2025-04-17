"""
Python Fundamentos - Guia de Referência
=====================================

1. Variáveis e Objetos
-------------------
# Em Python, variáveis são referências para objetos em memória
# Não são "caixas" que contêm valores, mas sim "etiquetas" que apontam para objetos

# Tudo em Python é objeto
# Cada objeto tem:
# - Tipo (type)
# - Valor
# - Métodos e atributos

# Para explorar objetos:
dir(objeto)   # Lista todos os métodos e atributos
help(objeto)  # Mostra a documentação
type(objeto)  # Mostra o tipo do objeto

2. Tipos Numéricos
---------------
# Inteiros (int)
num_decimal = 42        # Base 10
num_binario = 0b101    # Base 2  (começa com 0b)
num_octal = 0o127      # Base 8  (começa com 0o)
num_hexa = 0xFF        # Base 16 (começa com 0x)

# Ponto Flutuante (float)
pi = 3.14159
velocidade = 2.5e8     # Notação científica (2.5 x 10^8)

# Operações
soma = 5 + 3           # Adição
sub = 5 - 3           # Subtração
mult = 5 * 3          # Multiplicação
div = 5 / 3           # Divisão (resultado float)
div_inteira = 5 // 3  # Divisão inteira
resto = 5 % 3         # Resto da divisão
potencia = 5 ** 3     # Potenciação

3. Booleanos e Comparações
----------------------
# Valores booleanos
verdadeiro = True
falso = False
nulo = None  # Representa ausência de valor

# Operadores de comparação
igual = x == y            # Igualdade
diferente = x != y        # Diferença
maior = x > y             # Maior que
maior_igual = x >= y      # Maior ou igual
menor = x < y             # Menor que
menor_igual = x <= y      # Menor ou igual

# Operadores lógicos
and_logico = True and False  # E lógico
or_logico = True or False    # OU lógico
not_logico = not True        # NÃO lógico

# Valores que Python considera False:
# - False
# - None
# - 0 (zero)
# - "" (string vazia)
# - [] (lista vazia)
# - {} (dicionário vazio)
# - set() (conjunto vazio)
# - () (tupla vazia)

4. Estruturas de Controle
----------------------
# if/elif/else
idade = 18
if idade >= 18:
    print("Maior de idade")
elif idade >= 16:
    print("Pode votar, não pode dirigir")
else:
    print("Menor de idade")

# Operador ternário
status = "Maior" if idade >= 18 else "Menor"

# Loops
## while - executa enquanto condição for verdadeira
contador = 0
while contador < 5:
    print(contador)
    contador += 1

## for - itera sobre sequência
for i in range(5):           # range gera sequência de números
    print(i)

for letra in "Python":       # itera sobre string
    print(letra)

# Controle de loops
# break    - sai do loop
# continue - pula para próxima iteração
# else     - executa quando loop termina normalmente

5. Strings
--------
# Formas de criar strings
aspas_simples = 'Python'
aspas_duplas = "Python"
multiplas_linhas = '''
    Texto em
    múltiplas linhas
'''

# Formatação
nome = "Maria"
idade = 25
# f-strings (Python 3.6+)
print(f"{nome} tem {idade} anos")
# .format()
print("{} tem {} anos".format(nome, idade))

# Métodos úteis
texto = "  Python  "
print(texto.upper())        # Maiúsculas
print(texto.lower())        # Minúsculas
print(texto.strip())        # Remove espaços
print(texto.split())        # Divide em lista
print(texto.replace('y', 'i'))  # Substitui caracteres
print('y' in texto)        # Verifica se contém

# Indexação e fatiamento
texto = "Python"
print(texto[0])     # Primeiro caractere
print(texto[-1])    # Último caractere
print(texto[1:4])   # Caracteres do índice 1 ao 3
print(texto[::2])   # Caracteres alternados
print(texto[::-1])  # String invertida

6. Listas
-------
# Lista é uma sequência mutável de elementos
numeros = [1, 2, 3, 4, 5]
mista = [1, "texto", True, 3.14]

# Operações básicas
print(len(numeros))         # Tamanho
print(numeros[0])          # Acesso por índice
print(2 in numeros)        # Verificação de elemento
print(numeros + [6, 7])    # Concatenação

# Fatiamento [início:fim:passo]
print(numeros[1:4])    # [2, 3, 4]
print(numeros[::2])    # [1, 3, 5]
print(numeros[::-1])   # [5, 4, 3, 2, 1]

# Métodos principais
numeros.append(6)      # Adiciona ao final
numeros.insert(0, 0)   # Insere na posição
numeros.pop()          # Remove e retorna último elemento
numeros.remove(3)      # Remove primeira ocorrência
numeros.sort()         # Ordena a lista
numeros.reverse()      # Inverte a lista
numeros.clear()        # Remove todos elementos

# List Comprehension
quadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Matrizes (listas de listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[1][1])  # Acessa elemento 5

7. Funções
--------
# Definição básica
def saudacao(nome):
    """Retorna uma saudação personalizada."""
    return f"Olá, {nome}!"

# Parâmetros default
def cadastro(nome, idade=18, cidade="São Paulo"):
    return f"{nome}, {idade} anos, {cidade}"

# Args e Kwargs
def exemplo(*args, **kwargs):
    """
    args: tupla com argumentos posicionais
    kwargs: dicionário com argumentos nomeados
    """
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

# Exemplo de uso
exemplo(1, 2, 3, nome="João", idade=25)

# Funções anônimas (lambda)
dobro = lambda x: x * 2
print(dobro(5))  # 10

8. Tuplas
-------
# Tupla é uma sequência imutável
coordenadas = (10, 20)
pessoa = ('João', 25, 'São Paulo')

# Desempacotamento
x, y = coordenadas
nome, idade, cidade = pessoa

# Métodos
print(coordenadas.count(10))  # Conta ocorrências
print(coordenadas.index(20))  # Encontra posição

# Vantagens das tuplas:
# - Imutáveis (mais seguras)
# - Mais eficientes em memória
# - Podem ser chaves de dicionários
# - Garantem integridade dos dados

9. Conjuntos (Sets)
----------------
# Set é uma coleção não ordenada de elementos únicos
frutas = {'maçã', 'banana', 'laranja'}
numeros = {1, 2, 3, 4, 5}

# Operações de conjuntos
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

uniao = a.union(b)                # {1, 2, 3, 4, 5, 6}
intersecao = a.intersection(b)    # {3, 4}
diferenca = a.difference(b)       # {1, 2}
dif_simetrica = a.symmetric_difference(b)  # {1, 2, 5, 6}

# Métodos
frutas.add('uva')          # Adiciona elemento
frutas.remove('banana')    # Remove elemento (erro se não existe)
frutas.discard('pera')    # Remove elemento (sem erro)

# Características importantes:
# - Elementos devem ser imutáveis
# - Não permite duplicatas
# - Ótimo para remover duplicatas de sequências
# - Eficiente para operações matemáticas de conjuntos

10. Dicionários
------------
# Dicionários são estruturas de dados que permitem armazenar pares de chave-valor
# Características principais:
# - Cada elemento tem uma chave única e um valor associado
# - Acesso rápido aos valores através das chaves (O(1))
# - Chaves devem ser imutáveis (strings, números, tuplas)
# - Valores podem ser de qualquer tipo (inclusive outros dicionários)
# - Mantém ordem de inserção (a partir do Python 3.7)
# - Muito usados para representar dados estruturados

# Exemplo completo
pessoa = {
    'nome': 'Pedro', 
    'idade': 27,
    'linguagens': ['Python', 'JavaScript', 'Java'],  # Lista como valor
    'ativo': True,                                   # Booleano como valor
    'endereco': {                                    # Dicionário aninhado
        'rua': 'Rua Principal',
        'numero': 123,
        'cidade': 'São Paulo'
    },
    'notas': (9.5, 8.7, 9.0),                       # Tupla como valor
    'cursos': {                                      # Conjunto como valor
        'Python Básico',
        'Web Development',
        'Data Science'
    }
}

# Operações comuns
# 1. Acessar valores
print(pessoa['nome'])           # Acesso direto
print(pessoa.get('idade', 0))   # Acesso seguro com valor default

# 2. Modificar/Adicionar valores
pessoa['idade'] = 28            # Modifica valor existente
pessoa['telefone'] = '123456'   # Adiciona novo par

# 3. Remover valores
valor = pessoa.pop('telefone')  # Remove e retorna valor
del pessoa['idade']             # Remove par chave-valor

# 4. Iterar sobre dicionário
for chave in pessoa:           # Itera sobre chaves
    print(chave)

for chave, valor in pessoa.items():  # Itera sobre pares
    print(f"{chave}: {valor}")

# 5. Métodos úteis
print(pessoa.keys())    # Lista de chaves
print(pessoa.values())  # Lista de valores
print(pessoa.items())   # Lista de tuplas (chave, valor)

# Dicionários vs JSON
# - Dicionários são estruturas de dados do Python
# - JSON é um formato de texto para transferência de dados
import json

# Dict para JSON (serialização)
texto_json = json.dumps(pessoa)

# JSON para Dict (desserialização)
dict_novo = json.loads(texto_json)

# Diferenças importantes:
# - Dict: usa True, False, None
# - JSON: usa true, false, null
# - Dict: aceita qualquer objeto imutável como chave
# - JSON: só aceita strings como chave
# - Dict: suporta mais tipos de dados (tuplas, sets, etc.)
# - JSON: suporta apenas strings, números, arrays, objetos, true, false, null
"""
