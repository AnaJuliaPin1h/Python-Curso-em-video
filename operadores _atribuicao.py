# Operadores de Atribuição



# Operadores de atribuição são atalhos para fazer uma operação
# e já guardar o resultado na mesma variável.
# Em vez de escrever x = x + 3, você escreve x += 3.


x = 10
print(x)   # 10


# += (adição)

# x += 3  é o mesmo que  x = x + 3
# pega o valor atual de x, soma 3, e guarda de volta em x

x = 10
x += 3
print(x)   # 13


# -= (subtração)

# x -= 3  é o mesmo que  x = x - 3
# pega o valor atual de x, subtrai 3, e guarda de volta em x

x = 10
x -= 3
print(x)   # 7


# *= (multiplicação)


# x *= 3  é o mesmo que  x = x * 3
# pega o valor atual de x, multiplica por 3, e guarda de volta em x

x = 10
x *= 3
print(x)   # 30


# /= (divisão)

# x /= 3  é o mesmo que  x = x / 3
# pega o valor atual de x, divide por 3, e guarda de volta em x

x = 10
x /= 2
print(x)   # 5.0  → divisão sempre retorna número com decimal


# %= (resto da divisão)

# x %= 3  é o mesmo que  x = x % 3
# pega o valor atual de x, divide por 3, e guarda só o RESTO

x = 10
x %= 3
print(x)   # 1  → 10 dividido por 3 = 3 com resto 1


# //= (divisão inteira)

# x //= 3  é o mesmo que  x = x // 3
# divide e guarda só a parte inteira (sem decimal)

x = 10
x //= 3
print(x)   # 3  → 10 dividido por 3 = 3.33... mas guarda só o 3


# 
# **= (potência)
# 

# x **= 3  é o mesmo que  x = x ** 3
# eleva x à potência 3 (x ao cubo)

x = 2
x **= 3
print(x)   # 8  → 2³ = 2 x 2 x 2 = 8


# RESUMO

# atalho    significa
# x += 3    x = x + 3
# x -= 3    x = x - 3
# x *= 3    x = x * 3
# x /= 3    x = x / 3
# x %= 3    x = x % 3   (resto)
# x //= 3   x = x // 3  (divisão inteira)
# x **= 3   x = x ** 3  (potência)


