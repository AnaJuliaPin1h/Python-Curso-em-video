# Aprovando Empréstimo
casa = float(input("Valor da casa: "))
salario = float(input("Salario do comprador: ")),
financiamento = int(input("Quantos anos de financiamento: "))

prestacao = casa / (financiamento * 12)
minimo = salario * 30/ 100

print("Para pagar uma casa de {} em {}".format(casa,financiamento))
print("Emprestimo pode ser concedido {}" .format(prestacao))

if prestacao <= minimo:
    print("Emprestimo pode ser concedido")
else:
    print("Emprestimo negado")