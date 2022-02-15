# Python Program to Compute the Power of a Number

# using a while loop

base =  int(input("Enter the Base: "))
exponenet =  int(input("Enter the Exponenet: "))

result = 1

while exponenet != 0:
    result *= base
    exponenet-=1
    
print("Answer = " + str(result))
# -----------------------------------------------

# using a for loop

for exponenet in range(exponenet, 0, -1):
    result *= base
    
print("Answer = " + str(result))
# -------------------------------------------------

# using pow()

# result = pow(base, exponenet)
# print("Answer = " + str(result))