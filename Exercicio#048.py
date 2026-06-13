# SOMA DOS NÚMEROS ÍMPARES MÚLTIPLOS DE 3

# soma -> guarda a soma dos valores encontrados
# cont -> conta quantos valores foram encontrados

soma = 0
cont = 0

for c in range(1, 501, 2):
    
    # Verifica se o número é múltiplo de 3
    if c % 3 == 0:
        soma += c
        cont += 1

print("A soma de todos os {} valores solicitados é {}"
      .format(cont, soma))