from random import randint
tupla = (randint(1,9), randint(1,9), randint(1,9), randint(1,9), randint(1,9))

print("Os números sorteados foram: ", end = " ")
for c in range(0, 5):
    print(tupla[c], end = " ")
    if c == 0:
        maior = tupla[c]
        menor = tupla[c]
    if tupla[c] > maior:
        maior = tupla[c]
    if tupla[c] < menor:
        menor = tupla[c]
print(f"""
O maior número sorteado foi {maior}""")
print(f"O menor número sorteado foi {menor}")