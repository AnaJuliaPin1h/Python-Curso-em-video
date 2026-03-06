a1 = input("Digite algo:")
print("O tipo primitivo deste valor é", type(a1))
print("Só tem espaços? ", a1.isspace())
print("É um numero?", a1.isnumeric())
print("É alfabeto?", a1.isalpha())
print("É alfanumérico?", a1.isalnum())
print("Está em maiúsculo?", a1.isupper())
print("Está em minúsculo?", a1.islower())
print("Está capitalizado?", a1.istitle())


#alfabetico - isalpha 
#numerico - isnumeric
#só tem espaços - isspace
#alfabético e numérico - isalnum
#está em maiúsculas - isupper
#está em minúculas - islower
#está só com a primeira letra em maiúsulas - istitle