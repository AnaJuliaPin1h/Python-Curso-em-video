# ============================================================
# ESTRUTURAS DE REPETIÇÃO EM PYTHON - GUIA COMENTADO E SIMPLES
# ============================================================

# Estruturas de repetição (loops) servem para executar
# um mesmo bloco de código várias vezes, sem precisar
# escrever o mesmo código repetidamente.

# Existem dois tipos principais em Python:

# while -> repete enquanto uma condição for verdadeira.
# for -> percorre elementos de uma sequência.

# Variáveis muito usadas em loops:

# Contador:
# conta quantas vezes algo aconteceu.
# Exemplo: quantidade de tentativas.

# Acumulador:
# guarda uma soma ou total.
# Exemplo: soma de vários números digitados.


# ============================================================
# 1) WHILE
# ============================================================

# O while verifica a condição antes de executar.

# Pense assim:

# "Enquanto a condição for verdadeira,
# continue repetindo."

# Exemplo:
#
# i = 1
#
# while i < 6:
#     print(i)
#     i += 1

# Funcionamento:

# i = 1 → imprime 1
# i = 2 → imprime 2
# i = 3 → imprime 3
# i = 4 → imprime 4
# i = 5 → imprime 5

# Quando i vira 6:

# i < 6 → falso

# O laço termina.


# ============================================================
# IMPORTÂNCIA DO i += 1
# ============================================================

# i += 1 significa:

# i = i + 1

# Serve para atualizar a variável de controle.

# Se esquecermos disso:

# i = 1
#
# while i < 6:
#     print(i)

# i continuará valendo 1 para sempre.

# Resultado:
# loop infinito.


# ============================================================
# WHILE NOT
# ============================================================

# while not inverte a condição.

# Exemplo:

# contador = 0
#
# while not (contador >= 5):

# é equivalente a:

# while contador < 5

# O laço continuará até contador chegar em 5.


# ============================================================
# CONTADOR
# ============================================================

# Um contador registra quantas vezes algo ocorreu.

# Exemplo:

# tentativas = 0

# tentativas += 1

# Cada repetição aumenta o contador em 1.


# ============================================================
# BREAK
# ============================================================

# break interrompe o laço imediatamente.

# Exemplo:

# while tentativas < 3:
#
#     if senha == senha_correta:
#         break

# Assim que encontrar a senha correta,
# o laço é encerrado.


# ============================================================
# ELSE NO WHILE
# ============================================================

# O else executa apenas se NÃO houver break.

# Exemplo:

# while tentativas < 3:
#     ...
#
# else:
#     print("Conta bloqueada")

# O else só será executado se todas as tentativas
# terminarem normalmente.


# ============================================================
# WHILE TRUE
# ============================================================

# while True cria um laço infinito.

# Exemplo:

# while True:
#     senha = input()

# Como True é sempre verdadeiro,
# o programa nunca termina sozinho.

# A única forma de sair é usando break.


# ============================================================
# LAÇO INTERATIVO
# ============================================================

# Um laço interativo é aquele em que o usuário
# decide quando parar.

# Exemplo:

# while True:
#
#     if resposta == "sair":
#         break

# O programa continuará até o usuário escolher sair.


# ============================================================
# ACUMULADOR
# ============================================================

# Um acumulador guarda um total.

# Exemplo:

# soma_total = 0

# soma_total += valor

# Significa:

# soma_total = soma_total + valor

# Exemplo:

# soma_total = 0
# valor = 10

# soma_total += valor

# Resultado:

# soma_total = 10


# ============================================================
# SENTINELA
# ============================================================

# Sentinela é uma variável que controla
# se o laço continua ou termina.

# Exemplo:

# resposta = "S"

# while resposta == "S":
#     ...
#     resposta = input("Deseja continuar?")

# Se o usuário digitar N,
# o laço termina.


# ============================================================
# OPERADORES DE ATRIBUIÇÃO COMPOSTOS
# ============================================================

# x += 1
# equivale a:
# x = x + 1

# x -= 1
# equivale a:
# x = x - 1

# x *= 2
# equivale a:
# x = x * 2

# x /= 2
# equivale a:
# x = x / 2

# x **= 2
# equivale a:
# x = x ** 2

# x //= 2
# equivale a:
# x = x // 2

# Esses operadores são muito usados em loops.


# ============================================================
# FOR
# ============================================================

# O for percorre uma sequência automaticamente.

# Pense assim:

# "Para cada elemento da sequência,
# faça alguma coisa."

# Pode percorrer:

# listas
# strings
# tuplas
# conjuntos
# dicionários
# range()


# ============================================================
# FOR EM LISTAS
# ============================================================

# frutas = ["maçã", "banana", "cereja"]
#
# for fruta in frutas:
#     print(fruta)

# Saída:

# maçã
# banana
# cereja


# ============================================================
# FOR EM STRINGS
# ============================================================

# for letra in "banana":
#     print(letra)

# O Python pega uma letra por vez.

# Saída:

# b
# a
# n
# a
# n
# a


# ============================================================
# CONTINUE
# ============================================================

# continue não encerra o laço.

# Ele apenas pula a repetição atual.

# Exemplo:

# for fruta in frutas:
#
#     if fruta == "banana":
#         continue
#
#     print(fruta)

# Saída:

# maçã
# cereja


# ============================================================
# RANGE()
# ============================================================

# range() gera números.

# range(6)

# gera:

# 0, 1, 2, 3, 4, 5

# O último número NÃO é incluído.


# ============================================================
# RANGE(INÍCIO, FIM)
# ============================================================

# range(2, 6)

# gera:

# 2, 3, 4, 5

# O 6 não entra.


# ============================================================
# RANGE(INÍCIO, FIM, PASSO)
# ============================================================

# range(2, 30, 3)

# gera:

# 2, 5, 8, 11, 14, ...


# ============================================================
# ELSE NO FOR
# ============================================================

# O else do for só executa se não houver break.

# Exemplo:

# for x in range(5):
#     print(x)
#
# else:
#     print("Fim")

# Como não houve break,
# o else será executado.


# ============================================================
# LOOPS ANINHADOS
# ============================================================

# Loop aninhado é um loop dentro de outro.

# Exemplo:

# for cor in cores:
#
#     for fruta in frutas:
#         print(cor, fruta)

# O loop interno executa completamente
# para cada repetição do loop externo.


# ============================================================
# PASS
# ============================================================

# pass não faz nada.

# Serve apenas para deixar um bloco vazio sem gerar erro.

# Exemplo:

# for x in range(3):
#     pass

# O programa não faz nada,
# mas também não gera erro.


# ============================================================
# MENU COM while True
# ============================================================

# while True:
#
#     opcao = input()
#
#     if opcao == "4":
#         break

# O programa continuará mostrando o menu
# até que o usuário escolha sair.


# ============================================================
# RESUMO FINAL
# ============================================================

# while
# repete enquanto uma condição for verdadeira.

# for
# percorre elementos de uma sequência.

# break
# interrompe o laço imediatamente.

# continue
# pula apenas a repetição atual.

# else
# executa somente se não houver break.

# contador
# conta quantas vezes algo aconteceu.

# acumulador
# guarda uma soma ou total.

# sentinela
# controla quando o laço termina.

# range()
# gera sequências numéricas.

# pass
# não faz nada.

# while True
# cria um laço infinito.

# FRASES MAIS IMPORTANTES:

# WHILE:
# "Enquanto a condição for verdadeira, continue repetindo."

# FOR:
# "Para cada elemento da sequência, faça alguma coisa."