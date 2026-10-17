def verpessoas():
    try:
        with open('cadastro.txt', 'r') as cadastro:
            pessoas = cadastro.read()
            print(pessoas)
    except FileNotFoundError:
        print('Não há pessoas cadastradas!')


def cadastrar():
    with open('cadastro.txt', 'a') as cadastro:
        nome = input('Nome: ').strip().title()
        idade = int(input('Idade: '))
        cadastro.write(f'{nome:<30}{idade:>8} anos\n')