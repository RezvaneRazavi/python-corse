def mul (n, m ):
    for i in range(1, n+1):
        for j in range(1, m+1):
            print( i*j, end=' ')
        print()


row = int(input('enter row: '))
col = int(input('enter col: '))
print('~~~~~~~~~~~~~~~~~~~')

mul (row, col)