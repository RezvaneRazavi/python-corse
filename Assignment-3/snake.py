array = []

len = int(input("Enter the length of array: "))

for i in range(len):
    if  i % 2 == 0:
        print("*", end="")
    else:
        print("#", end="")
    
