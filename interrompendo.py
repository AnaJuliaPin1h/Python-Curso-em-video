# EXEMPLOS DE WHILE, BREAK E CONTINUE
#
# Neste arquivo, eu estudo quatro situações:
#
# 1. Menu interativo com break e continue.
# 2. Busca de números primos.
# 3. Processamento de notas com continue e else.
# 4. Busca de um número em uma matriz com while aninhado.
#
# Eu uso a variável executar_exemplo para escolher qual exemplo
# será executado. Assim, consigo estudar tudo no mesmo arquivo.


# Eu escolho o exemplo que quero executar:
# 1 = Menu interativo
# 2 = Números primos
# 3 = Processamento de notas
# 4 = Busca em matriz

executar_exemplo = 1


# EXEMPLO 1 — MENU INTERATIVO COM BREAK E CONTINUE

if executar_exemplo == 1:

    # Eu crio uma variável para armazenar o saldo inicial.
    saldo = 1000.00

    # Eu uso while True para manter o menu funcionando.
    # Como a condição é sempre verdadeira, preciso de break
    # para encerrar o laço.
    while True:

        # Eu mostro as opções disponíveis.
        print("\n=== MENU BANCÁRIO ===")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("0 - Sair")

        # Eu recebo a opção digitada.
        # strip() remove espaços extras do começo e do final.
        opcao = input("Escolha uma opção: ").strip()

        # Eu verifico se a opção digitada é válida.
        if opcao not in ("0", "1", "2", "3"):

            print("Opção inválida. Tente novamente.")

            # Eu pulo o restante desta repetição
            # e volto para o início do menu.
            continue

        # Eu verifico se o usuário deseja sair.
        if opcao == "0":

            print("Encerrando o programa...")

            # Eu interrompo o while True.
            break

        # Eu verifico se o usuário quer consultar o saldo.
        if opcao == "1":

            # Eu mostro o saldo com duas casas decimais.
            print(f"Saldo: R$ {saldo:.2f}")

            # Eu volto ao menu sem pedir um valor.
            continue

        # Eu peço o valor para depósito ou saque.
        try:

            # Eu converto o texto digitado para float.
            valor = float(input("Digite o valor: "))

        except ValueError:

            # Se a conversão falhar, eu aviso o usuário.
            print("Digite um valor numérico válido.")

            # Eu retorno ao menu para tentar novamente.
            continue

        # Eu verifico se o valor é positivo.
        if valor <= 0:

            print("O valor precisa ser maior que zero.")

            # Eu ignoro essa operação e volto ao menu.
            continue

        # Eu verifico se a opção foi depósito.
        if opcao == "2":

            # Eu adiciono o valor ao saldo.
            saldo += valor

            print("Depósito realizado!")

        # Se a opção foi 3, eu realizo a operação de saque.
        elif opcao == "3":

            # Eu verifico se existe saldo suficiente.
            if valor > saldo:

                print("Saldo insuficiente.")

            else:

                # Eu retiro o valor do saldo.
                saldo -= valor

                print("Saque realizado!")


# EXEMPLO 2 — BUSCA DE NÚMEROS PRIMOS COM WHILE

elif executar_exemplo == 2:

    # Eu crio uma função para verificar se um número é primo.
    def eh_primo(n):

        # Números menores que 2 não são primos.
        if n < 2:
            return False

        # Eu começo procurando divisores a partir do número 2.
        divisor = 2

        # Eu testo os divisores até a raiz quadrada de n.
        # Se divisor * divisor ultrapassar n, posso parar.
        while divisor * divisor <= n:

            # O operador % retorna o resto da divisão.
            # Se o resto for zero, encontrei um divisor.
            if n % divisor == 0:

                # Eu retorno False porque n não é primo.
                return False

            # Eu aumento o divisor para testar o próximo número.
            divisor += 1

        # Se nenhum divisor foi encontrado, n é primo.
        return True

    # Eu crio uma lista vazia para guardar os números primos.
    primos = []

    # Eu começo a busca pelo número 1.
    candidato = 1

    # Eu procuro números primos até 50.
    while candidato <= 50:

        # Eu verifico se o candidato é primo.
        if eh_primo(candidato):

            # Se for primo, eu adiciono à lista.
            primos.append(candidato)

        # Eu avanço para o próximo candidato.
        candidato += 1

    # Eu mostro os números primos encontrados.
    print("Números primos até 50:", primos)


# EXEMPLO 3 — PROCESSAMENTO DE NOTAS COM CONTINUE E ELSE

elif executar_exemplo == 3:

    # Eu crio uma lista que contém notas e valores inválidos.
    notas = [8.5, -3, 7.0, "abc", 10, 12, 6.5, 9.0]

    # Eu começo pelo primeiro elemento da lista.
    indice = 0

    # Eu crio uma variável para somar as notas válidas.
    soma = 0

    # Eu conto quantas notas válidas foram encontradas.
    validas = 0

    # Eu percorro a lista enquanto houver elementos.
    while indice < len(notas):

        # Eu pego a nota que está na posição atual.
        nota = notas[indice]

        # Eu avanço o índice antes das validações.
        # Isso evita repetir a mesma nota quando uso continue.
        indice += 1

        # Eu verifico se a nota é um número.
        if not isinstance(nota, (int, float)):

            print(f"Nota ignorada: {nota} não é um número.")

            # Eu pulo para a próxima nota.
            continue

        # Eu verifico se a nota está entre 0 e 10.
        if not 0 <= nota <= 10:

            print(f"Nota ignorada: {nota} está fora do intervalo.")

            # Eu não somo essa nota.
            continue

        # Se a nota passou pelas validações,
        # eu adiciono seu valor à soma.
        soma += nota

        # Eu aumento a quantidade de notas válidas.
        validas += 1

    else:

        # Este else é executado quando o while termina
        # normalmente, sem ser interrompido por break.
        print("Terminei de percorrer todas as notas.")

    # Eu verifico se encontrei alguma nota válida.
    if validas > 0:

        # Eu calculo a média das notas válidas.
        media = soma / validas

        # Eu mostro a média com duas casas decimais.
        print(f"Média das notas válidas: {media:.2f}")

    else:

        # Eu evito dividir por zero se nenhuma nota for válida.
        print("Não existem notas válidas para calcular a média.")


# EXEMPLO 4 — BUSCA EM MATRIZ COM WHILE ANINHADO

elif executar_exemplo == 4:

    # Eu crio uma matriz com três linhas e três colunas.
    matriz = [
        [3, 8, 1],
        [7, 42, 5],
        [9, 2, 6]
    ]

    # Eu defino o número que quero encontrar.
    alvo = 42

    # Eu começo pela primeira linha.
    linha = 0

    # Eu crio uma flag para indicar se encontrei o número.
    # False significa que ainda não encontrei.
    encontrado = False

    # Eu percorro as linhas enquanto existirem linhas
    # e enquanto o número ainda não tiver sido encontrado.
    while linha < len(matriz) and not encontrado:

        # Eu começo pela primeira coluna da linha atual.
        coluna = 0

        # Eu percorro as colunas da linha atual.
        while coluna < len(matriz[linha]):

            # Eu comparo o elemento atual com o alvo.
            if matriz[linha][coluna] == alvo:

                # Eu mostro a posição em que encontrei o número.
                print(
                    f"Encontrei {alvo} no índice "
                    f"[{linha}][{coluna}]."
                )

                # Eu altero a flag para indicar que encontrei.
                encontrado = True

                # Eu interrompo somente o while das colunas.
                break

            # Se não encontrei o número, avanço a coluna.
            coluna += 1

        # Eu avanço para a próxima linha.
        # Se encontrado for True, o while externo termina
        # na próxima verificação da condição.
        linha += 1

    # Eu verifico se a busca terminou sem encontrar o alvo.
    if not encontrado:

        print(f"Não encontrei o número {alvo} na matriz.")


# VALIDAÇÃO DA ESCOLHA DO EXEMPLO

else:

    # Se eu escolher um número diferente de 1, 2, 3 ou 4,
    # o programa informa que a escolha não é válida.
    print("Escolha um exemplo entre 1 e 4.")