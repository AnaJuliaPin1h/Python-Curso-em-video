#Aumentos múltiplos

salário = float(input("Qual é o salario do funcionario:  "))
if salário > 1250:
    novo = salário + salário * 10/100
else:
    salário <= 1250
    novo = salário + salário * 15/100


print("Quem ganhava R${:.2f} a partir de agora passa a ganhar {:.2f} agora" .format(salário, novo))

#control com a tecla ;:,  faz comentario