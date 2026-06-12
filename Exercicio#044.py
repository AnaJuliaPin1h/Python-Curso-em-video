# Gerenciador de Pagamentos


preço = float(input('Digite o valor das compras: '))

ad = preço - (10/100*preço)
ac = preço - (5/100*preço)
c2x = preço
c3x = preço + (20/100*preço)

print('''Suas opções de pagamento:
[ 1 ] À vista dinheiro/cheque (10% de desconto)
[ 2 ] À vista cartão (5% de desconto)
[ 3 ] 2x cartão 
[ 4 ] 3x cartão (20% de juros)
''')

choose = int(input('Sua escolha: '))

if choose == 1:
    print('Valor final: R${:.2f}'.format(ad))
elif choose == 2:
    print('Valor final: R${:.2f}'.format(ac))
elif choose == 3:
    print('Valor final: R${:.2f}'.format(c2x))
elif choose == 4:
    print('Valor final: R${:.2f}'.format(c3x))