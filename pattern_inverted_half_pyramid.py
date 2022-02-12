# Python Program to print inverted half pyramid using *

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    print("\n")
print("-------------------------------------")

# Python Program to create inverted half pyramid using numbers

for i in range(rows, 0, -1):
    for j in range(1, i):
        print(j, end=" ")
    print("\n")
print("-------------------------------------")
