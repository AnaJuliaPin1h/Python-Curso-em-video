def moeda(n):
    if n - int(n) == 0:
        return f'R${int(n)},00'
    else:
        return f'R${int(n)},{int((n - int(n)) * 100)}'