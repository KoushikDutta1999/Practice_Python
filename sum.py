from cgitb import reset
from unittest import result


def sum(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

result = sum(100)

print(result)