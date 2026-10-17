#Dados o tamanho de um arquivo (em bits), bem como a velocidade da conexão (em bits 
#por segundo), informe o tempo necessário para o download do arquivo.


# Entrada
tamanho_arquivo = int(input("Digite o tamanho do arquivo (bits): "))
velocidade = int(input("Digite a velocidade da conexão (bits por segundo): "))

# Processamento
tempo = tamanho_arquivo / velocidade

# Saída
print("Tempo necessário para o download:", tempo, "segundos")