# Procurando uma string dentro de outra

nome = input('Digite o nome: ').upper()

if 'SILVA' in nome:                         # operador in verifica se existe dentro da string
    print('O nome TEM Silva.')
else:
    print('O nome NÃO tem Silva.')


# or
#nome = str(input("Qual é o seu nome completo: ")).strip()
#print("Seu nome tem SILVA? {}" .format ("silva" in nome.lower()))


# strip()  É um método
# É um método da classe string (str).
# Remove os espaços em branco do início E do fim da string.
# Muito útil para limpar o que o usuário digita com espaços acidentais.
# Exemplo:
# "  oi  ".strip() retorna "oi"