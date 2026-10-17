valores = []
while True:
    v = int(input("Digite um valor:\n"))
    if v not in valores:
        print("Valor adicionado com sucesso…\n")
        valores.append(v)
    else:
        print("Valor duplicado! Não vou adicionar…")
    escolha = input("Quer continuar? [S/N]\n").lower().strip()
    if escolha == "s":
        continue
    else:
        print("-="*40)
        print(f"Você digitou os valores {sorted(valores)}")
        break