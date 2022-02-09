# Python Program to transpose a matrix using list comprehension

rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of First Matrix:")
x= [[int(input()) for i in range(column)] for i in range(rows)]
print("The Matrix is: ")
for n in x:
    print(n)

result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
print("-----------------------------------------")
for r in result:
    print(r)