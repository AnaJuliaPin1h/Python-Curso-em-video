print('{:^40}'.format('Scaner de compras!'))
print('-=' * 20)
preco = total = mais_1000 = preco_baixo = 0
artigo_barato = ''
while True:
    artigo = str(input('Nome do artigo: ')).strip().title()
    preco = float(input('Preço do artigo: '))
    total += preco
    print('-' * 20)

    if preco > 1000:
        mais_1000 += 1
    if preco_baixo == 0 or preco < preco_baixo:
        preco_baixo = preco
        artigo_barato = artigo
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Continuar a ler? [S/N] ')).strip().upper()[0]
    print('-' * 20)

    if resposta in 'N':
        break

print('-=' * 20)
print(f'O total da compra foi {total:.2f}€')
print(f'Foram lidos {mais_1000} artigos acima de 1000€')
print(f'O artigo {artigo_barato} foi o mais barato e custou {preco_baixo:.2f}€')