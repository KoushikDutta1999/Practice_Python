# Python Program to add all element from list

List = eval(input("Enter Element for List: "))
# [1,2,4,4,3,3,3,6,5] 
print("The List ",List)

sum = 0
for i in List:
    sum = sum + i
    
print("Sum of the elements of the List: ",sum)