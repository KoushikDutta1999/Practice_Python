# a = print from 4th index
# b = print the 5th last number
# c = print every even index

List = eval(input("Enter List Elements: "))
print("The List: ",List)

a = List[4::]

b = List[-5]

c = List[::2]

print("List starting from 4th index: ",a)

print("5th from last Element: ",b)

print("List of every even index: ",c)