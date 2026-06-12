# Média

from time import sleep
print('Coloque as notas dos 4 trimestres para saber se você passou de ano.')
n1 = float(input('Primeiro nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
média = float(n1 + n2 + n3 + n4) / 4
print('Calculando...')
sleep(3)
if média >= 7.0:
    print('Parabéns, sua média foi {:.2f} e você passou de ano!'.format(média))
elif média >= 5.0 and média < 7.0:
    print('Sua média foi {:.2f}, sendo assim você está de recuperação!'.format(média))
else:
    print('Sua média foi {:.2f}, sendo assim você está reprovado, volte no proximo ano!'.format(média))