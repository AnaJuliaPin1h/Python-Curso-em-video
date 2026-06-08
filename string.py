
# strings 1.0


# Uma string em Python é uma sequência de caracteres entre aspas. Você pode acessar, analisar e transformar strings usando métodos embutidos.

nome = "Ana Júlia"


# metodos  Métodos são chamados usando o ponto (.)
texto = "banana"

texto.count("a")
texto.find("n")

# Já funções são chamadas diretamente                        len(texto)
# E operadores são usados entre valores                      "ana" in texto



# len() é uma Função
# count()  É um método           
# find()  É um método
# in  é  um Operador




# ANÁLISE DE STRINGS


# len()  é uma Função
# É uma função embutida (built-in function) do Python.
# Serve para contar a quantidade de caracteres de uma string.
# Conta quantos caracteres existem em uma string.
# Exemplo:
# len("Ana") retorna 3, pois a palavra possui 3 caracteres.




# count()  É um método
# É um método da classe string (str).
# Conta quantas vezes uma letra ou palavra aparece na string.
# Exemplo:
# "banana".count("a") retorna 3, pois a letra "a" aparece 3 vezes.




# find()  É um método
# É um método da classe string (str).
# Retorna a posição (índice) da primeira ocorrência de um caractere ou palavra.
# Se não encontrar, retorna -1.
# Exemplo:
# "banana".find("n") retorna 2, pois o primeiro "n" está na posição 2.



# in  é  um Operador
# É um operador de associação (membership operator).
# Verifica se um texto está presente dentro da string.
# Retorna True (verdadeiro) se encontrar e False (falso) caso contrário.
# Exemplo:
# "ana" in "banana" retorna True, pois "ana" faz parte da palavra "banana".





# TRANSFORMAÇÃO DE STRINGS


# upper()  É um método
# É um método da classe string (str).
# Converte todos os caracteres da string para letras MAIÚSCULAS.
# Exemplo:
# "ana júlia".upper() retorna "ANA JÚLIA"

nome = "ana júlia"
print(nome.upper())   # ANA JÚLIA




# lower()  É um método
# É um método da classe string (str).
# Converte todos os caracteres da string para letras minúsculas.
# Exemplo:
# "ANA JÚLIA".lower() retorna "ana júlia"

nome = "ANA JÚLIA"
print(nome.lower())   # ana júlia




# capitalize()  É um método
# É um método da classe string (str).
# Coloca apenas a PRIMEIRA letra da string em maiúscula e o restante em minúsculas.
# Atenção: só a primeira letra da frase inteira, não de cada palavra.
# Exemplo:
# "ana júlia costa".capitalize() retorna "Ana júlia costa"

nome = "ana júlia costa"
print(nome.capitalize())   # Ana júlia costa




# title()  É um método
# É um método da classe string (str).
# Coloca a primeira letra de CADA PALAVRA em maiúscula.
# Exemplo:
# "ana júlia costa".title() retorna "Ana Júlia Costa"

nome = "ana júlia costa"
print(nome.title())   # Ana Júlia Costa




# replace()  É um método
# É um método da classe string (str).
# Substitui uma parte da string por outra.
# Sintaxe: string.replace("texto antigo", "texto novo")
# Exemplo:
# "oi mundo".replace("mundo", "Ana") retorna "oi Ana"

frase = "oi mundo"
print(frase.replace("mundo", "Ana"))   # oi Ana




# strip()  É um método
# É um método da classe string (str).
# Remove os espaços em branco do início E do fim da string.
# Muito útil para limpar o que o usuário digita com espaços acidentais.
# Exemplo:
# "  oi  ".strip() retorna "oi"

texto = "  oi  "
print(texto.strip())   # oi




# lstrip()  É um método
# É um método da classe string (str).
# Remove os espaços em branco apenas do lado ESQUERDO (início) da string.
# Exemplo:
# "  oi  ".lstrip() retorna "oi  "

texto = "  oi  "
print(texto.lstrip())   # oi  




# rstrip()  É um método
# É um método da classe string (str).
# Remove os espaços em branco apenas do lado DIREITO (fim) da string.
# Exemplo:
# "  oi  ".rstrip() retorna "  oi"

texto = "  oi  "
print(texto.rstrip())   #   oi




# ============================================================
# FATIAMENTO DE STRINGS (Slicing)
# ============================================================


# Fatiamento  usa colchetes [ ]
# Permite acessar partes específicas de uma string usando índices.
# Índices começam em 0 (zero).
# Sintaxe: string[inicio:fim]  →  o caractere do índice "fim" NÃO é incluído.
# Exemplos:
# "banana"[0]    retorna "b"   (primeira letra)
# "banana"[2]    retorna "n"   (letra na posição 2)
# "banana"[1:4]  retorna "ana" (posições 1, 2 e 3)
# "banana"[:3]   retorna "ban" (do início até a posição 2)
# "banana"[3:]   retorna "ana" (da posição 3 até o fim)
# "banana"[-1]   retorna "a"   (última letra — índice negativo)
# "banana"[::-1] retorna "ananab" (string ao contrário)

palavra = "banana"
print(palavra[0])     # b
print(palavra[1:4])   # ana
print(palavra[:3])    # ban
print(palavra[-1])    # a
print(palavra[::-1])  # ananab




# ============================================================
# DIVISÃO DE STRINGS
# ============================================================


# split()  É um método
# É um método da classe string (str).
# Divide a string em uma LISTA de partes, usando um separador.
# Se não informar separador, divide pelos espaços.
# Exemplo:
# "Ana Júlia Costa".split() retorna ["Ana", "Júlia", "Costa"]
# "1-2-3".split("-")        retorna ["1", "2", "3"]

nome = "Ana Júlia Costa"
partes = nome.split()
print(partes)        # ['Ana', 'Júlia', 'Costa']
print(partes[0])     # Ana    (primeiro nome)
print(partes[-1])    # Costa  (último nome)




# ============================================================
# JUNÇÃO DE STRINGS
# ============================================================


# join()  É um método
# É um método da classe string (str).
# Une os elementos de uma lista em uma única string, usando um separador.
# É o oposto do split().
# Sintaxe: "separador".join(lista)
# Exemplo:
# "-".join(["1", "2", "3"]) retorna "1-2-3"
# " ".join(["Ana", "Júlia"]) retorna "Ana Júlia"

lista = ["Ana", "Júlia", "Costa"]
print(" ".join(lista))    # Ana Júlia Costa
print("-".join(lista))    # Ana-Júlia-Costa


####################################################################################
#                                  String 2.0
####################################################################################




# 'olá' é o mesmo que "olá"
# Você pode usar aspas simples ou duplas — funcionam igual.
print("olá")
print('olá')


# ============================================================
# ATRIBUIR STRING A UMA VARIÁVEL
# ============================================================

# Atribuir uma string a uma variável é feito com o nome da variável
# seguido de um sinal de igual e o valor entre aspas.
# O nome da variável pode ser qualquer palavra que você escolher:
# a, txt, nome, frase... tudo funciona igual.

a = "Hello"
print(a)   # Hello


# ============================================================
# STRINGS SÃO ARRAYS (LISTAS DE CARACTERES)
# ============================================================

# Strings são arrays (listas de caracteres).
# Cada letra de uma string ocupa uma posição numerada,
# chamada de ÍNDICE, que começa no ZERO.

a = "Bem-vindo"
#    B  e  m  -  v  i  n  d  o
#    0  1  2  3  4  5  6  7  8

# Para acessar uma letra específica, use colchetes com o índice:
print(a[0])   # B → primeira letra  (posição 0)
print(a[3])   # -  → quarta posição (posição 3)
print(a[-1])  # o → última letra    (índice negativo)


# ============================================================
# LOOP EM STRING — percorrendo letra por letra
# ============================================================

# Como strings são arrays, podemos usar o for para passar
# por cada letra uma de cada vez.
# Cada volta do loop guarda uma letra diferente na variável x.

for x in "banana":
    print(x)
# Imprime uma letra por linha:
# b
# a
# n
# a
# n
# a


# ============================================================
# VERIFICAR SE ALGO ESTÁ NA STRING — operador in / not in
# ============================================================

# "in" verifica se uma palavra ou letra ESTÁ dentro da string.
# Retorna True (verdadeiro) ou False (falso).

txt = "As melhores coisas da vida são de graça!"

print("graça" in txt)       # True  → está presente
print("caro" not in txt)    # True  → NÃO está presente

# Você também pode usar dentro de um if:
if "graça" in txt:
    print("Sim, 'graça' está presente")   # essa linha executa

if "caro" not in txt:
    print("Não, 'caro' NÃO está presente")   # essa linha executa


# ============================================================
# STRINGS SÃO ARRAYS — ÍNDICES E FATIAMENTO
# ============================================================

# Cada letra de uma string ocupa uma posição chamada ÍNDICE.
# O índice começa no ZERO, não no 1.

palavra = "Python"
#          P  y  t  h  o  n
#          0  1  2  3  4  5   → índices positivos (da esquerda pra direita)
#         -6 -5 -4 -3 -2 -1   → índices negativos (da direita pra esquerda)


# ============================================================
# 1. ÍNDICE NORMAL (número positivo)
# ============================================================

# Cada letra tem um número começando do zero.
# Usamos colchetes [ ] para acessar a letra na posição desejada.

print(palavra[0])   # P  → primeira letra (posição 0)
print(palavra[3])   # h  → quarta letra   (posição 3)


# ============================================================
# 2. ÍNDICE NEGATIVO
# ============================================================

# Conta de trás pra frente, começando do -1 (última letra).
# Útil quando você não sabe o tamanho da string e quer pegar do fim.

#  P   y   t   h   o   n
# -6  -5  -4  -3  -2  -1

print(palavra[-1])  # n → última letra
print(palavra[-2])  # o → penúltima letra

# CURIOSIDADE: palavra[2] e palavra[-4] retornam a mesma letra!
# O índice positivo começa do início, o negativo começa do fim.
# P  y  t  h  o  n
# 0  1  2  3  4  5
#-6 -5 -4 -3 -2 -1
print(palavra[2])   # t
print(palavra[-4])  # t  → mesma letra, caminhos diferentes


# ============================================================
# 3. FATIAMENTO [inicio:fim]
# ============================================================

# Pega um PEDAÇO da string.
# REGRA MAIS IMPORTANTE: o índice do FIM não é incluído!

# palavra[1:4]
# P  y  t  h  o  n
# 0  1  2  3  4  5
#    ↑        ↑
# inicio    fim (não entra)
# Pega as posições 1, 2 e 3 → y t h → "yth"

print(palavra[1:4])  # yth

# Outros exemplos de fatiamento:
print(palavra[:3])   # Pyt    → do início até a posição 2 (3 não entra)
print(palavra[3:])   # hon    → da posição 3 até o fim
print(palavra[:])    # Python → a string inteira

# Fatiamento com índice negativo:
# palavra[-4:-1]
# P   y   t   h   o   n
# -6  -5  -4  -3  -2  -1
#          ↑        ↑
#        inicio   fim (não entra)
# Pega as posições -4, -3, -2 → t h o → "tho"

print(palavra[-4:-1])  # tho


# ============================================================
# 4. len() — COMPRIMENTO DA STRING
# ============================================================

# len() é uma função que retorna quantos caracteres a string tem.
# "Python" tem 6 letras, então retorna 6.

print(len(palavra))  # 6


# ============================================================
# 5. LOOP EM STRING — percorrendo letra por letra
# ============================================================

# Como strings são arrays, podemos usar o for para passar
# por cada letra uma de cada vez.

for x in "Pi":
    print(x)
# Imprime:
# P
# i
# (uma letra por linha, na ordem)


# ============================================================
# EXERCÍCIO — palavra = "chocolate"
# ============================================================

palavra = "chocolate"
#          c  h  o  c  o  l  a  t  e
#          0  1  2  3  4  5  6  7  8
#         -9 -8 -7 -6 -5 -4 -3 -2 -1

# 1. palavra[-1]
# Índice -1 sempre é a última letra.
print(palavra[-1])      # e

# 2. palavra[-3]
# Conta 3 posições do fim: -1=e, -2=t, -3=a
print(palavra[-3])      # a

# 3. palavra[0:5]
# Começa na posição 0, vai até a 4 (o 5 NÃO entra).
# posições 0,1,2,3,4 → c,h,o,c,o
print(palavra[0:5])     # choco

# 4. palavra[3:]
# Sem número no fim significa "até o fim da string".
# Começa na posição 3 → c,o,l,a,t,e
print(palavra[3:])      # colate

# 5. palavra[:4]
# Sem número no início significa "desde o começo".
# Vai até a posição 3 (o 4 NÃO entra) → c,h,o,c
print(palavra[:4])      # choc

# 6. palavra[-4:-1]
# Fatiamento com índices negativos — a regra é a mesma: o fim NÃO entra.
#  c   h   o   c   o   l   a   t   e
# -9  -8  -7  -6  -5  -4  -3  -2  -1
# posições -4,-3,-2 → l,a,t  (-1 não entra)
print(palavra[-4:-1])   # lat

# 7. Qual a diferença entre palavra[2] e palavra[-7]?
# palavra[2]  → índice POSITIVO, conta da ESQUERDA começando no 0 → o
# palavra[-7] → índice NEGATIVO, conta da DIREITA começando no -1 → o
# Os dois retornam a mesma letra — só o caminho é diferente!
print(palavra[2])       # o
print(palavra[-7])      # o


# ============================================================
# SLICING — FATIAMENTO DETALHADO
# ============================================================

# Slicing é quando você pega um PEDAÇO (fatia) da string.
# Sintaxe: string[inicio:fim]
# REGRA: o caractere do índice FIM nunca é incluído.

b = "Hello, World!"
#    H  e  l  l  o  ,     W  o  r  l   d   !
#    0  1  2  3  4  5  6  7  8  9  10  11  12


# --- FATIAMENTO COM INÍCIO E FIM ---

# b[2:5] → começa na posição 2, vai até a 4 (5 NÃO entra)
#    H  e  l  l  o
#    0  1  2  3  4  5
#          ↑        ↑
#        inicio   fim (não entra)
# pega posições 2,3,4 → l,l,o
print(b[2:5])    # llo


# --- FATIAMENTO SEM INÍCIO (começa do zero) ---

# Quando você não coloca número antes dos dois pontos,
# Python entende que começa do INÍCIO da string (posição 0).
# b[:5] → do começo até a posição 4 (5 NÃO entra)
#    H  e  l  l  o  ,
#    0  1  2  3  4  5
#    ↑           ↑
# início       fim (não entra)
# pega posições 0,1,2,3,4 → H,e,l,l,o
print(b[:5])     # Hello


# --- FATIAMENTO SEM FIM (vai até o final) ---

# Quando você não coloca número depois dos dois pontos,
# Python entende que vai até o FIM da string.
# b[2:] → da posição 2 até o último caractere
#    H  e  l  l  o  ,     W  o  r  l   d   !
#    0  1  2  3  4  5  6  7  8  9  10  11  12
#          ↑
#        início (vai até o fim)
print(b[2:])     # llo, World!


# --- FATIAMENTO COM ÍNDICE NEGATIVO ---

# Você também pode fatiar usando índices negativos.
# Lembre: índice negativo conta de trás pra frente, começando no -1.

#    H   e   l   l   o   ,      W   o   r   l   d   !
#   -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

# b[-5:-2] → da posição -5 até a -3 (-2 NÃO entra)
# -5=o, -4=r, -3=l, -2=d  → mas -2 não entra, então pega -5,-4,-3 → o,r,l
print(b[-5:-2])  # orl


# ============================================================
# EXERCÍCIO — x = 'Welcome'
# ============================================================

# Qual será o resultado de: x = 'Welcome'  /  print(x[3:5])

x = 'Welcome'
#    W  e  l  c  o  m  e
#    0  1  2  3  4  5  6

# x[3:5] → começa na posição 3, vai até a 4 (5 NÃO entra)
# posição 3 = c
# posição 4 = o
# posição 5 = m → NÃO entra
# resultado: c,o → "co"

print(x[3:5])   # co

# As outras opções estavam erradas porque:
# "lcome" → seria x[2:] ou x[2:7], começa na posição 2
# "come"  → seria x[3:7], vai até o fim a partir do 3
# "com"   → seria x[3:6], pega posições 3,4,5
