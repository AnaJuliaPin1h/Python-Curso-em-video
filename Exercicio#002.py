# Faça um programa que leia o nome de uma pessoa
# e mostre uma mensagem de boas-vindas.

# Declaramos uma variável chamada "nome".
# Ela vai receber (=) o valor digitado pelo usuário no teclado.

# Para receber dados do usuário, utilizamos a função input().
# Essa função permite a entrada de dados pelo teclado.

# Podemos fazer a formatação da saída usando vírgula (,),
# concatenação (+) ou chaves {} com o método .format().

# Saída formatada utilizando chaves {}:
# Depois da string (mensagem), usamos .format(nome)
# para inserir o valor da variável dentro das chaves.

# Saída formatada utilizando f-string.
# A letra f antes das aspas permite colocar variáveis
# diretamente dentro da string usando chaves {}.
# Dentro das chaves colocamos o nome da variável.
# print(f"Olá {nome}, é um prazer te conhecer!")

nome = input("Me diga seu nome: ")
print('Olá {} é um prazer te conhecer'.format(nome));