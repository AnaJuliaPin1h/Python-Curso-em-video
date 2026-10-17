#João recebeu seu salário e precisa pagar duas contas que estão atrasadas. Como as 
#contas estão atrasadas, João terá que pagar multa de 2% sobre cada conta. Faça 
#um algoritmo que calcule e mostre quanto restará do salário do João

salario = float(input("Digite seu salario: "))
conta1 = float(input("Digite o valor da primeira conta: "))
conta2 = float(input("Digite o valor da segunda conta: "))

conta1_multa = conta1 + (conta1 * 0.02)

conta2_multa = conta2 + (conta2 * 0.02)

total_contas = conta1_multa + conta2_multa

salario_restante = salario - total_contas
print(salario_restante)