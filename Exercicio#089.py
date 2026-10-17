alunos = []   
while True:
    aluno = []
    aluno.append(input('Nome: ').strip().title())
    aluno.append(float(input(f'Nota 1: ')))
    aluno.append(float(input(f'Nota 2: ')))
    alunos.append(aluno)
    res = input('Deseja continuar: [S/N] ').strip()[0]
    if res in 'Nn':
        break
print(f'{'Nº':<5}| {'Nome':<20}| {'Média':<5}')
print('-' * 35)
for i, a in enumerate(alunos):
    print(f'{i:<5}|', end=' ')
    print(f'{a[0]:<20}|', end=' ')
    soma = a[1] + a[2]
    print(f'{soma/2:>5.1f}')
esc = 0
while True:
   n = abs(int(input('Mostrar notas de qual aluno: (999 interrompe) ')))
   
   if n == 999:
        print('\033c', end='')
        print('Programa encerrado...')
        break
if n < len(alunos):
        print('-' * 35)
        print(f'Notas do(a) aluno(a): {alunos[n][0].upper()}')
        for i in range(2):
            print(f'\tNota {i + 1}: {alunos[n][i + 1]:.1f}')
        print('-' * 35)