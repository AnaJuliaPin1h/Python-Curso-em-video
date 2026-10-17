grupo = []
mulheres = []
pesoa_acima_media = []
pessoa = {}
media = 0
while True:
    pessoa["nome"] = input("Digite seu nome: ").strip().title()
    pessoa["sexo"] = " "
    while pessoa["sexo"] != "M" and pessoa["sexo"] != "F":
        pessoa["sexo"] = input("Digite seu sexo:[M/F] ").strip().upper()[0]
        if pessoa["sexo"] not in "MF":
            print("Erro! Por favor, digite apenas M ou F.")
    pessoa["idade"] = int(input("Digite sua idade: "))
    media += pessoa["idade"]
    grupo.append(pessoa.copy())
    continua = " "
    while continua not in "SN":
            continua = input("VocÊ quer adicinar mais um usuario? [S/N] ").strip().upper()[0]
            if continua not in "SN":
                print("Erro! Por favor, digite apenas S ou N.")
    if continua == "N":
        break
media_total = media / len(grupo)
for f in range(len(grupo)):
    if grupo[f]["sexo"] == "F":
        mulheres.append(grupo[f]["nome"])
    if grupo[f]["idade"] > media_total:
        pesoa_acima_media.append(grupo[f]["nome"])
        
print(grupo)
print("-="*30)
print(f"O grupo tem {len(grupo)} pessoas.")
print(f"A media de idade é de {media_total:.2f}")
print(f"As mulheres cadastradas foram: {", ".join(mulheres)}")
print(f"Lista das pessoas que estão acima da media de idade do grupo: {", ".join(pesoa_acima_media)}")