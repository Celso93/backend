# --- Compreensão de Lista, Conjunto e Dicionário ---

# ===================================================================
# 1. Compreensão de Lista (List Comprehension)
# ===================================================================

# Lista base para os exemplos: [0, 1, 2, ..., 10]
ex_lista = list(range(0, 11))

# Forma tradicional com loop `for` para filtrar a lista
ex1_result = []
for numero in ex_lista:
    if numero > 6:
        ex1_result.append(numero)
print(f"1. Resultado com for loop:         {ex1_result}")

# Forma "Pythônica" com List Comprehension (apenas filtrando)
# Sintaxe: [expressao for item in lista if condicao]
ex2_result = [
    numero
    for numero in ex_lista
    if numero > 6
]
print(f"2. Com list comprehension:         {ex2_result}")

# List Comprehension que transforma os itens enquanto filtra
def multiple_by(numero, multiplicador):
    return numero * multiplicador

ex3_result = [
    multiple_by(numero, 2)
    for numero in ex_lista
    if numero > 6
]
print(f"3. Com list comprehension e função: {ex3_result}")


# ===================================================================
# 2. Compreensão de Conjunto (Set Comprehension)
# ===================================================================

ex_lista_para_conjunto = list(range(5)) # Exemplo: [0, 1, 2, 3, 4]

# A sintaxe é quase idêntica à de lista, mas com chaves {}.
# O resultado é um 'set', que não contém elementos duplicados e é desordenado.
ex_conjunto_compreensao = {
    posicao
    for posicao in ex_lista_para_conjunto
    if posicao < 4
}
print(f"\n4. Compreensão de conjunto:        {ex_conjunto_compreensao}")


# ===================================================================
# 3. Compreensão de Dicionário (Dictionary Comprehension)
# ===================================================================

valores_em_reais_feira = {
    'Tomate': 5.00,
    'Pepino': 6.00,
    'Cenoura': 3.00
}
fator_conversao_ienes = 26.65

# A sintaxe define uma 'chave: valor' para cada item do loop.
# O método .items() é usado para percorrer as chaves e os valores do dicionário original.
valores_em_ienes_feira = {
    produto: preco * fator_conversao_ienes
    for produto, preco in valores_em_reais_feira.items()
}
print(f"5. Compreensão de dicionário:      {valores_em_ienes_feira}")