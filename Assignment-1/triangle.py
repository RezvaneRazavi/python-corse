print("Please enter the sides: ")

a = float(input('first side: '))
b = float(input('second side: '))
c = float(input('third side: '))


if a < b + c and b < a + c and c < a + b:
    print('YES, possible to triangle.')
else: 
    print('No, not possible.')
