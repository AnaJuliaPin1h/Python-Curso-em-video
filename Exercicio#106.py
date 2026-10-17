color = {
        'default' : '\033[m',
        'blue' : '\033[30;44m',
        'white': '\033[7;30m',
        'green' : '\033[30;42m',
        'red' : '\033[30;41m'
    }

def ajuda(cmd):
    esc(f'Acessando o manual do comando \'{cmd}\'', cor='blue')
    print(color['white'], end='')
    help(cmd)
    print(color['default'], end='')

def esc(cmd, cor='default'):
    print(color[cor], end='')
    print('~'*(len(cmd) + 4))
    print(cmd.center((len(cmd) + 4), ' '))
    print('~'*(len(cmd) + 4))
    print(color['default'], end='')

comando = ''
while True:
    esc('SISTEMA DE AJUDA PyHelp', cor='green')
    comando = input('Função ou biblioteca > ').strip().lower()
    if comando == 'fim':
        esc('Até logo!', cor='red')
        break
    ajuda(comando)