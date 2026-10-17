# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
entrada = input('insira 2 números separados por espaço')
n1, n2 = entrada.split()
n1 = float(n1)
n2 = float(n2)
c = 0
print(''' [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior
 [ 4 ] novos números
 [ 5 ] sair do programa
    ''')
while c != 5:
    c = int(input('insira uma função a ser aplicada:'))
    if c == 1:
        soma = n1 + n2
        print(f'a soma requisitada é {soma}')
    elif c == 2:
        mult = n1*n2
        print(f'o resultado é {mult}')
    elif c == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'o maior número é {maior}')
    elif c == 4:
        novosnumeros = input('insira os números separados por espaço novamente:')
        n1, n2 = novosnumeros.split()
        n1 = float(n1)
        n2 = float(n2)
    elif c == 5:
        print('o programa foi finalizado')
    else:
        print('número inserido imcompatível')