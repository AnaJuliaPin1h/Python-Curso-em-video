#------------------------------------------------------------------------------------
# STRING VAZIA vs NONE vs VARIÁVEL NÃO DEFINIDA
#------------------------------------------------------------------------------------

# "" → texto vazio
# None → ausência de valor

#------------------------------------------------------------------------------------
# 1. Caixa de sapatos vazia — String Vazia ("")
#------------------------------------------------------------------------------------

# É uma string vazia. Existe um valor armazenado,
# mas esse valor é um texto com zero caracteres.
a = ""

#------------------------------------------------------------------------------------
# 2. Etiqueta "Sem Valor" — Nulo (None)
#------------------------------------------------------------------------------------

# O Python sabe que a variável existe, mas não tem dado nenhum.
# A variável existe e seu valor é None,
# que representa a ausência de valor.
a1 = None

#------------------------------------------------------------------------------------
# 3. Variável Não Definida — Simulação do erro (a variável nem existe)
#------------------------------------------------------------------------------------

# NÃO crie a variável aqui. Se tentar usar 'c' abaixo, dará NameError.
# c = <-- Isso daria erro de sintaxe se deixado assim.
# Erro: NameError: name 'c' is not defined

#------------------------------------------------------------------------------------
# 4. Variável com Texto
#------------------------------------------------------------------------------------

b = "Ola mundo"

#------------------------------------------------------------------------------------
# Resultados
#------------------------------------------------------------------------------------

print(f"a: '{a}'")   # Saída: a: ''        (vazio, mas existe)
print(f"a1: {a1}")   # Saída: a1: None
print(f"b: {b}")     # Saída: b: Ola mundo

# Descomente a linha abaixo para ver o erro de Variável Não Definida:
# print(c)           # Erro: NameError: name 'c' is not defined

#------------------------------------------------------------------------------------
# RESUMO — Para que servem esses três conceitos?
#------------------------------------------------------------------------------------

# ""           → Valor conhecido (texto vazio).
#                Uso: inicializar acumuladores antes de um loop.
#                Ex: resultado = "" (antes de somar palavras de uma lista)

# None         → Estado conhecido (ausência de valor).
#                Uso: controlar fluxo — distinguir "valor vazio" de "ainda não calculado".
#                Ex: if a1 is None: → toma um caminho diferente (mostra erro ou tenta de novo)

# Não definida → Erro lógico (uso inválido).
#                O NameError é um mecanismo de segurança: impede o programa de rodar
#                com dados incorretos, forçando o programador a declarar variáveis antes do uso.

#------------------------------------------------------------------------------------
# CRIANDO VARIÁVEIS
# Python não tem comando para declarar variável.
# Ela é criada no momento em que você atribui um valor pela primeira vez.
#------------------------------------------------------------------------------------

x = 5
y = "John"
print(x)   # Saída: 5
print(y)   # Saída: John

#------------------------------------------------------------------------------------
# TIPAGEM DINÂMICA
# Variáveis não precisam ser declaradas com tipo fixo.
# Podem mudar de tipo depois de definidas.
#------------------------------------------------------------------------------------

x = 44      # x é do tipo int
x = "Sally" # x agora é do tipo str (mesmo nome, valor diferente)
print(x)    # Saída: Sally

#------------------------------------------------------------------------------------
# REGRAS PARA NOMES DE VARIÁVEIS
#------------------------------------------------------------------------------------

# CERTOS: Nomes LEGAIS:
myvar    = "John"
my_var   = "John"
_meu_var = "John"
meuVar   = "John"   # camelCase
MEUVAR   = "John"   # UPPER_CASE
myvar2   = "John"   # com número no final

# ERRADO: Nomes ILEGAIS (causam erro de sintaxe):
# 2myvar  = "John"   → não pode começar com número
# meu-var = "John"   → hífen não é permitido
# meu var = "John"   → espaço não é permitido

# Regras resumidas:
# • Começa com letra ou _ (nunca com número)
# • Só usa letras, números e _ (sem hífen, espaço ou especiais)
# • É case-sensitive: age, Age e AGE são três variáveis diferentes
# • Não pode ser uma palavra reservada do Python (if, for, while, etc.)

#------------------------------------------------------------------------------------
# ATRIBUIÇÃO MÚLTIPLA — Vários valores em uma linha
#------------------------------------------------------------------------------------

x, y, z, u = "Orange", "Banana", "Cherry", "Uva"
print(x)   # Orange
print(y)   # Banana
print(z)   # Cherry
print(u)   # Uva

# OBSERVAÇÃO: O número de variáveis deve corresponder ao número de valores.

#------------------------------------------------------------------------------------
# UM VALOR PARA MÚLTIPLAS VARIÁVEIS
#------------------------------------------------------------------------------------

x = y = z = "Laranja"
print(x)   # Laranja
print(y)   # Laranja
print(z)   # Laranja

#------------------------------------------------------------------------------------
# DESEMPACOTAMENTO DE LISTA
# Pega os valores dentro de uma lista e coloca em variáveis separadas.
# O número de variáveis deve ser exatamente igual ao número de elementos.
#------------------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "Uva", "Frutas"]
x, y, z, u, f = fruits

print(x)   # apple
print(y)   # banana
print(z)   # cherry
print(u)   # Uva
print(f)   # Frutas

#------------------------------------------------------------------------------------
# SAÍDA DE VARIÁVEIS COM print()
#------------------------------------------------------------------------------------

x = "Python é demais"
print(x)   # Saída: Python é demais

#------------------------------------------------------------------------------------
# FORMAS DE JUNTAR VALORES NO print()
#------------------------------------------------------------------------------------

# Forma 1 — Usando vírgula ,
# O print() recebe valores separados e adiciona espaços automaticamente.
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)   # Saída: Python is awesome

# Forma 2 — Usando o operador +
# Concatena os textos exatamente como estão (sem espaços automáticos).
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)            # Saída: Python is awesome
print("Python is " + "awesome")  # Saída: Python is awesome

#------------------------------------------------------------------------------------
# + COM NÚMEROS vs + COM STRINGS
#------------------------------------------------------------------------------------

a = 4
b = 5
print(a + b)   # Saída: 9  → operação de SOMA (tipo int)

# Se fossem strings, o + seria CONCATENAÇÃO:
# a = "4"
# b = "5"
# print(a + b)  → Saída: "45"

#------------------------------------------------------------------------------------