# Python Program to Remove duplicate element in a list

List1 = eval(input("Enter the Element of the List"))
# [1,2,3,3,4,5,5,6]
print("The List ",List1)

l = [] #empty list

for i in List1:
    if i not in l:
        l.append(i)


print("List after removing Duplicate elements: ",l)