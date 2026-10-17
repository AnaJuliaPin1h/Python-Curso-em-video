lista_numeros = []
while True:

    numero = int(input("Digite um Número:"))
    lista_numeros.append(numero)
    continuar = input("voê quer continuar? S/N").upper().strip()

    if continuar == "N":
        break

# A)
print(f"foram digitados {len(lista_numeros)} números.")
# B)
lista_numeros.sort(reverse= True)
print(f"A lista em ordem decrescente: {lista_numeros}")
# C)
if 5 in lista_numeros:
    print("O número 5 foi digitado e pertence à lista.")

else:
    print("O número 5 não foi digitado e não pertence à lista")