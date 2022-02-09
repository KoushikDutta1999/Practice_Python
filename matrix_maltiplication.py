# A Python Program to multiply two matrices using list comprehension

rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of First Matrix:")
matrix_a= [[int(input()) for i in range(column)] for i in range(rows)]
print("First Matrix is: ")
for n in matrix_a:
    print(n)

print("-----------------------------------------")
rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of Second Matrix:")
matrix_b= [[int(input()) for i in range(column)] for i in range(rows)]
print("Second Matrix is: ")
for n in matrix_b:
    print(n)

result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*matrix_b)] for X_row in matrix_a]
print("-----------------------------------------")
for r in result:
    print(r)