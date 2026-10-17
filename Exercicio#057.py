x = 0
while x == 0:
    s = str(input('Coloque seu sexo [M/F]: ')).strip().upper()
    if s == 'M' or s == 'F':
        x += 1
    else:
        print('ERRO. DIGITE CORRETAMENTE')
if s == 'M':
    print('Sexo Masculino Cadastrado')
elif s == 'F':
    print('Sexo Feminino Cadastrado')