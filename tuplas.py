from collections import namedtuple
import math


# Exemplo 1: Registro de alunos com tuplas nomeadas

# Eu crio um modelo de tupla chamado Aluno.
# Cada aluno terá quatro campos: nome, curso, semestre e média.
# Com namedtuple, eu acesso os dados pelo nome do campo,
# em vez de precisar lembrar a posição de cada informação.
Aluno = namedtuple("Aluno", ["nome", "curso", "semestre", "media"])

# Eu crio uma lista com os dados de três alunos.
# Cada elemento é um objeto Aluno com os campos nomeados.
turma = [
    Aluno("Ana Júlia", "ADS", 6, 8.7),
    Aluno("João", "ADS", 4, 7.2),
    Aluno("Camila", "ADS", 5, 9.1),
]

# Eu percorro a turma para acessar os dados de cada aluno.
for aluno in turma:

    # Eu acesso os campos pelo nome, como aluno.nome e aluno.media.
    print(
        f"{aluno.nome} está no {aluno.semestre}º semestre, "
        f"média {aluno.media}"
    )

# Eu uso max() para encontrar o aluno com a maior média.
# O argumento key=lambda a: a.media indica que devo comparar
# os alunos pelo valor do campo media.
melhor = max(turma, key=lambda a: a.media)

# Eu mostro o nome e a média do aluno com o melhor resultado.
print(f"Maior média: {melhor.nome} ({melhor.media})")

# Eu também posso desempacotar uma namedtuple normalmente.
# Cada variável recebe o valor correspondente à posição do campo.
nome, curso, semestre, media = turma[0]

# Eu mostro o nome e a média do primeiro aluno.
print(nome, media)

# As tuplas são imutáveis: eu não posso alterar diretamente
# um campo da tupla original.
# Porém, namedtuple oferece _replace() para criar uma nova tupla
# com um dos campos substituídos.
aluno_atualizado = turma[1]._replace(media=7.5)

# Eu mostro a nova versão do registro.
# O aluno original continua com média 7.2.
print(aluno_atualizado)


# Exemplo 2: Coordenadas e cálculo de distância

# Eu importo math para utilizar a função sqrt(),
# que calcula a raiz quadrada.
# (A importação já foi feita no início do arquivo.)

# Eu crio uma função que recebe dois pontos.
# Cada ponto é uma tupla com duas coordenadas: x e y.
def distancia(p1, p2):

    # Eu desempacoto as coordenadas do primeiro ponto.
    x1, y1 = p1

    # Eu desempacoto as coordenadas do segundo ponto.
    x2, y2 = p2

    # Eu calculo a distância entre os pontos usando
    # a fórmula da distância no plano cartesiano:
    # raiz quadrada de (x2 - x1)² + (y2 - y1)².
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Eu crio três pontos representados por tuplas.
origem = (0, 0)
ponto_a = (3, 4)
ponto_b = (6, 8)

# Eu calculo e mostro a distância entre a origem e o ponto A.
print(f"Distância da origem até A: {distancia(origem, ponto_a)}")

# Eu calculo e mostro a distância entre A e B.
print(f"Distância de A até B: {distancia(ponto_a, ponto_b)}")

# Eu posso usar tuplas como chaves de um dicionário.
# Como estas tuplas contêm números imutáveis, elas podem ser usadas
# para identificar cada coordenada.
cidades = {
    (-23.55, -46.63): "São Paulo",
    (-22.90, -43.17): "Rio de Janeiro",
}

# Eu acesso o nome da cidade usando a tupla de coordenadas como chave.
print(cidades[(-23.55, -46.63)])


# Exemplo 3: Desempacotamento avançado com *

# Eu crio uma tupla com informações pessoais e acadêmicas.
registro = ("Ana Júlia", "ADS", "UMC", 2023, 2027, "SP", "Brasil")

# Eu desempacoto a tupla em três partes:
# nome recebe o primeiro elemento;
# *meio recebe todos os elementos intermediários;
# pais recebe o último elemento.
#
# O operador * captura os valores restantes em uma lista.
nome, *meio, pais = registro

# Eu mostro o primeiro elemento.
print(nome)

# Eu mostro os elementos que ficaram no meio.
# Mesmo que registro seja uma tupla, meio será uma lista.
print(meio)

# Eu mostro o último elemento.
print(pais)

# Eu crio uma função que recebe um primeiro argumento
# e depois pode receber vários argumentos adicionais.
def resumo(primeiro, *demais):

    # Eu uso len() para contar quantos argumentos adicionais recebi.
    # demais é uma tupla dentro da função.
    print(
        f"Primeiro: {primeiro}, "
        f"quantidade restante: {len(demais)}"
    )

# Eu uso *registro para desempacotar os elementos da tupla.
# Cada elemento será enviado como um argumento separado à função.
resumo(*registro)

# Eu crio duas variáveis com valores iniciais.
a, b = 1, 2

# Eu troco os valores das variáveis em uma única instrução.
# Python permite desempacotar os valores da direita nas variáveis
# da esquerda, sem precisar criar uma variável temporária.
a, b = b, a

# Eu mostro os valores depois da troca.
print(a, b)


# Exemplo 4: Retornando múltiplos valores de uma função

# Eu crio uma função que recebe uma sequência de notas.
def estatisticas(notas):

    # Eu encontro a menor nota usando min().
    minimo = min(notas)

    # Eu encontro a maior nota usando max().
    maximo = max(notas)

    # Eu calculo a média somando as notas e dividindo
    # pela quantidade de elementos.
    media = sum(notas) / len(notas)

    # Eu retorno os três resultados separados por vírgulas.
    # Python reúne esses valores em uma tupla.
    return minimo, maximo, media


# Eu chamo a função e desempacoto os três resultados
# diretamente nas variáveis menor, maior e media.
menor, maior, media = estatisticas([7.0, 9.5, 8.0, 6.5])

# Eu mostro as estatísticas calculadas.
print(f"Menor: {menor}, Maior: {maior}, Média: {media:.2f}")

# Eu também posso guardar a tupla retornada inteira
# em uma única variável, sem desempacotar os valores.
resultado = estatisticas([10, 5, 8])

# Eu acesso somente a média pelo índice 2.
# Os índices de uma tupla começam em 0:
# 0 = mínimo, 1 = máximo, 2 = média.
print(resultado[2])