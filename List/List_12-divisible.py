# Python Program to Print all elements divisible by M and N in the List

List = eval(input("Enter the Element of the List"))
# [1,2,4,4,3,3,3,6,5] 
print("The List: ",List)

m = int(input("The M: "))
n = int(input("The N: "))

for i in List:
    if i % m == 0 and i % n == 0:
        print("Elements divisible by M and N: ",i)