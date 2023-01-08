number = int(input('enter number= '))

temp1 = 1
temp2 = 0

for i in range(number):
    sum = temp1 + temp2
    temp1 = temp2
    temp2 = sum
    print(sum)

    