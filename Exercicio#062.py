ft = int(input('Enter the first term of an arithmetic progression: ')) #ft = first term
cd = int(input('Enter the common difference of an arithmetic progression: ')) #cd = common difference
counter = 0
while counter != 10:
    print(f'{ft} ', end = '')
    if counter < 9:
        ft += cd
    counter += 1
    if counter == 10:
        print()
at = 1
#at = additional terms
while at != 0:
    at = int(input('Do you want show how many terms?[type only numbers] '))
    c = 0
    while c != at:
        ft += cd
        print(f'{ft} ', end = '')
        c += 1
        if c == at:
            print()
print('ACABOU')