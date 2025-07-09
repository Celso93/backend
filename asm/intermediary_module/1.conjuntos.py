# Conjuntos
# o uso e mais ninchado
a = {1, 2, 3, 4}

'''
Observacoes:
- Parece dicionario mas nao possui chave
- Numeros dentro de um conjunto nao se repetem
- Conjunto nao tem ordenacao, portanto exemplo[0] nao funciona
- Elementos nao sao mutaveis, somente elementos unicos
- Nao pode conter uma lista
- type(a) = set

%timeit = quanto tempo demora pra executar um script
    
Exemplo de utilidade:
1 - UTIL para filtar valores unicos de uma lista
2 - Ramo da matematica
3 - Exemlo de aluno: Verificar se todos os elementos de uma lista estão em outra lista
'''

# exemlo 1
ex1 = [1, 1, 2, 3, 3, 4 ,5]
ex1_transformando_em_conjunto = set(ex1) # {1, 2, 3, 4, 5}, elementos nao se repetem
ex1_retornando_para_lista = list(ex1_transformando_em_conjunto)

# exemlo 2
ex2_conjunto1 = set(list(range(0,100)))
ex2_conjunto2 = set([42, 88, 71, 23, 9, 64, 5, 77, 95, 30, 14, 101])

# 1. União (A ∪ B)
# Como o conjunto2 está contido no conjunto1, a união é o próprio conjunto1.
uniao = ex2_conjunto1.union(ex2_conjunto2)
# Alternativa: uniao = ex2_conjunto1 | ex2_conjunto2


# 2. Interseção (A ∩ B)
# Como todos os elementos do conjunto2 também estão no conjunto1, a interseção é o próprio conjunto2.
intersecao = ex2_conjunto1.intersection(ex2_conjunto2)
# Alternativa: intersecao = ex2_conjunto1 & ex2_conjunto2

# 3. Diferença (A ∖ B)
# Elementos que estão em um conjunto, mas não no outro. A ordem importa!
diferenca_1_2 = ex2_conjunto1.difference(ex2_conjunto2)
# Alternativa: diferenca_1_2 = ex2_conjunto1 - ex2_conjunto2


diferenca_2_1 = ex2_conjunto2.difference(ex2_conjunto1)
# Alternativa: diferenca_2_1 = ex2_conjunto2 - ex2_conjunto1

# 4. Diferença Simétrica (A Δ B)
# Elementos que estão em um ou no outro, mas não em ambos.
simetrica = ex2_conjunto1.symmetric_difference(ex2_conjunto2)
# Alternativa: simetrica = ex2_conjunto1 ^ ex2_conjunto2

# 5. É Subconjunto? (A ⊆ B)
# Verifica se um conjunto está totalmente contido em outro.
subset_2_em_1 = ex2_conjunto2.issubset(ex2_conjunto1)
# Alternativa: subset_2_em_1 = ex2_conjunto2 <= ex2_conjunto1

subset_1_em_2 = ex2_conjunto1.issubset(ex2_conjunto2)
# Alternativa: subset_1_em_2 = ex2_conjunto1 <= ex2_conjunto2

# 6. É Superconjunto? (A ⊇ B)
# Verifica se um conjunto contém todos os elementos de outro.
superset_1_de_2 = ex2_conjunto1.issuperset(ex2_conjunto2)
# Alternativa: superset_1_de_2 = ex2_conjunto1 >= ex2_conjunto2


# exemlo 3
ex3_lista1 = list(range(0,100))
ex3_lista2 = [42, 88, 71, 23, 9, 64, 5, 77, 95, 30, 14, 50, 81, 29, 60, 1, 99, 45, 73, 22, 8, 56, 38, 91, 19, 67, 34, 85, 12, 49]

ex3_conjunto1 = set(ex3_lista1)
ex3_conjunto2 = set(ex3_lista2)

ex3_resultado = ex3_conjunto2.issubset(ex3_conjunto1)
# ex3_retorna_lista = list(ex3_resultado)
