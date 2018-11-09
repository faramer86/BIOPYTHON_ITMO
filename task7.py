

from functools import reduce

# EASY

# First

def valuesunion(*dicts):
    l = list()
    for i in dicts:
        for j in i.values():
            l.append(j)
    return set(l)
   
# Second
     
def popcount(n):
    a = bin(n)
    return a.count('1')

# Third
    
def powers(n, m):
    new_dict = dict()
    for i in range(1, n + 1):
        new_dict[i] = i ** i % m
    return new_dict
        
# 4th
    
def subpalindrome(Str):
    cache = {}
    if Str in cache.keys():
        return cache[Str]
    if Str == Str[::-1]:
        return Str
    else:
        left = subpalindrome(Str[: -1])
        right = subpalindrome(Str[1: ])
        recursedList = [left, right]
        cache[Str] = max(recursedList, key=len) 
        return cache[Str]

# 5th
        
def isIPv4(s):
    new_list = s.split('.')
    new_list = list(map(lambda x: int(x).bit_length(), new_list))
    new_list = list(filter(lambda x: x <= 8, new_list))
    if len(new_list) == 4:
        return True
    else:
        return False

# 6th

# HAS NO TIME

# HARD 

# 2

def fibonacci(n):
    return reduce(lambda x, n:[x[1], x[0] + x[1]], range(n), [0,1])[0]
