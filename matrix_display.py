# A Python Program for matrix input from user

row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

matrix = []
print("Enter the entries rowwise: ")

for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)
    
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end = " ")
    print()