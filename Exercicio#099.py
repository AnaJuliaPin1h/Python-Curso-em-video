def maior(*lst):
    if not lst:
        print('Não foi informado nenhum valor')
        return
    ma = 0
    for l in lst:
        if ma == 0 or ma < l:
            ma = l
    print(f'O maior valor na ordem {lst} é {ma}')

maior(1, 2, 4, 2, 8)
maior(1, 4, 3)
maior()