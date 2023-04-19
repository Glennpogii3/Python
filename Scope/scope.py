def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def fib(n):
    if n in {0, 1}:
        return n
    return fib(n - 1) + fib(n - 2)

def fib2(n):
    if n == 0:
        r = 0
    elif n == 1:
        r = 1
    else:
        n1 = 1
        n2 = 0
        for f in range(1 , n):
            r = n2 + n1
            n2 = n1
            n1 = r
    return r

for i in range(36):
    print(i, fib2(i))

