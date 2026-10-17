# EXCEÇÕES AVANÇADAS EM PYTHON
# Todos os exemplos em um único arquivo


# EXEMPLO 1: HIERARQUIA DE EXCEÇÕES PERSONALIZADAS

# Eu crio uma classe base para agrupar os erros de cadastro.
class ErroDeCadastro(Exception):
    """Eu uso esta classe para agrupar erros de cadastro."""


# Esta exceção acontece quando um campo obrigatório está vazio.
class CampoObrigatorioError(ErroDeCadastro):
    def __init__(self, campo):
        self.campo = campo
        super().__init__(f"O campo '{campo}' é obrigatório.")


# Esta exceção acontece quando a idade é inválida.
class IdadeInvalidaError(ErroDeCadastro):
    def __init__(self, idade):
        self.idade = idade
        super().__init__(f"Idade inválida: {idade}")


def cadastrar(dados):
    if not dados.get("nome"):
        raise CampoObrigatorioError("nome")

    idade = dados.get("idade")

    if not isinstance(idade, int) or not 0 < idade < 130:
        raise IdadeInvalidaError(idade)

    return f"{dados['nome']} cadastrado(a) com sucesso."


registros = [
    {"nome": "Ana", "idade": 22},
    {"nome": "", "idade": 22},
    {"nome": "João", "idade": 200},
]

for registro in registros:
    try:
        print(cadastrar(registro))

    except CampoObrigatorioError as erro:
        # Eu trato especificamente o erro de campo obrigatório.
        print(f"Campo faltando: {erro.campo}")

    except ErroDeCadastro as erro:
        # Eu capturo outros erros da hierarquia de cadastro.
        print(f"Erro de cadastro: {erro}")


# EXEMPLO 2: ENCADEANDO EXCEÇÕES COM raise ... from

import json


class ConfiguracaoError(Exception):
    """Eu uso esta exceção para erros de configuração."""


def carregar_config(texto):
    try:
        return json.loads(texto)

    except json.JSONDecodeError as erro:
        # Eu lanço uma mensagem mais clara e preservo a causa original.
        raise ConfiguracaoError(
            "Arquivo de configuração malformado."
        ) from erro


try:
    # A vírgula final torna este JSON inválido.
    carregar_config('{"porta": 8080,}')

except ConfiguracaoError as erro:
    print(f"Mensagem: {erro}")
    print(f"Causa original: {erro.__cause__}")


# EXEMPLO 3: GERENCIADOR DE CONTEXTO COM LIMPEZA GARANTIDA

from contextlib import contextmanager


@contextmanager
def conexao_simulada(nome):
    print(f"Abrindo conexão com {nome}")

    try:
        # Eu entrego o recurso para o bloco "with".
        yield nome

    except Exception as erro:
        # Eu registro o erro e deixo ele continuar subindo.
        print(f"Erro dentro do bloco: {erro}")
        raise

    finally:
        # Eu fecho a conexão mesmo se acontecer um erro.
        print("Fechando conexão.")


try:
    with conexao_simulada("banco de dados") as conexao:
        print(f"Executando consulta em {conexao}")

        # Eu provoco um erro de propósito.
        resultado = 10 / 0

except ZeroDivisionError:
    print("O erro foi tratado do lado de fora do bloco.")


# EXEMPLO 4: RETENTATIVAS COM ESPERA EXPONENCIAL

import random
import time


class ServicoIndisponivel(Exception):
    pass


def chamar_api():
    # Eu simulo uma API que falha em aproximadamente 70% das chamadas.
    if random.random() < 0.7:
        raise ServicoIndisponivel("Timeout no servidor")

    return {"status": "ok"}


def com_retentativas(funcao, tentativas=4, espera_inicial=0.5):
    espera = espera_inicial

    for numero in range(1, tentativas + 1):
        try:
            # Se funcionar, eu retorno o resultado e encerro as tentativas.
            return funcao()

        except ServicoIndisponivel as erro:
            # Se for a última tentativa, deixo o erro subir.
            if numero == tentativas:
                raise

            print(
                f"Tentativa {numero} falhou ({erro}). "
                f"Espero {espera}s."
            )

            # Eu espero antes de tentar novamente.
            time.sleep(espera)

            # Eu dobro o tempo de espera a cada falha.
            espera *= 2


try:
    print(com_retentativas(chamar_api))

except ServicoIndisponivel:
    print("Desisti após todas as tentativas.")


# EXEMPLO 5: VÁRIOS ERROS COM ExceptionGroup E except*

# Este exemplo exige Python 3.11 ou superior.

def validar_notas(notas):
    erros = []

    for nota in notas:
        # Eu guardo um TypeError se a nota não for numérica.
        if not isinstance(nota, (int, float)):
            erros.append(TypeError(f"Nota não numérica: {nota!r}"))

        # Eu guardo um ValueError se a nota estiver fora do intervalo.
        elif not 0 <= nota <= 10:
            erros.append(ValueError(f"Nota fora do intervalo: {nota}"))

    if erros:
        # Eu agrupo os erros encontrados em uma única exceção.
        raise ExceptionGroup("Problemas nas notas", erros)

    return True


try:
    validar_notas([7, "oito", 11, 9])

except* TypeError as grupo:
    # Eu trato os erros de tipo que estiverem no grupo.
    print("Erros de tipo:", [str(erro) for erro in grupo.exceptions])

except* ValueError as grupo:
    # Eu trato os erros de valor que estiverem no grupo.
    print("Erros de valor:", [str(erro) for erro in grupo.exceptions])