from random import randint
from time import sleep
jogadores = {}
lista = []
for j in range(1, 5):
    jogadores["nome"] = input(f"jogador {j}, Digite seu nome: ").strip().title()
    jogadores["dado"] = randint(1,20)
    sleep(1)
    print(f"Jogador {j} tirou {jogadores["dado"]}")
    lista.append(jogadores.copy())
lista.sort(reverse = True, key = lambda jogador: jogador["dado"])
print("\nRanking dos jogadores:")
for n, jogador in enumerate(lista, start = 1):
    sleep(1)
    print(f"{n}° jogador: {jogador['nome']} com {jogador["dado"]}")
print(f"{"fim":=^20}")