from time import sleep
def contador(ini: int, fim: int, passo: int = 1):
    passo *= -1 if ini > fim or passo < 0 else 1
    fim = fim - 1 if ini > fim else fim + 1
    for c in range(ini, fim, passo):
        print(c, end=', ', flush=True)
        sleep(0.15)
    print()

contador(1, 10)
contador(10, 0, 2)
contador(5, 55, -8)
contador(-55, 0, 10)