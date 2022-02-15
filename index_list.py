# Python Program to Access Index of a List Using for Loop

n = int(input("Enter number of element: "))

my_list = []

for i in range(0, n):
    ele = int(input())
    my_list.append(ele)
print(my_list)

print("The index(starting from 0) of the values are: ")
for index, val in enumerate(my_list):
    print(index,val)

#Start the indexing with non zero value

print("The index(starting from 1) of the values are: ")
for index, val in enumerate(my_list, start=1):
    print(index,val)

#Without using enumerate()

print("Without using enumerate()")
for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)