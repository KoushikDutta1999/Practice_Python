# Python Program to perform different set operations like in mathematics

arr1 = []
num = int(input("Enter number of arr1: "))

for i in range(1, num+1):
    ele = int(input("Enter : "))
    arr1.append(ele)

arr2 = []
num = int(input("Enter number of arr2: "))

for i in range(1, num+1):
    ele = int(input("Enter : "))
    arr2.append(ele)

print("First List: ",arr1)
print("Second List: ",arr2)

union_list = list(set(arr1 + arr2))
print("Union of Both List : ",union_list)
print("---------------------------------------------------")
