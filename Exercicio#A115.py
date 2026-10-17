from pasta import menu

menu()


def linha(msg):
    print('-' * 50)
    print(f'{msg}')
    print('-' * 50)

def inteiro(num):
    while True:
        try:
            valor = int(input(num))
        except (TypeError, ValueError):
            print('\033[31m Erro, tente de novo. \033[m')
        except (KeyboardInterrupt):
            print('\033[31m Usuário não quis digitar. \033[m')
            return 0
        else:
            return valor
            
def menu():
    from time import sleep
    while True:
        linha(f'{"Menu Principal":>32}')
        print('\033[33m1 - \033[32mVer pessoas cadastradas')
        print('\033[33m2 - \033[32mCadastrar nova Pessoa')
        print('\033[33m3 - \033[32mSair do Sistema \033[m')
        print('-' * 50)

        opcao = inteiro('\033[36mDigite a sua opção: \033[m')
        if opcao <= 0 or opcao > 3:
            print('Erro')
        elif opcao == 1:
            linha(f'{"Opção 1":>28}')
        elif opcao == 2:
            linha(f'{"Opção 2":>28}') 
        else:
            print('Saindo do Programa...')
            sleep(1)
            print('Volte Sempre !')
            exit()