x = int(input('enter number: '))
y = int(input('enter number: '))

if x > y:
    big_number = x
else:
    big_number = y

for i in range(big_number, x*y+1):
    if i % x == 0 and i % y == 0:
        kmm = i
        break

print("kmm: ", kmm)