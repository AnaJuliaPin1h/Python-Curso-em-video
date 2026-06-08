#Analisador de Textos
nome = str(input("Digite seu nome: "))
print("Analisando nome.....")

print("Seu nome em letras maiusculas: {}" .format(nome.upper()))
print("Seu nome em letras minusculas: {}" .format(nome.lower()))
print("Seu nome tem ao todo: {} letras" .format(len(nome)))

#print("Seu primeiro nome é: {}, e ele tem {} letras" .format(len(nome.find(' ') )))   # o find retorna so o primeiro nome

separa = nome.split()
print(separa)

#é usado para dividir uma string (texto) em pedaços menores e organizá-los em uma lista. 
# Por padrão, ele separa o texto onde encontra espaços em branco

texto = "Python é muito legal"
palavras = texto.split()

print(palavras)
# Saída: ['Python', 'é', 'muito', 'legal']