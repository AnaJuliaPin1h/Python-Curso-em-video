# Exemplo 1: Gerenciador de tarefas com operações em lista

# Eu crio uma lista chamada tarefas.
# Cada tarefa é um dicionário que guarda o título e o status.
# False significa que a tarefa ainda não foi concluída.
# True significa que a tarefa já foi concluída.
tarefas = [
    {"titulo": "Estudar listas", "concluida": False},
    {"titulo": "Revisar exercícios", "concluida": True},
    {"titulo": "Enviar relatório", "concluida": False},
]

# Eu adiciono uma nova tarefa ao final da lista.
# append() recebe um elemento e coloca esse elemento no final.
tarefas.append({
    "titulo": "Fazer exercício físico",
    "concluida": False
})

# Eu insiro uma tarefa urgente na posição 0.
# insert(0, ...) coloca a tarefa no início da lista.
tarefas.insert(0, {
    "titulo": "Responder e-mail da UMC",
    "concluida": False
})

# Eu percorro as tarefas para encontrar a primeira que está pendente.
for tarefa in tarefas:

    # Eu verifico se a tarefa ainda não foi concluída.
    # not False resulta em True.
    if not tarefa["concluida"]:

        # Eu altero o status da primeira tarefa pendente para True.
        tarefa["concluida"] = True

        # Eu uso break para parar o for.
        # Assim, eu marco apenas uma tarefa como concluída.
        break

# Eu crio uma nova lista contendo somente os títulos das tarefas pendentes.
# A compreensão de lista percorre todas as tarefas.
# A condição filtra aquelas cujo status é False.
pendentes = [
    tarefa["titulo"]
    for tarefa in tarefas
    if not tarefa["concluida"]
]

# Eu mostro os títulos das tarefas que ainda preciso realizar.
print("Pendentes:", pendentes)

# Eu substituo a lista tarefas por uma nova lista
# que contém apenas as tarefas não concluídas.
# Dessa forma, eu removo as concluídas sem modificar a lista
# enquanto estou percorrendo seus elementos.
tarefas = [
    tarefa
    for tarefa in tarefas
    if not tarefa["concluida"]
]

# Eu ordeno as tarefas restantes pelo título, em ordem alfabética.
# sort() modifica a própria lista.
# key=lambda tarefa: tarefa["titulo"] define o critério da ordenação.
tarefas.sort(key=lambda tarefa: tarefa["titulo"])

# Eu mostro somente os títulos das tarefas restantes.
print([tarefa["titulo"] for tarefa in tarefas])


# Exemplo 2: Removendo duplicatas mantendo a ordem

# Eu crio uma função que recebe uma lista e devolve outra
# lista sem elementos repetidos, preservando a ordem original.
def remover_duplicatas(lista):

    # Eu crio um conjunto vazio para registrar os valores
    # que já encontrei.
    # Um set não guarda elementos duplicados.
    vistos = set()

    # Eu crio uma lista vazia para armazenar o resultado final.
    resultado = []

    # Eu percorro os elementos da lista original, na ordem em que aparecem.
    for item in lista:

        # Eu verifico se o elemento ainda não está no conjunto vistos.
        if item not in vistos:

            # Eu adiciono o elemento ao conjunto.
            # Assim, se ele aparecer novamente, saberei que já foi visto.
            vistos.add(item)

            # Eu adiciono o elemento à lista de resultado.
            # Como só faço isso na primeira ocorrência,
            # a ordem original é preservada.
            resultado.append(item)

    # Eu devolvo a lista sem duplicatas.
    return resultado


# Eu crio uma lista que contém números repetidos.
numeros = [3, 1, 3, 2, 1, 5, 2, 8]

# Eu chamo a função e mostro o resultado.
print(remover_duplicatas(numeros))


# Exemplo 3: Matriz com listas aninhadas

# Eu crio uma matriz em que cada linha representa um aluno
# e cada coluna representa uma nota de prova.
notas = [
    [8.0, 7.5, 9.0],   # Ana Júlia
    [6.0, 7.0, 5.5],   # João
    [9.5, 10.0, 8.5],  # Camila
]

# Eu uso enumerate() para percorrer a matriz.
# Ele me fornece o índice da linha e o conteúdo dessa linha.
for i, linha in enumerate(notas):

    # Eu somo as notas da linha e divido pela quantidade de provas.
    # len(linha) retorna quantas notas aquele aluno possui.
    media = sum(linha) / len(linha)

    # Eu mostro o número do aluno começando em 1,
    # embora os índices da lista comecem em 0.
    print(f"Aluno {i + 1}: média {media:.2f}")

# Eu transponho a matriz para organizar os dados por prova.
# zip(*notas) combina a primeira nota de cada aluno,
# depois a segunda nota de cada aluno e assim por diante.
# list(coluna) converte cada grupo de notas em uma lista.
provas = [
    list(coluna)
    for coluna in zip(*notas)
]

# Eu mostro as notas da primeira prova, que está no índice 0.
print("Notas da prova 1:", provas[0])

# Eu crio uma matriz com 2 linhas e 3 colunas, preenchida com zeros.
# A compreensão externa cria cada linha.
# A compreensão interna cria três zeros independentes em cada linha.
#
# Eu evito [[0] * 3] * 2, porque essa forma repete a referência
# à mesma lista interna. Alterar uma linha poderia afetar a outra.
grade = [
    [0 for _ in range(3)]
    for _ in range(2)
]

# Eu altero o elemento da primeira linha e segunda coluna.
# Os índices começam em 0, então grade[0][1] corresponde
# à posição da linha 1 e coluna 2 para uma pessoa.
grade[0][1] = 5

# Eu mostro a matriz depois da alteração.
print(grade)


# Exemplo 4: Fatiamento avançado e cópia de listas

# Eu crio uma lista de letras.
letras = ["a", "b", "c", "d", "e", "f", "g"]

# Eu uso o fatiamento [1:4].
# O índice 1 é incluído, mas o índice 4 não.
# Portanto, eu recebo os elementos b, c e d.
print(letras[1:4])

# Eu uso [::2] para percorrer a lista com passo 2.
# Isso significa que eu pego um elemento e pulo o próximo.
print(letras[::2])

# Eu uso [::-1] para percorrer a lista de trás para frente.
# O passo -1 inverte a ordem dos elementos.
print(letras[::-1])

# Eu crio uma lista original com três números.
original = [1, 2, 3]

# Eu atribuo original a copia_ref.
# Isso não cria uma nova lista: as duas variáveis apontam
# para o mesmo objeto na memória.
copia_ref = original

# Eu uso [:] para criar uma cópia superficial da lista.
# Neste caso, como os elementos são números, a cópia
# funciona de forma independente para as alterações na lista.
copia_real = original[:]

# Eu adiciono o número 4 usando a referência copia_ref.
# Como copia_ref e original apontam para a mesma lista,
# a lista original também será alterada.
copia_ref.append(4)

# Eu mostro original: ela agora contém o número 4.
print(original)

# Eu mostro copia_real: ela continua com os três números originais.
print(copia_real)


# Exemplo 5: Lista de listas com sorted e múltiplos critérios

# Eu crio uma lista de alunos.
# Cada aluno é representado por uma lista com nome, média e curso.
alunos = [
    ["Camila", 9.1, "ADS"],
    ["João", 7.2, "ADS"],
    ["Ana Júlia", 9.1, "ADS"],
    ["Pedro", 8.0, "ADS"],
]

# Eu uso sorted() para criar uma nova lista ordenada.
# Primeiro, eu comparo a média, em ordem decrescente.
# O sinal de menos em -a[1] faz a maior média aparecer primeiro.
# Se dois alunos tiverem a mesma média, eu comparo os nomes
# em ordem alfabética usando a[0].
#
# A lista original alunos não é modificada por sorted().
ranking = sorted(
    alunos,
    key=lambda a: (-a[1], a[0])
)

# Eu percorro o ranking usando enumerate().
# start=1 faz a contagem das posições começar em 1.
for posicao, (nome, media, curso) in enumerate(ranking, start=1):

    # Eu desempacoto cada registro nas variáveis nome, media e curso.
    # Depois, mostro a posição, o nome e a média do aluno.
    print(f"{posicao}º {nome}: {media}")