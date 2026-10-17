def cadastro():

    titulo("NOVO CADASTRO")

    with open("pessoas.txt", "a") as arquivo:

        while True:
                nome = input("Digite o nome: ")

                if nome.isnumeric():
                    print("Nome inválido")
                else:
                    break

        while True:
            try:
                idade = int(input("Digite a idade: "))
            except:
                print("Favor digitar uma idade válida.")
            else:
                arquivo.write(f"{nome};{idade}\n")
                break

def listar():

    titulo("PESSOAS CADASTRADAS")

    with open("pessoas.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            nome, idade = linha.split(";")
            print(f"{nome:<20}{idade:>5} anos")

def sair():

    titulo("PROGRAMA ENCERRADO")

def titulo(msg):
    print("="*30)
    print(f"{msg}".center(30))
    print("="*30)


import sistema as sys

sys.titulo("SISTEMA DE CADASTRO")

while True:
    try:
        print("1 - Mostrar lista.\n"
                        "2 - Cadastrar novo usuário.\n"
                        "3 - Encerrar programa.")
        sys.titulo("~")
        opc = int(input("Digite a opção desejada: "))
        sys.titulo("~")
    except ValueError:
        print("Favor digitar um número válido.")

    else:
        if opc == 1:
            sys.listar()
            sys.titulo("~")
            continue
        elif opc == 2:
            sys.cadastro()
            sys.titulo("~")
            continue
        elif opc == 3:
            sys.sair()
            break
        else:
            print("Opção inválida")
            continue