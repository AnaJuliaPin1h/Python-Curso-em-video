# ==========================================================
# CONDIÇÕES EM PYTHON
# ==========================================================

# As condições são usadas para tomar decisões no programa.
# Elas permitem executar diferentes blocos de código
# dependendo do resultado de um teste lógico.

# ----------------------------------------------------------
# OPERADORES DE COMPARAÇÃO
# ----------------------------------------------------------

# ==  Igual a
# !=  Diferente de
# <   Menor que
# <=  Menor ou igual a
# >   Maior que
# >=  Maior ou igual a

# Esses operadores são usados principalmente nas estruturas:
# if, elif e else.

# ==========================================================
# IF
# ==========================================================

# A instrução if executa um bloco de código somente
# quando a condição for verdadeira (True).

# Exemplo:

a = 33
b = 200

if b > a:
    print("b é maior que a")

# Explicação:
# O Python verifica se b é maior que a.
# Como 200 > 33, a condição é verdadeira.
# Portanto, o bloco dentro do if é executado.

# ==========================================================
# COMO O IF FUNCIONA
# ==========================================================

# Toda condição retorna:
# True  -> Verdadeiro
# False -> Falso

# Se for True:
# O código dentro do if será executado.

# Se for False:
# O Python ignora o bloco do if.

# ==========================================================
# INDENTAÇÃO (RECUO)
# ==========================================================

# Python utiliza espaços no início da linha para indicar
# quais instruções pertencem ao bloco da condição.

# Exemplo correto:

idade = 20

if idade >= 18:
    print("Você é maior de idade")

# Se não houver recuo, ocorrerá erro de sintaxe.

# ==========================================================
# VÁRIAS INSTRUÇÕES DENTRO DE UM IF
# ==========================================================

idade = 20

if idade >= 18:
    print("Você é adulto")
    print("Você pode votar")
    print("Você possui todos os direitos legais")

# Todas as instruções recuadas serão executadas.

# ==========================================================
# USANDO VARIÁVEIS BOOLEANAS
# ==========================================================

# Variáveis booleanas possuem apenas dois valores:
# True ou False.

usuario_logado = True

if usuario_logado:
    print("Bem-vindo de volta!")

# Não é necessário escrever:
# if usuario_logado == True

# ==========================================================
# ELIF
# ==========================================================

# A palavra-chave elif significa:
# "Se a condição anterior não for verdadeira,
# tente esta condição."

a = 33
b = 33

if b > a:
    print("b é maior que a")
elif a == b:
    print("a e b são iguais")

# Como b > a é falso,
# o Python verifica a condição do elif.

# ==========================================================
# VÁRIOS ELIF
# ==========================================================

# Você pode utilizar quantos elif forem necessários.

nota = 75

if nota >= 90:
    print("Conceito A")
elif nota >= 80:
    print("Conceito B")
elif nota >= 70:
    print("Conceito C")
elif nota >= 60:
    print("Conceito D")

# Resultado:
# Conceito C

# ==========================================================
# COMO O ELIF FUNCIONA
# ==========================================================

# O Python verifica as condições de cima para baixo.

# Assim que encontra a primeira condição verdadeira:
# ✔ Executa aquele bloco.
# ✔ Ignora todas as demais condições.

# Apenas o primeiro bloco verdadeiro será executado.

# ==========================================================
# EXEMPLO DE FAIXA ETÁRIA
# ==========================================================

idade = 25

if idade < 13:
    print("Você é uma criança")
elif idade < 20:
    print("Você é um adolescente")
elif idade < 65:
    print("Você é um adulto")
else:
    print("Você é um idoso")

# Resultado:
# Você é um adulto

# ==========================================================
# QUANDO USAR ELIF?
# ==========================================================

# Utilize elif quando houver várias condições
# mutuamente exclusivas.

dia = 3

if dia == 1:
    print("Segunda-feira")
elif dia == 2:
    print("Terça-feira")
elif dia == 3:
    print("Quarta-feira")
elif dia == 4:
    print("Quinta-feira")
elif dia == 5:
    print("Sexta-feira")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")

# ==========================================================
# ELSE
# ==========================================================

# O else captura qualquer situação que não foi
# atendida pelas condições anteriores.

a = 200
b = 33

if b > a:
    print("b é maior que a")
elif a == b:
    print("a e b são iguais")
else:
    print("a é maior que b")

# Resultado:
# a é maior que b

# ==========================================================
# ELSE SEM ELIF
# ==========================================================

# Não é obrigatório utilizar elif.

a = 200
b = 33

if b > a:
    print("b é maior que a")
else:
    print("b não é maior que a")

# ==========================================================
# ESTRUTURA COMPLETA
# ==========================================================

temperatura = 22

if temperatura > 30:
    print("Está muito quente!")
elif temperatura > 20:
    print("Está agradável!")
elif temperatura > 10:
    print("Está fresco!")
else:
    print("Está frio!")

# ==========================================================
# IF EM UMA LINHA (SHORT HAND IF)
# ==========================================================

# Quando houver apenas uma instrução,
# é possível escrever tudo em uma única linha.

a = 5
b = 2

if a > b: print("a é maior que b")

# Os dois pontos (:) continuam obrigatórios.

# ==========================================================
# RESUMO
# ==========================================================

# if
# Testa uma condição.

# elif
# Testa outra condição caso as anteriores sejam falsas.

# else
# Executa quando nenhuma condição anterior for verdadeira.

# Estrutura geral:

# if condição:
#     código

# elif outra_condição:
#     código

# else:
#     código


# ==========================================================
# OPERADORES LÓGICOS EM PYTHON
# ==========================================================

# Operadores lógicos são usados para combinar
# condições e criar expressões mais complexas.

# Python possui três operadores lógicos principais:

# and -> Retorna True se todas as condições forem verdadeiras.
# or  -> Retorna True se pelo menos uma condição for verdadeira.
# not -> Inverte o resultado da condição.

# ==========================================================
# OPERADOR AND
# ==========================================================

# O operador and exige que TODAS as condições
# sejam verdadeiras para retornar True.

# Sintaxe:
# condição1 and condição2

# Exemplo:

a = 200
b = 33
c = 500

if a > b and c > a:
    print("As duas condições são verdadeiras")

# Explicação:
# a > b  -> True
# c > a  -> True
#
# Como ambas são verdadeiras,
# o resultado final é True.

# ==========================================================
# OPERADOR OR
# ==========================================================

# O operador or exige que pelo menos UMA das
# condições seja verdadeira.

# Sintaxe:
# condição1 or condição2

# Exemplo:

a = 200
b = 33
c = 500

if a > b or a > c:
    print("Pelo menos uma condição é verdadeira")

# Explicação:
# a > b -> True
# a > c -> False
#
# Como existe pelo menos uma condição verdadeira,
# o resultado final é True.

# ==========================================================
# OPERADOR NOT
# ==========================================================

# O operador not inverte o resultado da condição.

# Se a condição for True,
# o not transforma em False.

# Se a condição for False,
# o not transforma em True.

# Exemplo:

a = 33
b = 200

if not a > b:
    print("a NÃO é maior que b")

# Explicação:
# a > b -> False
#
# not False -> True
#
# Portanto, o bloco é executado.

# ==========================================================
# ORDEM DE PRECEDÊNCIA DOS OPERADORES LÓGICOS
# ==========================================================

# Quando vários operadores aparecem juntos,
# o Python segue a seguinte ordem:

# 1° not
# 2° and
# 3° or

# Exemplo:

idade = 25
e_estudante = False
possui_cupom = True

if (idade < 18 or idade > 65) and not e_estudante or possui_cupom:
    print("Desconto aplicado!")

# ==========================================================
# USANDO PARÊNTESES
# ==========================================================

# Em condições mais complexas, utilize parênteses.
#
# Isso torna o código mais fácil de ler
# e ajuda a controlar a ordem de avaliação.

# Exemplo:

temperatura = 25
esta_chovendo = False
fim_de_semana = True

if (temperatura > 20 and not esta_chovendo) or fim_de_semana:
    print("Ótimo dia para atividades ao ar livre!")

# Explicação:
#
# temperatura > 20      -> True
# not esta_chovendo     -> True
#
# True and True         -> True
#
# Como a primeira parte já é True,
# a condição inteira será verdadeira.

# ==========================================================
# TABELA RESUMO
# ==========================================================

# AND
#
# True  and True  -> True
# True  and False -> False
# False and True  -> False
# False and False -> False

# OR
#
# True  or True  -> True
# True  or False -> True
# False or True  -> True
# False or False -> False

# NOT
#
# not True  -> False
# not False -> True

# ==========================================================
# RESUMO
# ==========================================================

# and
# Todas as condições precisam ser verdadeiras.

# or
# Pelo menos uma condição precisa ser verdadeira.

# not
# Inverte o resultado da condição.

# Ordem de avaliação:
# 1° not
# 2° and
# 3° or

# Utilize parênteses para melhorar a legibilidade
# e evitar erros em expressões complexas.