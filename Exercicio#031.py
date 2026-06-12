#Custo da Viagem

distancia = float(input("Qual é a distancia da sua viagem: "))

print("Voce esta prestes a começar uma viagem de {} Km" .format(distancia))

porkm_50 = distancia * 0.50

porkm_45 = distancia * 0.45

if distancia <= 200:
    porkm_50 = print("E o preço da passagem será de {}" .format(porkm_50))

elif distancia >= 200:
    porkm_45 = print("E o preço da passagem será de {}" .format(porkm_45))

#print("E o preço da passagem será de {}" .format(porkm))