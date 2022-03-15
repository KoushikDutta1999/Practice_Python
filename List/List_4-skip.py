# Python Program to print list with skipped element

List = eval(input("Enter List Element: "))
print("The List ",List)

a = int(input("Enter numbers to skip: "))

l = List[::a]

print("List after skipping",l)