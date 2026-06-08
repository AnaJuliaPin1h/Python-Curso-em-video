# Radar eletrônico contínuo
print("--- SISTEMA DE RADAR ELETRÔNICO ---")

while True:
    entrada = input("\nDigite a velocidade ou 'sair' para encerrar: ")
    
    # Condição de parada do loop
    if entrada.lower() == 'sair':     #O comando .lower() permite que o usuário digite "SAIR", "Sair" ou "sair" para fechar o programa
        print("Sistema encerrado.")
        break
        
    # Conversão do valor digitado para número
    velo = float(entrada)
    
    # Verificação da velocidade
    if velo > 80:
        print("> MULTADO < Você ultrapassou o limite de 80km/h!")
        
        # Calcula a multa APENAS sobre o que passou do limite
        excesso = velo - 80
        multa = excesso * 7
        
        print(f"Velocidade excedida: {excesso:.1f} km/h")
        print(f"Você deve pagar uma multa de R$ {multa:.2f}")
    else:
        print("Dirija com segurança!!!")