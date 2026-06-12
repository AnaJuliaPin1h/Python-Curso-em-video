# Classificando Atletas

from datetime import date

ano = int(input('Informe o seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print (f'Você tem {idade} anos. Sua categoria é: MIRIM.')
elif idade <= 14:
    print (f'Você tem {idade} anos. Sua categoria é: INFANTIL.')
elif idade <= 19:
    print (f'Você tem {idade} anos. Sua categoria é: JUNIOR.')
elif idade <= 25:
    print (f'Você tem {idade} anos. Sua categoria é: SÊNIOR.')
else:
    print (f'Você tem {idade} anos. Sua categoria é: MASTER.')