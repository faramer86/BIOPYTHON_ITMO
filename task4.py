def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2) 

def recurrent(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return recurrent(n // 2)
    else:
        return recurrent((n - 1) // 2) + recurrent((n - 1) // 2 + 1) 

def digitsum(n):
    if n <= 9:
        return n
    return digitsum(n//10) + n%10

def reversestring(s):
    num = len(s)
    if s == '':
        return ''
    return s[-1] + reversestring(s[0:num-1])

def ackermann(m, n):
    if m == 0:
        return n+1
    elif n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n - 1))
