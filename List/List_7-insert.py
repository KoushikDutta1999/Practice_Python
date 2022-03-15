# Python Program to insert element between a List

List = eval(input("Enter List Element: "))
print("The List ",List)

place = int(input("Enter the index place to insert an element: "))

ele = int(input("Enter the element to insert: "))

List.insert(place,ele)

print("List after inserting an element between the List: ",List)