##########################################
# Operadores de Comparação
##########################################

# Operadores de comparação comparam dois valores
# e sempre retornam True (verdadeiro) ou False (falso).


x = 5
y = 3


# ============================================================
# == (igual a)
# ============================================================

# Verifica se os dois valores são IGUAIS.
# Atenção: == é comparação, = é atribuição (guardar valor).

print(x == y)   # False → 5 não é igual a 3


# ============================================================
# != (diferente de)
# ============================================================

# Verifica se os dois valores são DIFERENTES.

print(x != y)   # True → 5 é diferente de 3


# ============================================================
# > (maior que)
# ============================================================

# Verifica se o valor da esquerda é MAIOR que o da direita.

print(x > y)    # True → 5 é maior que 3


# ============================================================
# < (menor que)
# ============================================================

# Verifica se o valor da esquerda é MENOR que o da direita.

print(x < y)    # False → 5 não é menor que 3


# ============================================================
# >= (maior ou igual a)
# ============================================================

# Verifica se o valor da esquerda é MAIOR OU IGUAL ao da direita.

print(x >= y)   # True → 5 é maior ou igual a 3

x = 3
print(x >= y)   # True → 3 é igual a 3, então também é verdadeiro


# ============================================================
# <= (menor ou igual a)
# ============================================================

# Verifica se o valor da esquerda é MENOR OU IGUAL ao da direita.

x = 5
print(x <= y)   # False → 5 não é menor nem igual a 3

x = 3
print(x <= y)   # True → 3 é igual a 3, então é verdadeiro


# ============================================================
# ENCADEAMENTO — comparar mais de uma coisa na mesma linha
# ============================================================

# Python permite verificar duas condições de uma vez.
# As duas formas abaixo fazem a mesma coisa:

x = 5

print(1 < x < 10)          # True → 5 está entre 1 e 10
print(1 < x and x < 10)    # True → mesma verificação, escrita separada

# Lê assim: "x é maior que 1 E menor que 10?"
# Se as duas forem verdadeiras → True
# Se uma for falsa → False


# ============================================================
# EXERCÍCIO
# ============================================================

# Qual é o resultado de 5 == 5 ?
print(5 == 5)   # True → porque 5 é igual a 5

# Resposta: True
# "Falso" estava errado porque os valores SÃO iguais.
# "5" estava errado porque comparação nunca retorna o número,
# sempre retorna True ou False.