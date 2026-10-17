def metade(num=0, moeda=False):
    """
    Retorna a metade do valor "num"
    :param num: o número a ser reduzido pela metade
    :param moeda: define se o valor será formatado para moedas
    :return: retorna um float igual à metade do valor num, com 2 casas decimais
    """
    num = float(num/2)
    if moeda:
        num = f'R${num:.2f}'.replace(".", ",")
    return num


def dobro(num=0, moeda=False):
    """
    Retorna o dobro do valor "num"
    :param num: o valor a ser dobrado
    :param moeda: define se o valor será formatado para moedas
    :return: retorna um float igual à metade do valor num, com 2 casas decimais
    """
    num = float(num*2)
    if moeda:
        num = f'R${num:.2f}'.replace(".", ",")
    return num


def aumentar(num=0, x=0, moeda=False):
    """
    Retorna o valor num + x%
    :param num: o valor inicial
    :param x: a porcentagem do aumento de num
    :param moeda: define se o valor será formatado para moedas
    :return: retorna um float igual a num *= x%
    """
    total = num + (num * x/100)
    if moeda:
        total = f'R${total:.2f}'.replace(".", ",")
    return total


def diminuir(num=0, x=0, moeda=False):
    """
    Retorna o valor num - x%
    :param num: o valor inicial
    :param x: a porcentagem de diminuição de num
    :param moeda: define se o valor será formatado para moedas
    :return: retorna um float igual a num / x%
    """
    total = num - (num * x/100)
    if moeda:
        total = f'R${total:.2f}'.replace(".", ",")
    return total


def moedas(valor=0):
    """
    Formata o valor em estilo monetário de reais
    :param valor: o valor em reais a ser formatado
    :return: Retorna o valor com R$ antes, e com duas casas decimais
    """
    final = f'R${valor:.2f}'.replace(".", ",")
    return final


def resumo(preco=0, aumento=0, diminuicao=0):
    """
    Mostra um resumo com cabeçalho, mostrando o dobro, metade, aumento e redução parametrizados
    :param preco: valor inicial a ser analisado
    :param aumento: porcentagem de aumento na função aumentar()
    :param diminuicao: porcentagem de redução na função diminuir()
    :return: retorna um cabeçalho com as alterações do valor com base no número do input inicial
    """
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:"}{moedas(preco):>14}')
    print(f'{"Dobro do preço:"}{dobro(preco, True):>15}')
    print(f'{"Metade do preço:"}{metade(preco, True):>14}')
    print(f'{aumento:<2}% de aumento:{aumentar(preco, aumento, True):>15}')
    print(f'{diminuicao:<2}% de redução:{diminuir(preco, diminuicao, True):>15}')
    print('-'*30)



from modulos.ex111_utilidades_cev.moeda.moedas import * # type: ignore

p = float(input('Digite um preço: R$'))
resumo(p, 30, 50)