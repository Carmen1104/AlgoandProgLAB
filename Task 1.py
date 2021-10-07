X = int(input('Enter the number :'))

#Code begins by checking if the number is divisible by 11. If not, it skips to the next part.
if X % 11 == 0:
    print('A', end='')
    #If true, then it continues the check for all other numbers.
    if X % 9 == 0:
        print('B', end='')
    elif X % 7 == 0:
        print('C', end='')
    else:
        print('D', end='')

#Checks if the number is divisible by 9. If not, skip. 
elif X % 9 == 0:
    print('B', end='')
    if X % 7 == 0:
        print('C', end='')
    else:
        print('D', end='')

#Checks if the number is divisible by 7. If not, skip.
elif X % 7 == 0:
    print('C', end='')
if X % 2 == 0:
    print('D', end='')

#Checks if the number is divisible by 2. If not, skip.
elif X % 2 == 0:
    print('D', end='')

#Prints EEEEEE!
else:
    print('E')