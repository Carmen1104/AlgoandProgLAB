X = int(input('Enter the number :'))

if X % 11 == 0:
    print('A', end='')
    if X % 9 == 0:
        print('B', end='')
    if X % 7 == 0:
        print('C', end='')
    if X % 2 == 0:
        print('D', end='')

elif X % 9 == 0:
    print('B', end='')
    if X % 7 == 0:
        print('C', end='')
    if X % 2 == 0:
        print('D', end='')

elif X % 7 == 0:
    print('C', end='')
    if X % 2 == 0:
        print('D', end='')

elif X % 2 == 0:
    print('D', end='')

else:
    print('E')