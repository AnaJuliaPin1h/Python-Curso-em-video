# Verificando as primeiras letras de um texto

cidade = input('Nome da cidade: ').upper()  # upper() garante a comparação independente de como o usuário digitou

if cidade[:5] == 'SANTO':                   # fatia as 5 primeiras letras
    print('A cidade COMEÇA com SANTO.')
else:
    print('A cidade NÃO começa com SANTO.')