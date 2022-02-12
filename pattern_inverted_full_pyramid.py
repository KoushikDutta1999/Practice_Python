# Python Program to print inverted full pyramid using *

rows = int(input("Enter numbers of rows: "))

for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ",end="") #There are two spaces
    for j in range(i, 2*i-1):
        print("* ",end="")
    for j in range(1, i-1):
        print("* ",end="")
    print()
print("----------------------------------------------")

