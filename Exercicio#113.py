def leiaint(msg):
    while True:
        try:
            print('\n\033[2;33m( Ctrl + C ) Para interromper.\033[m')
            val = int(input(msg))

        except Exception as erro:
            print(f'\033[31mO ERRO encontrado foi ( {erro.__class__.__name__} )\033[m')
            print('\033[31merro, digite valor numerico.\033[m')

        except KeyboardInterrupt:
            print(f'\n\nO usuario decidiu não enviar nada.')
            return 0
            
        else:
            print('\n\033[32mTudo Certo! INTEIRO CONFIRMADO!\033[m\n')
            return val



def leiafloat(msg):
    while True:
        try:
            print('\n\033[2;33m( Ctrl + C ) Para interromper.\033[m')
            val = float(input(msg))

        except Exception as erro:
            print(f'\033[31mO ERRO encontrado foi ( {erro.__class__.__name__} )\033[m')
            print('\033[31mErro, digite valor numerico\033[m')
            continue

        except KeyboardInterrupt:
            print(f'\n\nO usuario decidiu não enviar nada.')
            return 0

        else:
            print('\n\033[32mTudo Certo! REAL CONFIRMADO!\033[m\n')
            return val



n1 = leiaint('Digite um valor INTEIRO: ')
n2 = leiafloat('Digite um REAL: ')
print(f'\n\033[31mO valor INTEIRO foi {n1} e o valor REAL foi {n2}\033[m.\n')