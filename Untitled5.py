# Criar um algoritmo que receba o salário de um funcionário
# e o percentual de aumento, calcule e mostre o valor do aumento
# e o novo salário.

salario_atual = float(input("Informe o seu salário atual: \n"))
aumento = float(input("Informe o percentual de aumento: \n"))

valor_aumento = salario_atual * (aumento / 100)

novo_salario = salario_atual + valor_aumento

print("\nValor do aumento:", valor_aumento)
print("Novo salário:", novo_salario)