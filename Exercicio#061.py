# v2 

print('!10 Primeiros Termos de uma Progressão Aritmética!')
print()

pa = 0
pt = int(input('Qual o Primeiro termo?: '))
r = int(input('Qual o a Razão?: '))
print()

while pa < 10:
    print (pt, '->',end=' ')
    pt = pt + r
    pa += 1

print()
print()
print('FIM', end=' ')