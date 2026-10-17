def moeda(preco = 0, moeda ='R$', formatar = False):
    if formatar:
        return f'{moeda}{preco:.2f}'.replace('.', ',') 
    else:
        return preco