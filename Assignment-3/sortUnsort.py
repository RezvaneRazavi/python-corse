array = []

len = int(input("Enter the length of array: "))

for i in range(len):
    number = input("enter number: ")
    array.append(number)

copyArray = array.copy()
array.sort()

if copyArray == array:
    print("sort")
else:
    print("not sort")
    


