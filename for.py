# ============================================================
# FOR EM PYTHON - GUIA COMENTADO E SIMPLES
# ============================================================

# O for é uma estrutura de repetição.
# Ele é usado para percorrer os elementos de uma sequência.
#
# Pense assim:
# "Para cada elemento da sequência, faça alguma coisa."
#
# O for pode percorrer:
# - listas
# - strings
# - tuplas
# - conjuntos (set)
# - dicionários
# - range()


# ============================================================
# 1) FOR PERCORRENDO UMA LISTA
# ============================================================

# Exemplo:
# frutas = ["apple", "banana", "cherry"]
#
# for fruta in frutas:
#     print(fruta)

# O que acontece?
# 1ª volta → fruta = "apple"
# 2ª volta → fruta = "banana"
# 3ª volta → fruta = "cherry"

# Saída:
# apple
# banana
# cherry


# ============================================================
# 2) FOR PERCORRENDO UMA STRING
# ============================================================

# Exemplo:
# for letra in "banana":
#     print(letra)

# Strings também são sequências.
# O Python pega uma letra por vez.

# 1ª volta → b
# 2ª volta → a
# 3ª volta → n
# 4ª volta → a
# 5ª volta → n
# 6ª volta → a

# Saída:
# b
# a
# n
# a
# n
# a


# ============================================================
# 3) BREAK
# ============================================================

# break interrompe o laço imediatamente.

# Exemplo:
# frutas = ["apple", "banana", "cherry"]
#
# for fruta in frutas:
#     print(fruta)
#
#     if fruta == "banana":
#         break

# O que acontece?
# Imprime "apple".
# Imprime "banana".
# Encontra o break.
# O laço é encerrado.

# Saída:
# apple
# banana

# Regra:
# break = parar o laço imediatamente.


# ============================================================
# 4) BREAK ANTES DO PRINT
# ============================================================

# Exemplo:
# for fruta in frutas:
#
#     if fruta == "banana":
#         break
#
#     print(fruta)

# O que acontece?
# Imprime "apple".
# Quando chega em "banana", para antes do print.

# Saída:
# apple


# ============================================================
# 5) CONTINUE
# ============================================================

# continue não encerra o laço.
# Ele apenas pula a volta atual e vai para a próxima.

# Exemplo:
# frutas = ["apple", "banana", "cherry"]
#
# for fruta in frutas:
#
#     if fruta == "banana":
#         continue
#
#     print(fruta)

# O que acontece?
# Imprime "apple".
# Ignora "banana".
# Continua normalmente.
# Imprime "cherry".

# Saída:
# apple
# cherry

# Regra:
# continue = pula somente a repetição atual.


# ============================================================
# 6) RANGE()
# ============================================================

# range() gera uma sequência de números.

# ------------------------------------------------------------
# range(6)
# ------------------------------------------------------------

# Exemplo:
# for x in range(6):
#     print(x)

# O Python gera:
# 0, 1, 2, 3, 4, 5

# O número 6 NÃO é incluído.

# Saída:
# 0
# 1
# 2
# 3
# 4
# 5

# Regra:
# range(6)
# começa em 0
# termina em 5
# o 6 não entra


# ------------------------------------------------------------
# range(início, fim)
# ------------------------------------------------------------

# Exemplo:
# for x in range(2, 6):
#     print(x)

# O Python gera:
# 2, 3, 4, 5

# O número 6 NÃO é incluído.

# Saída:
# 2
# 3
# 4
# 5

# Regra:
# range(2, 6)
# começa em 2
# termina em 5


# ------------------------------------------------------------
# range(início, fim, passo)
# ------------------------------------------------------------

# Exemplo:
# for x in range(2, 30, 3):
#     print(x)

# O Python gera:
# 2, 5, 8, 11, 14, 17, 20, 23, 26, 29

# Regra:
# range(2, 30, 3)
# começa em 2
# vai até antes do 30
# soma 3 em cada repetição


# ============================================================
# 7) ELSE NO FOR
# ============================================================

# O else do for só executa se o laço terminar normalmente.

# Exemplo:
# for x in range(3):
#     print(x)
#
# else:
#     print("Fim")

# Saída:
# 0
# 1
# 2
# Fim

# Como não houve break, o else foi executado.


# ------------------------------------------------------------
# ELSE COM BREAK
# ------------------------------------------------------------

# Exemplo:
# for x in range(5):
#
#     if x == 3:
#         break
#
#     print(x)
#
# else:
#     print("Fim")

# Saída:
# 0
# 1
# 2

# O else NÃO executa.

# Regra:
# else do for só funciona se NÃO houver break.


# ============================================================
# 8) FOR ANINHADO (LOOP DENTRO DE LOOP)
# ============================================================

# Exemplo:
# cores = ["red", "blue"]
# frutas = ["apple", "banana"]
#
# for cor in cores:
#     for fruta in frutas:
#         print(cor, fruta)

# O que acontece?

# Quando cor = "red":
# red apple
# red banana

# Quando cor = "blue":
# blue apple
# blue banana

# Saída:
# red apple
# red banana
# blue apple
# blue banana

# Regra:
# O loop interno executa completamente
# para cada repetição do loop externo.


# ============================================================
# 9) PASS
# ============================================================

# pass não faz nada.
# Ele é usado quando ainda não queremos escrever o código,
# mas precisamos deixar a estrutura pronta.

# Exemplo:
# for x in range(3):
#     pass

# O programa não faz nada e não gera erro.

# Regra:
# pass = "não faça nada por enquanto".


# ============================================================
# RESUMO FINAL
# ============================================================

# for item in sequência
# percorre cada elemento da sequência.

# for letra in "texto"
# percorre cada caractere da string.

# break
# interrompe o laço imediatamente.

# continue
# pula somente a repetição atual.

# range(n)
# gera números de 0 até n-1.

# range(a, b)
# gera números de a até b-1.

# range(a, b, passo)
# soma "passo" em cada repetição.

# else no for
# executa somente se não houver break.

# for dentro de for
# chama-se loop aninhado.

# pass
# não faz nada.

# FRASE MAIS IMPORTANTE PARA MEMORIZAR:
#
# "Para cada elemento da sequência, faça alguma coisa."
#
# Essa é a ideia principal do for em Python.