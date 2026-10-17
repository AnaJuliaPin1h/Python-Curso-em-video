#Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada 
#metro quadrado, deve-se usar 18W de potência. Faça um algoritmo que receba as 
#duas dimensões de um cômodo (em metros). Calcule e mostre a sua área (em m2) 
#e a potência de iluminação que deverá ser utilizada. 

comprimento = float(input("Informe Comprimento do cômodo (em metros):  "))
largura = float(input("Informe a Largura do cômodo (em metros):  "))

#descobrir a area Calcular a área do cômodo
area = comprimento * largura

potencia = area * 18  # 18W por metro quadrado

print("Área do cômodo:", area, "m²")
print("Potência necessária:", potencia, "W")