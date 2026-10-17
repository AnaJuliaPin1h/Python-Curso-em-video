def voto():
    from datetime import date
    idade = date.today().year - nasc
    print(f'Com {idade} anos: ', end='')
    if 65 > idade >= 18:
        print('VOTO OBRIGATÓRIO.')
    elif idade > 65:
        print('VOTO OPCIONAL.')
    else:
        print('NÃO VOTA.')


nasc = int(input('Em que ano você nasceu? '))
voto()