# ============================================================
# WHILE EM PYTHON - GUIA COMENTADO E SIMPLES
# ============================================================

# O while é uma estrutura de repetição.
# Ele executa um bloco de código ENQUANTO uma condição
# for verdadeira.

# Pense assim:
#
# "Enquanto isso for verdadeiro, continue repetindo."

# Exemplo:
# enquanto i < 6:
#     continue repetindo


# ============================================================
# 1) WHILE BÁSICO
# ============================================================

# Antes do while, normalmente criamos uma variável de controle.

# Exemplo:
# i = 1
#
# while i < 6:
#     print(i)
#     i += 1

# O que acontece?

# i começa valendo 1.

# 1ª repetição:
# i = 1 → imprime 1 → soma 1 → i vira 2

# 2ª repetição:
# i = 2 → imprime 2 → i vira 3

# 3ª repetição:
# i = 3 → imprime 3 → i vira 4

# 4ª repetição:
# i = 4 → imprime 4 → i vira 5

# 5ª repetição:
# i = 5 → imprime 5 → i vira 6

# Agora a condição i < 6 é falsa.
# O laço termina.

# Saída:
# 1
# 2
# 3
# 4
# 5


# ============================================================
# IMPORTÂNCIA DO i += 1
# ============================================================

# O incremento é muito importante.

# Exemplo:
# i += 1

# Isso significa:
# pegue o valor atual de i e some 1.

# Se esquecermos disso:

# i = 1
#
# while i < 6:
#     print(i)

# i continuará valendo 1 para sempre.

# Resultado:
# loop infinito.

# Regra:
# while precisa alterar a variável de controle,
# caso contrário o programa pode nunca terminar.


# ============================================================
# 2) BREAK
# ============================================================

# break interrompe o laço imediatamente.

# Exemplo:
# i = 1
#
# while i < 6:
#     print(i)
#
#     if i == 3:
#         break
#
#     i += 1

# O que acontece?

# i = 1 → imprime 1
# i = 2 → imprime 2
# i = 3 → imprime 3
# encontra o break
# o laço é encerrado

# Saída:
# 1
# 2
# 3

# Regra:
# break = parar o laço imediatamente.


# ============================================================
# 3) CONTINUE
# ============================================================

# continue não encerra o laço.
# Ele apenas pula a repetição atual.

# Exemplo:
# i = 0
#
# while i < 6:
#     i += 1
#
#     if i == 3:
#         continue
#
#     print(i)

# O que acontece?

# i = 1 → imprime 1
# i = 2 → imprime 2
# i = 3 → encontra continue → não imprime
# i = 4 → imprime 4
# i = 5 → imprime 5
# i = 6 → imprime 6

# Saída:
# 1
# 2
# 4
# 5
# 6

# Regra:
# continue = pula apenas a volta atual.


# ============================================================
# 4) ELSE NO WHILE
# ============================================================

# O else executa quando o while termina normalmente.

# Exemplo:
# i = 1
#
# while i < 6:
#     print(i)
#     i += 1
#
# else:
#     print("Fim")

# Saída:
# 1
# 2
# 3
# 4
# 5
# Fim

# O else executou porque o while terminou
# naturalmente.


# ============================================================
# ELSE COM BREAK
# ============================================================

# Exemplo:
# i = 1
#
# while i < 6:
#
#     if i == 3:
#         break
#
#     print(i)
#     i += 1
#
# else:
#     print("Fim")

# Saída:
# 1
# 2

# O else NÃO executa.

# Regra:
# else do while só funciona se NÃO houver break.


# ============================================================
# BREAK x CONTINUE
# ============================================================

# break
# interrompe completamente o laço.

# continue
# pula apenas a repetição atual.

# Exemplo:

# break:
# 1
# 2
# 3
# para tudo.

# continue:
# 1
# 2
# pula 3
# continua com 4, 5 e 6.




# EXEMPLO COMPLETO


# i = 0
#
# while i < 6:
#
#     i += 1
#
#     if i == 3:
#         continue
#
#     print(i)

# Passo a passo:

# i começa em 0

# 1ª volta:
# i vira 1 → imprime 1

# 2ª volta:
# i vira 2 → imprime 2

# 3ª volta:
# i vira 3 → continue → não imprime

# 4ª volta:
# i vira 4 → imprime 4

# 5ª volta:
# i vira 5 → imprime 5

# 6ª volta:
# i vira 6 → imprime 6

# Agora i < 6 é falso.
# O laço termina.

# Saída:
# 1
# 2
# 4
# 5
# 6


# ============================================================
# RESUMO FINAL
# ============================================================

# while condição:
# repete enquanto a condição for verdadeira.

# i += 1
# altera a variável de controle.

# break
# interrompe o laço imediatamente.

# continue
# pula apenas a repetição atual.

# else no while
# executa somente se não houver break.

# loop infinito
# acontece quando a condição nunca se torna falsa.

# FRASE MAIS IMPORTANTE PARA MEMORIZAR:
#
# "Enquanto a condição for verdadeira, continue repetindo."
#
# Essa é a ideia principal do while em Python.