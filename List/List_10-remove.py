# Python Program to remove an element from a List

List = eval(input("Enter Element for List: "))
print("The List ",List)

rem = int(input("Enter the element to remove: "))

List.remove(rem)

print("List after removing:",List)