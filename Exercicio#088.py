from random import randint
from time import sleep

lista_jogos_totais = []
lista_temporaria = []

quant_jogos = int(input(f"Quantos jogos você quer que eu sorteie? "))

print("-="*3, end=" ")
print(f"SORTEANDO {quant_jogos} JOGOS", end=" ")
print("-="*3, end=" ")
print()
for j in range(0, quant_jogos):
    for s in range(6):
        numero_sorteado = randint(1, 60)
        if numero_sorteado not in lista_jogos_totais:
            lista_temporaria.append(numero_sorteado)

    lista_temporaria.sort()
    lista_jogos_totais.append(lista_temporaria[:])
    lista_temporaria.clear()
    print(f"Jogo {j+1}: {lista_jogos_totais[j]}")
    sleep(1)

print("-="*5, end=" ")
print("<", end=" ")
print("BOA SORTE!", end=" ")
print("<", end=" ")
print("-="*5, end=" ")
print()