# Python Program to find an element in a given List

List = eval(input("Enter the Element of the List"))
print("The List ",List)

num = int(input("Enter the Element to Find: "))

for i in List:
    if i == num :
        print("!!!Element Found!!!",num)
    else:
        print("lement Not Found")