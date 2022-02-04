def recursive_fibonacci(n):
    if n <=1:
        return n
    else:
        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10

for i in range(n_terms):
    print(recursive_fibonacci(i))