n = int(input('Digite um número [999 para parar]: '))
soma = 0
cont = 0
if n != 999:
      while n != 999:
          soma += n    # É o mesmo que Digitar soma = soma + n
          cont +=1
          n = int(input('Digite um número [999 para parar]: '))
      print(f'Você digitou {cont} números e a soma entre eles foi {soma}')

else:
    print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
    print('Programa Finalizado!')