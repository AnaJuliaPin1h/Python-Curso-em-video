from time import sleep

aberto = []
fechado = []

expressao = str(input("Informe uma expressão algébrica: "))

for i in range(0, len(expressao)): #esse laço vai ler parte por parte da expressão
    if "(" in expressao[i]: #se encontrar o parenteses aberto vai colocar na lista "aberto"
        aberto.append(expressao[i])
    elif ")" in expressao[i]: #se encontrar o parenteses fechado vai colocar na lista de "fechado"
        fechado.append(expressao[i])

print("Verificando...")
sleep(1)

if len(aberto) - len(fechado) == 0: #vai subtrair os números da lista "aberto" e "fechado". Se der zero, a expressão está completa
    print("A expressão informada está COMPLETA!")
else:
    print("A expressão informada está INCOMPLETA!")