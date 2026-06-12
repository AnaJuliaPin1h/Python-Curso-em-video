#Ano bissexto

ano = int(input("Em que ano deseja analisar?  "))

if ano % 4 == 0:
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não e bissexto" .format(ano))