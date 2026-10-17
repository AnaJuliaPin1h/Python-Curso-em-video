def leiaint(txt):
    while True:
        n = input(txt)
        if (n[0] == "-" and n[1:].isnumeric()) or n.isnumeric():
            n = int(n)
            return n
        else:
            print("\033[1;31mERRO! valor nao valido.\033[m")
            
n = leiaint("Digite um numero inteiro: ")
print(f"Você digitou o numero {n}")