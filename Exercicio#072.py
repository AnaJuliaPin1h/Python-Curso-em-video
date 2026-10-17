numeros = (
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "catorze",
    "quinze", "dezesseis", "dezessete", "dezoito",
    "dezenove", "vinte"
)

while True:
    numero = int(input("Digite um numero entre 0 e 20 "))
    if 0 <= numero <= 20:
        print(f"Voce digitou o numero {numeros[numero]} ")
    else:
        print("Opção invalida digite um numero entre 0 e 20")
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar in "Nn":
        break
print(f"Fim do jogo")