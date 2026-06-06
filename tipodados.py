# Variáveis podem armazenar dados de diferentes tipos

# Tipos de Dados em Python:
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Obtendo o Tipo de Dados
# Posso obter o tipo de dados de qualquer objeto usando a função type()
x = 5
print(type(x))  # <class 'int'>

# Exemplos de variáveis de diferentes tipos:

x1 = "Hello World"  
# str (string) -> Texto entre aspas. Pode conter letras, números ou símbolos
# Exemplos: "Python", "123"

x2 = 20  
# int (inteiro) -> Número sem parte decimal
# Exemplos: 5, -100

x3 = 20.5  
# float (ponto flutuante) -> Número com parte decimal
# Exemplos: 3.14, -0.001

x4 = 1j  
# complex -> Número com parte imaginária (em Python, j indica a parte imaginária)
# Exemplos: 2 + 3j

x5 = ["apple", "banana", "cherry"]  
# list -> Coleção ordenada e mutável de elementos. Pode conter tipos diferentes
# Exemplos: [1, "a", 3.5]

x6 = ("apple", "banana", "cherry")  
# tuple -> Coleção ordenada, mas imutável
# Exemplos: (1, 2, 3)

x7 = range(6)  
# range -> Sequência de números, normalmente usada em loops
# Exemplo: range(0, 5) gera [0, 1, 2, 3, 4]

x8 = {"name": "John", "age": 36}  
# dict -> Dicionário, coleção de pares chave: valor
# Exemplo: {"cor": "azul", "tamanho": "M"}

x9 = {"apple", "banana", "cherry"}  
# set -> Conjunto, coleção não ordenada de elementos únicos
# Exemplo: {1, 2, 3}

x10 = frozenset({"apple", "banana", "cherry"})  
# frozenset -> Igual ao set, mas imutável. Não dá para adicionar ou remover elementos

x11 = True  
# bool -> Representa verdadeiro ou falso
# Exemplos: True, False

x12 = b"Hello"  
# bytes -> Sequência de bytes (valores binários), usada em manipulação de dados binários
# Exemplo: b"Python"

x13 = bytearray(5)  
# bytearray -> Sequência de bytes mutável. Pode ser alterada depois de criada

x14 = memoryview(bytes(5))  
# memoryview -> Permite acessar bytes de forma eficiente, sem criar cópias

x15 = None  
# NoneType -> Representa ausência de valor ou “vazio”









#Variáveis
#• Espaços de memória que designamos com um nome e 
#armazenamos valores.
#• Estes valores podem ser modificados e utilizados em qualquer ponto do programa.
#• Atribuímos um valor a uma variável por meio do sinal de igualdade

# ==============================
# Resolução de Problemas
# Entrada -> Processamento -> Saída
# ==============================

# 1. Leia atentamente o enunciado.
# 2. Identifique as entradas de dados.
# 3. Identifique as saídas de dados.
# 4. Pense em como transformar as entradas nas saídas desejadas.
# 5. Elabore um algoritmo para resolver o problema.
# 6. Teste o algoritmo.
# 7. Implemente na linguagem desejada.

# ==============================
# Etapas para Resolver um Problema
# ==============================

# Entendimento:
# - Ler e compreender o problema a ser resolvido.

# Diagramação:
# - Elaborar o algoritmo (fluxograma ou pseudocódigo).

# Codificação:
# - Implementar o algoritmo na linguagem desejada.