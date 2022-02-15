n1 = int(input("Enter number of element: "))

list_1 = []

for i in range(0, n1):
    ele = input()
    list_1.append(ele)
print("List 1:", list_1)

n2 = int(input("Enter number of element: "))

list_2 = []

for i in range(0, n2):
    ele = input()
    list_2.append(ele)
print("List 2:", list_2)


print("Joined / Concatenated list: " )
list_joined = list_1 + list_2
print(list_joined)

#With unique values

print("Joined / Concatenated list with Unique Values: " )
list_joined = list(set(list_1 + list_2))
print(list_joined)