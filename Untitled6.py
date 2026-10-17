# Criar um algoritmo que receba o ano de nascimento de uma pessoa
# e o ano atual, calcule e mostre:
# - A idade desta pessoa hoje
# - A idade desta pessoa em 2030

nascimento = int(input("Informe seu ano de nascimento: "))
atual_ano = int(input("Informe o ano atual: "))

idade_atual = atual_ano - nascimento
idade_2030 = 2030 - nascimento

print("Idade atual:", idade_atual)
print("Idade em 2030:", idade_2030)