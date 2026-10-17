idade_cont = homen_mais = mulher_mais = 0 # variaveis recebendo 0
while True:
    print('=+=+' * 9)
    sexo = ' '                           #fica vazio por ser uma variavel dentro de um while
    while sexo not in 'MF':              #enquanto sexo não estiver em 'MF' repita a função
        sexo = str(input('Qual o sexo? [M/f]: ')).strip().upper()[0]
    idade = int(input('Qual a sua idade?: '))
    continuar = ' '                      #fica vazio por ser uma variavel dentro de um while
    while continuar not in 'SN':         #enquanto sexo não estiver em 'SN' repita a função
        continuar = str(input('Quer continuar?: [S/N]: ')).strip().upper()[0]
    if idade >= 18:                      #se idade for maior igual a 18 cont mais 1
        idade_cont += 1
    if sexo == 'M':                      #se sexo == 'M' cont mais 1
        homen_mais += 1
    if sexo == 'F' and idade < 20:       #se sexo for igual a 'F' e idade menor que 20 cont mais 1
        mulher_mais += 1
    if continuar == 'N':
        break
print('=+=+' * 9)
print(f'>>>Temos {idade_cont} pessoas maiores de 18 anos.')
print(f'>>Tivemos {homen_mais} homens cadastrados!.')
print(f'>Foram cadastradas {mulher_mais} mulheres menores de 20 anos.')
print('<<<Acabou>>>')