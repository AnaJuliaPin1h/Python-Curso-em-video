#Faça um algoritmo que receba o custo de um espetáculo teatral e o preço do 
#convite deste espetáculo. Esse algoritmo deve calcular e mostrar a quantidade de 
#convites que devem ser vendidos para que pelo menos o custo do espetáculo seja 
#alcançado.

custo_total = float(input("Custo do espetáculo teatral: "))
preco_convite = float(input("Custo do convite espetáculo teatral: "))

quantidade = custo_total / preco_convite

print("É necessário vender", quantidade, "convites para cobrir o custo.")