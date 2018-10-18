from itertools import *
from math import *


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
    return digitsum(n // 10) + n % 10


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


def genbinarystrings(n):
    bin_str = [''.join(p) for p in product('10', repeat=n)]
    bin_str.sort(key=lambda s: s.count('1'))
    return bin_str


def istpower(n):
    if n <= 0:
        return False
    elif n == 1:
        return True
    elif n % 2 == 0:
        return istpower(n // 2)
    else:
        return False


def concatnumbers(a, b):
    if b // 10 == 0:
        return a * 10 + b
    else:
        return round(concatnumbers(a, b/10) * 10, 1)


def buttock(n):
    if n == 1:
        return [1]
    else:
        return buttock(n-1) + [n] + buttock(n-1)


def parentheses(s):
    if len(s) in [0, 1, 2]:
        return '(' + s + ')'
    else:
        return '(' + s[0] + parentheses(s[1:-1]) + s[-1] + ')'


def gcd(a, b):
    if a == b:
        return a
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)


def mergesort(unsorted_list):
    def merge(left_half, right_half):
        #  merge and sort
        new_list = []
        while len(left_half) != 0 and len(right_half) != 0:
            if left_half[0] < right_half[0]:
                new_list.append(left_half[0])
                left_half.remove(left_half[0])
            else:
                new_list.append(right_half[0])
                right_half.remove(right_half[0])
        if len(left_half) == 0:
            new_list = new_list + right_half
        else:
            new_list = new_list + left_half
        return new_list
    #  devide the list
    if len(unsorted_list) <= 1:
        return unsorted_list
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
    #  continue to devide until length is 1 (rec number 1)
    left_list = mergesort(left_list)
    right_list = mergesort(right_list)
    # then merge and sort
    return list(merge(left_list, right_list))
