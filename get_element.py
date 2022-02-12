# Python Program to get an element from array

arr = []

n = int(input("Enter number of element: "))

for i in range(0, n):
    ele = input()
    arr.append(ele)

print("First Element: ",arr[0])
print("Last Element: ",arr[-1])