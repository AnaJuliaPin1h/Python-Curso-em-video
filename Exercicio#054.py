# Grupo da Maioridade

from datetime import date
maiores = []
menores = []
data_atual = date.today().year
for n in range (0, 7):
    pessoas = int(input('Insira o ano de nascimento da pessoa:\n'))
    if (data_atual-pessoas) >= 21:
        maiores.append(pessoas) 
    else:   
        menores.append(pessoas)

print(f'No total existem {len(maiores)} adultos')

print(f'No total existem {len(menores)} menores')