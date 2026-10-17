def aumentar(p, t, formato=False):
    return p * (1 + t / 100) if not formato else moeda(p * (1 + t / 100))


def diminuir(p, t, formato=False):
    return p * (1 - t / 100) if not formato else moeda(p * (1 - t / 100))


def dobro(p, formato=False):
    return p * 2 if not formato else moeda(p * 2)  # not format == not True


def metade(p, formato=False):
    return p / 2 if formato is not True else moeda(p / 2)


def moeda(p):
    return f'R${p:.2f}'.replace('.', ',')


def resumo(p, a, r):
    titulo('RESUMO DO VALOR')
    print(f'Valor analisado: \t{moeda(p)}')
    print(f'Dobro do valor: \t{dobro(p, True)}')
    print(f'Dobro do valor: \t{metade(p, True)}')
    print(f'{a}% de aumento: \t{aumentar(p, a, True)}')
    print(f'{r}% de redução: \t{diminuir(p, r, True)}')
    rodape('RESUMO DO VALOR')
    return


def titulo(txt):
    print('*' * (len(txt ) +20))
    print(f'{txt:^{(len(txt)+20)}}')
    print('*' * (len(txt ) +20))


def rodape(tit):
    print('*' * (len(tit) + 20))