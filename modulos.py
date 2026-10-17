

# 1. IMPORTANDO MÓDULOS

# Importo o módulo math para usar funções matemáticas.
import math

# Importo o módulo random para gerar valores aleatórios.
import random

# Importo o módulo datetime para trabalhar com datas e horários.
import datetime

# Importo o módulo statistics para calcular média e outras estatísticas.
import statistics

# Uso math para calcular a raiz quadrada.
raiz = math.sqrt(25)
print("Raiz quadrada de 25:", raiz)

# Uso random para sortear um número entre 1 e 10.
numero_sorteado = random.randint(1, 10)
print("Número sorteado:", numero_sorteado)

# Uso datetime para mostrar a data e o horário atuais.
agora = datetime.datetime.now()
print("Data e horário atuais:", agora)

# Uso statistics para calcular a média de uma lista.
notas = [7, 8, 9, 10]
media = statistics.mean(notas)
print("Média das notas:", media)


# 2. IMPORTANDO UMA FUNÇÃO ESPECÍFICA

# Em vez de importar o módulo inteiro, posso importar apenas
# a função que quero utilizar.
from math import sqrt

# Agora posso chamar sqrt() diretamente, sem escrever math.sqrt().
print("Raiz quadrada de 36:", sqrt(36))


# 3. USANDO ALIAS (APELIDO) PARA UM MÓDULO


# Posso dar um apelido ao módulo para escrever menos.
import datetime as dt

# Uso o apelido dt para acessar a data atual.
data_atual = dt.date.today()
print("Data de hoje:", data_atual)


# 4. CRIANDO E USANDO FUNÇÕES

# Esta função calcula a média de uma lista de notas.
def calcular_media(lista_notas):
    # Somo todas as notas e divido pela quantidade.
    return sum(lista_notas) / len(lista_notas)


# Esta função verifica se o aluno foi aprovado.
def verificar_situacao(media):
    # Se a média for maior ou igual a 7, o aluno está aprovado.
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


# Testo as funções.
notas_aluno = [8, 7, 9]
media_aluno = calcular_media(notas_aluno)

print("Média do aluno:", media_aluno)
print("Situação:", verificar_situacao(media_aluno))


# 5. SIMULANDO UM PACOTE COM FUNÇÕES


# Em um projeto real, essas funções poderiam estar distribuídas
# em módulos dentro de uma pasta de pacote.
#
# Aqui, para manter tudo em um único arquivo, defino as funções
# diretamente neste script.

def somar(a, b):
    # Retorno a soma dos dois valores.
    return a + b


def subtrair(a, b):
    # Retorno a diferença entre os dois valores.
    return a - b


def multiplicar(a, b):
    # Retorno o produto dos dois valores.
    return a * b


def dividir(a, b):
    # Verifico se o divisor é zero para evitar erro.
    if b == 0:
        return "Não é possível dividir por zero."

    return a / b


# Uso as funções como se fossem ferramentas de um pacote.
print("Soma:", somar(10, 5))
print("Subtração:", subtrair(10, 5))
print("Multiplicação:", multiplicar(10, 5))
print("Divisão:", dividir(10, 5))


# 6. __name__ == "__main__"


# A variável especial __name__ indica como o arquivo está sendo usado.
#
# Quando executo este arquivo diretamente, __name__ recebe "__main__".
# Quando o arquivo é importado por outro módulo, __name__ recebe
# o nome do módulo.

if __name__ == "__main__":
    # Este trecho só será executado quando eu rodar este arquivo
    # diretamente, e não quando ele for importado.
    print("O arquivo está sendo executado diretamente.")


# 7. SIMULANDO __all__


# Em módulos reais, __all__ define quais nomes serão importados
# quando alguém usar: from modulo import *
#
# Como este exemplo está em um único arquivo, apenas mostro
# como a variável é definida.

__all__ = ["somar", "subtrair", "multiplicar", "dividir"]

print("Nomes definidos em __all__:", __all__)


# 8. INSPECIONANDO O MÓDULO ATUAL


# __file__ informa o caminho do arquivo Python atual.
print("Caminho deste arquivo:", __file__)

# __package__ informa o pacote ao qual o módulo pertence.
# Em um script executado diretamente, normalmente será None
# ou uma string vazia.
print("Pacote deste módulo:", __package__)


# 9. IMPORTAÇÃO DINÂMICA COM importlib


# O módulo importlib permite importar módulos pelo nome,
# durante a execução do programa.
import importlib

# Importo o módulo math usando seu nome como texto.
modulo_matematica = importlib.import_module("math")

# Acesso à função sqrt() por meio do módulo importado.
print(
    "Raiz quadrada usando importlib:",
    modulo_matematica.sqrt(49)
)


# 10. CONSULTANDO MÓDULOS CARREGADOS

# O módulo sys permite acessar informações do interpretador Python.
import sys

# sys.modules guarda os módulos que já foram carregados.
if "math" in sys.modules:
    print("O módulo math já está carregado.")



# 11. CONSULTANDO E ALTERANDO sys.path


# sys.path contém os caminhos em que Python procura módulos.
print("Caminhos de busca dos módulos:")
for caminho in sys.path:
    print(caminho)

# Posso acrescentar um caminho à lista de busca.
# Em um projeto real, esse caminho seria a pasta onde está
# o módulo que quero importar.
#
# Exemplo:
# sys.path.append("C:/meu_projeto/meus_modulos")


# 12. EXEMPLO DE IMPORTAÇÃO RELATIVA



# Em um pacote real, uma importação relativa pode ser escrita assim:
#
# from .modulo import funcao
#
# O ponto (.) indica o pacote atual.
#
# Dois pontos (..) indicam o pacote pai:
#
# from ..outro_modulo import funcao
#
# Essas importações dependem da estrutura real de pastas e do
# contexto em que o módulo é executado. Por isso, não funcionam
# como importações relativas comuns em um script isolado.


# 13. EXEMPLO DE IMPORTAÇÃO CIRCULAR


# Uma importação circular acontece quando:
#
# modulo_a importa modulo_b
# e modulo_b importa modulo_a.
#
# Isso pode causar erros porque um dos módulos pode ainda estar
# sendo inicializado quando o outro tenta utilizá-lo.
#
# Para evitar esse problema, posso:
# 1. Reorganizar as funções e classes em um terceiro módulo.
# 2. Evitar que módulos dependam diretamente uns dos outros.
# 3. Fazer uma importação dentro da função, quando apropriado.
#
# Exemplo de importação local:
#
# def usar_recurso():
#     import outro_modulo
#     return outro_modulo.recurso()
#
# O exemplo acima é apenas ilustrativo. Para funcionar, o módulo
# outro_modulo precisa existir e estar acessível ao Python.


# 14. RESUMO

# Módulo:
# Um arquivo Python que contém funções, classes ou variáveis.
#
# Pacote:
# Uma pasta que organiza módulos relacionados.
#
# import:
# Permite utilizar recursos de outro módulo.
#
# importlib:
# Permite importar módulos dinamicamente.
#
# __name__:
# Indica o nome pelo qual o módulo está sendo executado.
#
# __main__:
# É o valor de __name__ quando o arquivo é executado diretamente.
#
# __all__:
# Define os nomes exportados em uma importação com *.
#
# sys.path:
# Lista os caminhos em que Python procura módulos.
#
# Importação circular:
# Acontece quando módulos importam uns aos outros, direta ou
# indiretamente.