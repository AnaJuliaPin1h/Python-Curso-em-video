#Criar um algoritmo que converta segundos em minutos e segundos. Por exemplo, 252 
#segundos equivalem a 4 minutos e 12 segundos. 


# Entrada de dados
segundos = int(input("Digite a quantidade de segundos: "))

#Processamento
minutos = segundos // 60
segundos_restantes = segundos % 60

print(minutos, "minutos e", segundos_restantes, "segundos")