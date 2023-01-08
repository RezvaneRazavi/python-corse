list = []
list_reverse = []

len_list = int(input("enter len list: "))

for i in range(len_list):
    number = int(input("enter number: "))
    list.append(number)
    

j = len_list-1
while j >= 0:
    list_reverse.append(list[j])
    j-=1

print(list)
print(list_reverse)
