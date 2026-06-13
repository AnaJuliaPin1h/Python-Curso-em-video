
#TAbuada

print('BEM VINDO(A) A TABUADA')
print('-='*15)
n = int(input('Escolha um número de 1 até 10: '))
for c in range (1, 11):
    m = c * n
    print ('{} * {} = {} '.format(n, c, m))