palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')

for i in palavras:
    print(f'Na palavra {i.upper()} temos: ', end='')
    for i in i:
        if i in 'AaEeIiOoUu':
            print(f'{i} ', end=' ')
    print('')

