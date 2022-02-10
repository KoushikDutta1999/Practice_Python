# Python Program to Randomly Select an Element From the List

import random

list = []

n = int(input("Enter number of element: "))
for i in range(0, n):
    ele = input()
    list.append(ele)

print(list)

print("Random Choice from the list is : ", random.choice(list))