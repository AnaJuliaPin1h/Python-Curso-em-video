# Maior e menor valores

num1 = float(input("Primeiro valor: "))
num2 = float(input("Segundo valor: "))
num3 = float(input("Terceiro valor: "))

menor = min(num1, num2, num3)     #funçao min
maior = max(num1, num2, num3)     #funçao max

print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))