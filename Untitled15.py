#Leia o valor da compra de um cliente.
#Sabendo que o ICMS é de 18%,
#calcule o valor do imposto e o valor total da compra (compra + imposto).

valor = float(input("Qual é o valor da compra: "))
icms =  18/100

imposto = valor * icms
total = valor + imposto

print(imposto)
print(total)