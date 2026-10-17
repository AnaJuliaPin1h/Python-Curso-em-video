from random import randint
def sorteia():
    return [randint(1, 10) for _ in range(5)]
def somaPar(lst):
    soma = 0
    for l in lst:
        if l % 2 == 0:
            soma += l
    return soma
s = sorteia()
print(s)
print(somaPar(s))