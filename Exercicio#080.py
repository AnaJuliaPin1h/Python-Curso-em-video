val = []

for i in range(5):
    va = int(input(f'Digite o {i + 1}º valor: '))
    if not val or va > max(val):
        val.append(va)
        print('Adicionado no final da lista...')
    else:  
        for j, v in enumerate(val):
            if va < v:
                val.insert(j, va)
                print(f'Adicionado na {j + 1}ª posição da lista...')
                break

print(val)