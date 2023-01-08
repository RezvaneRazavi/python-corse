list = []
list_delete = []


len_list = int(input("enter len list: "))

for i in range(len_list):
    number = int(input("enter number: "))
    list.append(number)

for item in list:
    if item not in list_delete:
        list_delete.append(item)

print(list)
print(list_delete)

