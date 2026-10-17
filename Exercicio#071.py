n = int(input('Valor de saque R$'))
while True:
    if n // 50:
        print(f'Total de {n//50} cédulas de R$50')
        n -= (n//50 * 50)
    if n // 20:
        print(f'Total de {n//20} cédulas de R$20')
        n -= (n//20 * 20)
    if n // 10:
        print(f'Total de {n//10} cédulas de R$10')
        n -= (n//10 * 10)
    if n // 1:
        print(f'Total de {n} cédulas de R$1')
    break