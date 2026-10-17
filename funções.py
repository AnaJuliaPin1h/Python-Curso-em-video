# TÓPICO 1 — DEFININDO E CHAMANDO FUNÇÕES

# EXEMPLO 1: Função simples sem parâmetros
# Eu defino uma função que exibe uma saudação fixa.
def mostrar_boas_vindas():
    print("Bem-vinda ao meu programa de estudos!")


# Eu chamo a função sempre que quiser executar esse bloco.
mostrar_boas_vindas()
mostrar_boas_vindas()  # Eu reutilizo o mesmo código sem repeti-lo.


# EXEMPLO 2: Função com parâmetros
# Eu defino uma função que recebe dois valores e exibe a soma.
def somar(a, b):
    print(f"{a} + {b} = {a + b}")


# Eu passo os valores ao chamar a função.
somar(3, 4)    # 3 + 4 = 7
somar(10, 25)  # 10 + 25 = 35


# TÓPICO 2 — RETORNO COM return

# EXEMPLO 1: Devolvendo um valor
# Eu calculo a área de um retângulo e devolvo o resultado.
def area_retangulo(largura, altura):
    area = largura * altura
    return area  # Eu entrego o valor para quem chamou a função.


# Eu guardo o valor devolvido em uma variável.
resultado = area_retangulo(5, 3)
print(f"A área é {resultado}")  # A área é 15


# EXEMPLO 2: Devolvendo múltiplos valores
# Eu calculo a nota e a situação do aluno e devolvo os dois valores.
def avaliar_nota(nota):
    situacao = "Aprovada" if nota >= 7 else "Em recuperação"
    return nota, situacao  # Eu devolvo uma tupla com os dois valores.


# Eu desempacoto os valores devolvidos pela função.
nota, situacao = avaliar_nota(8.5)
print(f"Nota {nota}: {situacao}")  # Nota 8.5: Aprovada


# TÓPICO 3 — PARÂMETROS COM VALOR PADRÃO

# EXEMPLO 1: Valor padrão simples
# Eu defino "Oi" como saudação padrão, caso ninguém informe outra.
def cumprimentar(nome, saudacao="Oi"):
    return f"{saudacao}, {nome}!"


print(cumprimentar("Ana"))             # Oi, Ana!
print(cumprimentar("Ana", "Bom dia"))  # Bom dia, Ana!


# EXEMPLO 2: Parâmetros nomeados
# Eu defino uma função com três parâmetros.
# Curso e semestre possuem valores padrão.
def criar_perfil(nome, curso="ADS", semestre=1):
    return f"{nome} | {curso} | {semestre}º semestre"


# Eu passo o argumento pelo nome, sem precisar informar todos os parâmetros.
print(criar_perfil("Ana Júlia", semestre=6))
# Ana Júlia | ADS | 6º semestre


# TÓPICO 4 — NÚMERO VARIÁVEL DE ARGUMENTOS

# EXEMPLO 1: Usando *args
# Eu aceito quantos números quiser e calculo a soma.
def somar_todos(*numeros):
    # numeros é uma tupla com todos os valores recebidos.
    return sum(numeros)


print(somar_todos(1, 2, 3))         # 6
print(somar_todos(10, 20, 30, 40))  # 100


# EXEMPLO 2: Usando **kwargs
# Eu aceito argumentos nomeados e monto uma ficha com eles.
def montar_ficha(**dados):
    # dados é um dicionário com os argumentos nomeados.
    for campo, valor in dados.items():
        print(f"{campo}: {valor}")


montar_ficha(nome="Ana Júlia", curso="ADS", cidade="São Paulo")


# TÓPICO 5 — FUNÇÕES COMO VALORES E FUNÇÕES lambda

# EXEMPLO 1: Passando uma função como argumento
# Eu aplico uma função a cada item de uma lista.
def aplicar_em_lista(funcao, lista):
    return [funcao(item) for item in lista]


def dobro(n):
    return n * 2


# Eu passo a função dobro como argumento, sem chamá-la com parênteses.
print(aplicar_em_lista(dobro, [1, 2, 3]))  # [2, 4, 6]


# EXEMPLO 2: Função lambda
# Eu crio uma função anônima e curta para elevar um número ao quadrado.
quadrado = lambda x: x ** 2

print(quadrado(5))  # 25

# Eu uso lambda como critério de ordenação dos alunos pela nota.
alunos = [
    ("Camila", 9.1),
    ("João", 7.2),
    ("Ana Júlia", 8.7)
]

ordenados = sorted(alunos, key=lambda aluno: aluno[1], reverse=True)
print(ordenados)


# TÓPICO 6 — ESCOPO DE VARIÁVEIS

# EXEMPLO 1: Variável local e global
contador = 0  # Eu defino uma variável global.


def incrementar():
    # Eu crio uma variável local, que existe somente dentro da função.
    contador_local = 10
    print(f"Dentro da função: {contador_local}")


incrementar()

# print(contador_local)
# Se eu tentar acessar contador_local aqui, ocorre um erro,
# porque essa variável só existe dentro da função.

print(f"Fora da função: {contador}")


# EXEMPLO 2: Usando global para alterar uma variável externa
total = 0  # Eu defino uma variável global.


def adicionar(valor):
    global total  # Eu aviso que quero alterar a variável global.
    total += valor


adicionar(5)
adicionar(3)

print(total)  # 8


# TÓPICO 7 — FUNÇÕES RECURSIVAS

# EXEMPLO 1: Fatorial
# Eu chamo a própria função até chegar ao caso base.
def fatorial(n):
    if n <= 1:
        return 1  # Caso base: eu paro a recursão aqui.

    # Eu reduzo o problema chamando a função com n - 1.
    return n * fatorial(n - 1)


print(fatorial(5))  # 120


# EXEMPLO 2: Soma recursiva de uma lista
# Eu somo os elementos de uma lista usando recursão.
def soma_recursiva(lista):
    if not lista:
        return 0  # Caso base: uma lista vazia soma zero.

    # Eu somo o primeiro item com a soma do restante da lista.
    return lista[0] + soma_recursiva(lista[1:])


print(soma_recursiva([4, 5, 6]))  # 15