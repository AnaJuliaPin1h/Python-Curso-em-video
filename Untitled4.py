# Criar um algoritmo que leia o saldo de uma aplicação
# e imprima o novo saldo considerando um reajuste de 15%.

saldo_atual = float(input("Informe o seu saldo atual: "))

reajuste = 15 / 100

novo_saldo = saldo_atual + (saldo_atual * reajuste)

print("\nSeu saldo atual, considerando o reajuste, é:", novo_saldo)