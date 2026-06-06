#Aluguel de Carros

dias = int(input("Quantos dias alugados: "))
km = float(input("Quantos Km rodados: "))

pago = (dias * 60) + (km * 0.15)

print(f"Total a pagar: R$ {pago:.2f}")

#dias * 60 → calcula o custo pelos dias alugados (R$ 60 por dia).
#km * 0.15 → calcula o custo pelos quilômetros rodados (R$ 0,15 por km).