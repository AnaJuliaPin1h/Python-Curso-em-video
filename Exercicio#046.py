# ==========================================================
# LAÇO DE REPETIÇÃO FOR
# Contagem regressiva
# ==========================================================

# O comando for é usado quando sabemos
# quantas vezes um bloco de código deve ser repetido.

# Sintaxe:

# for variável in range():
#     código

# ==========================================================
# O QUE SIGNIFICA CADA PARTE?
# ==========================================================

# for
# Palavra-chave que inicia um laço de repetição.

# cont
# Variável de controle (contador).
# Ela recebe um novo valor a cada repetição.

# in
# Significa "em" ou "dentro de".
# Indica que a variável irá percorrer
# todos os valores gerados pelo range().

# range()
# Função que gera uma sequência de números.

# ==========================================================
# RANGE COM 2 PARÂMETROS
# ==========================================================

# range(início, fim)

# início -> primeiro número da sequência.
# fim    -> valor limite (não é incluído).

# Exemplo:

for cont in range(0, 11):
    print(cont)

print("ACABOU!!!")

# Explicação:
#
# range(0, 11)
#
# começa em 0
# termina antes do 11
#
# Resultado:
#
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# ==========================================================
# OUTRO EXEMPLO
# ==========================================================

for cont in range(1, 10):
    print(cont)

print("ACABOU!!!")

# Explicação:
#
# range(1, 10)
#
# começa em 1
# termina antes do 10
#
# Resultado:
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# ==========================================================
# RANGE COM 3 PARÂMETROS
# ==========================================================

# range(início, fim, passo)

# início -> onde começa.
# fim    -> onde termina (não inclui).
# passo  -> de quanto em quanto vai contar.

# ==========================================================
# CONTAGEM REGRESSIVA
# ==========================================================

for cont in range(10, -1, -1):
    print(cont)

print("ACABOU!!!")

# Explicação:
#
# range(10, -1, -1)
#
# começa em 10
# termina antes do -1
# diminui 1 a cada repetição
#
# Resultado:
#
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

# ==========================================================
# EXEMPLO DE PASSO DIFERENTE
# ==========================================================

for cont in range(0, 11, 2):
    print(cont)

# Explicação:
#
# começa em 0
# termina antes do 11
# aumenta de 2 em 2
#
# Resultado:
#
# 0
# 2
# 4
# 6
# 8
# 10

# ==========================================================
# RESUMO
# ==========================================================

# for
# Cria um laço de repetição.

# in
# Faz a variável percorrer os valores.

# range()
# Gera uma sequência de números.

# range(fim)
# Conta de 0 até fim - 1.

# range(início, fim)
# Conta do início até fim - 1.

# range(início, fim, passo)
# Conta usando o passo definido.

# Passo positivo:
# Conta para frente.

# Passo negativo:
# Conta para trás.