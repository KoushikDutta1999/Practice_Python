# Python Program to show a month of a particular year

import calendar

yy = int(input("Enter the Year: "))
mm = int(input("Enter the Month in number: "))

print(calendar.month(yy,mm))