#Criar um algoritmo que calcule o consumo médio de um automóvel (medido em km/l), 
#dado que são conhecidos a distância total percorrida e o volume de combustível 
#consumido para percorrê-la (medido em litros). 

distância_total_percorrida = float(input("Informe a quilometragem percorrida pelo veículo:  "))
combustivel_gasto = float(input("Informe a quantidade de combustível consumida durante o percurso:  "))


consumo_medio = distância_total_percorrida / combustivel_gasto
print("O consumo medio foi de" , consumo_medio)