# Python Program to show sum of N natural numbers

num = int(input("Enter a number : "))

if num <= 0:
    print("Enter a number greater than 0")
else:
    sum = 0
    # use while loop to iterate untill zero

    while(num>0):
        sum += num
        num -= 1
    print("The sum is : ",sum)