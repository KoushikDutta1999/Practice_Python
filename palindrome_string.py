# Python Program to check if a string is palindrome or not

my_str = input("Enter your String: ")

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("The String is a Palindrome.")
else:
    print("The String is not a Palindrome.")