# Peso do saco de ração em kg
racao_peso = float(input("Peso do saco de ração (kg): "))

# Quantidade de ração para cada gato em gramas
gato1 = float(input("Quantidade de ração do gato 1 (g): "))
gato2 = float(input("Quantidade de ração do gato 2 (g): "))

# Converter o peso do saco para gramas
racao_peso_gramas = racao_peso * 1000

# Consumo diário dos dois gatos
consumo_dia = gato1 + gato2

# Consumo em 5 dias
consumo_5_dias = consumo_dia * 5

# Quantidade restante
restante = racao_peso_gramas - consumo_5_dias

print("Restará", restante, "gramas de ração após 5 dias.")