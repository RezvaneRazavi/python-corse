x = int(input("enter number1: "))
y = int(input("enter number2: "))

if x > y:
    x, y = y, x

for i in range(1, x+1):
    if x % i == 0 and y % i == 0:
        bmm = i

print('bmm:', bmm)