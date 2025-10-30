# WAP to eval list 1 and list 2 and find sum of list
# for eg
# list1 = [1,2,3]
# list2 = [4,5,6]
# sum_list = [5,7,9]

list1 = eval(input("Enter list: "))
list2 = eval(input("Enter list 2: "))
list_sum = []

for a,b in zip(list1,list2):
    list_sum.append(a + b)

if len(list1) > len(list2):
    for i in range(len(list2), len(list1)):
        list_sum.append(list1[i])
elif len(list1) < len(list2):
    for i in range(len(list1), len(list2)):
        list_sum.append(list2[i])

print(list_sum)

# print(dir(list))