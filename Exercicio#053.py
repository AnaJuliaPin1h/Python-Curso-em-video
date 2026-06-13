# Detector de Palíndromo

frase = str(input('Digite frase: ').strip().lower().replace(' ',''))
f2 = (frase[::-1])
print(f2)
if frase == f2:
    print('palindromo')
else:
    print('Nao é palindromo')