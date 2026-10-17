# EXEMPLO 1 — AGENDA DE CONTATOS
# Eu guardo contatos em um dicionário, usando o nome como chave.
# Com ele, posso buscar, atualizar, adicionar, remover e agrupar contatos.

agenda = {
    "Ana Júlia": {
        "telefone": "(11) 97638-3864",
        "cidade": "São Paulo",
        "tags": ["ADS", "Python"]
    },
    "João": {
        "telefone": "(11) 91234-5678",
        "cidade": "Mogi das Cruzes",
        "tags": ["JeansSky"]
    },
    "Camila": {
        "telefone": "(11) 99876-5432",
        "cidade": "São Paulo",
        "tags": ["JeansSky", "ADS"]
    }
}

# Eu busco um contato sem causar erro, usando get() com um valor padrão.
contato = agenda.get("Pedro", {"telefone": "não cadastrado"})
print("Telefone de Pedro:", contato["telefone"])

# Eu atualizo a cidade de um contato existente.
agenda["João"]["cidade"] = "Suzano"

# Eu adiciono um contato novo.
agenda["Maylon"] = {
    "telefone": "(11) 95555-0000",
    "cidade": "Mogi das Cruzes",
    "tags": []
}

# Eu removo um contato e guardo os dados removidos com pop().
removido = agenda.pop("Maylon")
print(f"Removi o contato com telefone {removido['telefone']}")

# Eu agrupo os contatos por cidade.
# setdefault() cria uma lista para a cidade, caso ela ainda não exista.
por_cidade = {}

for nome, dados in agenda.items():
    por_cidade.setdefault(dados["cidade"], []).append(nome)

print("Contatos por cidade:", por_cidade)

# Eu filtro os contatos que possuem a tag "ADS".
contatos_ads = [
    nome
    for nome, dados in agenda.items()
    if "ADS" in dados["tags"]
]

print("Contatos de ADS:", contatos_ads)


# EXEMPLO 2 — CONTAGEM DE FREQUÊNCIA DE PALAVRAS
# Eu conto quantas vezes cada palavra aparece em um texto.

texto = """Eu estudo Python todos os dias. Python é uma linguagem
que eu uso para estudar dados, sistemas e automação."""

# Eu substituo alguns sinais de pontuação por espaços.
for sinal in ".,\n":
    texto = texto.replace(sinal, " ")

# Eu transformo o texto em letras minúsculas e separo as palavras.
palavras = texto.lower().split()

# Eu conto as ocorrências de cada palavra.
contagem = {}

for palavra in palavras:
    # get() retorna 0 se a palavra ainda não estiver no dicionário.
    contagem[palavra] = contagem.get(palavra, 0) + 1

# Eu ordeno as palavras da mais frequente para a menos frequente.
# Depois, seleciono as três primeiras.
top3 = sorted(
    contagem.items(),
    key=lambda par: par[1],
    reverse=True
)[:3]

# Eu mostro as três palavras mais frequentes.
for palavra, vezes in top3:
    print(f"{palavra}: {vezes}")


# EXEMPLO 3 — CADASTRO DE NOTAS COM DICIONÁRIOS
# Eu organizo as notas de cada aluno por matéria.
# Assim, posso calcular médias e encontrar as maiores notas.

notas = {
    "Ana Júlia": {
        "Algoritmos": 8.5,
        "Banco de Dados": 9.0,
        "Redes": 7.5
    },
    "João": {
        "Algoritmos": 5.0,
        "Banco de Dados": 6.5,
        "Redes": 6.0
    },
    "Camila": {
        "Algoritmos": 9.5,
        "Banco de Dados": 8.0,
        "Redes": 9.0
    }
}

# Eu calculo a média de cada aluno.
medias = {
    aluno: sum(materias.values()) / len(materias)
    for aluno, materias in notas.items()
}

print("Médias dos alunos:", medias)

# Eu identifico os alunos com média abaixo de 7.
em_atencao = [
    aluno
    for aluno, media in medias.items()
    if media < 7
]

print("Alunos que precisam de atenção:", em_atencao)

# Eu encontro a maior nota de cada matéria.
melhores_notas = {}

for aluno, boletim in notas.items():
    for materia, nota in boletim.items():

        # Se a matéria ainda não estiver registrada,
        # ou se a nota atual for maior, eu atualizo o dicionário.
        if materia not in melhores_notas or nota > melhores_notas[materia][1]:
            melhores_notas[materia] = (aluno, nota)

# Eu mostro o aluno que teve a maior nota em cada matéria.
for materia, (aluno, nota) in melhores_notas.items():
    print(f"{materia}: melhor nota de {aluno} ({nota})")


# EXEMPLO 4 — CACHE E MEMOIZAÇÃO COM FIBONACCI
# Eu uso um dicionário para guardar resultados já calculados.
# Isso evita que a função recursiva repita cálculos desnecessários.

cache = {}


def fibonacci(n):
    # Se o resultado já estiver no cache, eu devolvo o valor guardado.
    if n in cache:
        return cache[n]

    # Os dois primeiros números da sequência são 0 e 1.
    if n < 2:
        resultado = n
    else:
        # Eu calculo o número somando os dois anteriores.
        resultado = fibonacci(n - 1) + fibonacci(n - 2)

    # Eu guardo o resultado para reutilizá-lo depois.
    cache[n] = resultado

    return resultado


print("Fibonacci de 50:", fibonacci(50))  # 12586269025


# EXEMPLO 5 — dict(), zip() E DESEMPACOTAMENTO
# Eu combino listas para criar um dicionário e uso ** para mesclar dicionários.

# Eu crio uma lista de campos e outra lista com seus valores.
campos = ["nome", "curso", "semestre"]
valores = ["Ana Júlia", "ADS", 4]

# zip() combina os itens correspondentes das duas listas.
# dict() transforma os pares em um dicionário.
registro = dict(zip(campos, valores))

print("Registro:", registro)

# Eu crio um dicionário com informações padrão.
padrao = {
    "curso": "ADS",
    "semestre": 1,
    "ativo": True
}

# Eu crio um dicionário com informações adicionais.
extra = {
    "semestre": 4,
    "portfolio": "meu-portfolio.netlify.app"
}

# Eu mesclo os dicionários usando **.
# Se uma chave aparecer nos dois, o valor de extra prevalece.
completo = {**padrao, **extra}

print("Cadastro completo:", completo)

# Eu inverto as chaves e os valores de um dicionário.
# Os valores precisam ser únicos para que essa inversão faça sentido.
siglas = {
    "ADS": "Análise e Desenvolvimento de Sistemas",
    "TI": "Tecnologia da Informação"
}

invertido = {
    nome: sigla
    for sigla, nome in siglas.items()
}

print("Sigla encontrada:", invertido["Tecnologia da Informação"])  # TI