from functools import reduce
import itertools

# EASY

# 1st


def valuesunion(*dicts):
    l = list()
    for i in dicts:
        for j in i.values():
            l.append(j)
    return set(l)

# 2nd


def popcount(n):
    a = bin(n)
    return a.count('1')

# 3rd


def powers(n, m):
    new_dict = dict()
    for i in range(1, n + 1):
        new_dict[i] = i ** i % m
    return new_dict

# 4th


def subpalindrome(Str):
    cache = {}

    def noncache(Str):
        if Str in cache.keys():
            return cache[Str]
        if Str == Str[::-1]:
            return Str
        else:
            left = noncache(Str[:-1])
            right = noncache(Str[1:])
            recursedList = [left, right]
            cache[Str] = max(sorted(recursedList), key=len)
            return cache[Str]
    return noncache(Str)

# 5th


def isIPv4(s):
    try:
        new_list = s.split('.')
        for number in new_list:
            if number.isdigit():
                continue
            else:
                return False
        new_list = list(map(lambda x: int(x).bit_length(), new_list))
        new_list = list(filter(lambda x: x <= 8, new_list))
        if len(new_list) == 4:
            return True
        else:
            return False
    except:
        return False

# 6th


def pascals():
    prev = (1,)
    for i in itertools.count(1):
        act = []
        act.append(1)
        for k in range(len(prev) - 1):
            act.append(prev[k] + prev[k + 1])
        act.append(1)
        yield tuple(prev)
        prev = act

# HARD

# 1st


def spiral(n):
    mat = [[0] * n for i in range(n)]
    st, m = 1, 0
    mat[n // 2][n // 2] = n * n
    for v in range(n // 2):
        # Up
        for i in range(n-m):
            mat[v][i + v] = st
            st += 1
        # Right
        for i in range(v + 1, n - v):
            mat[i][-v-1] = st
            st += 1
        # Down
        for i in range(v + 1, n - v):
            mat[- v - 1][- i - 1] = st
            st += 1
        # Left
        for i in range(v + 1, n - (v + 1)):
            mat[- i - 1][v] = st
            st += 1
        m += 2
    return mat

# 2nd


def fibonacci(n):
    return reduce(lambda x, n: [x[1], x[0] + x[1]], range(n), [0, 1])[0]

# 3rd



def brackets2(n, m):
    def unique_permutations(iterable, r=None):
        previous = tuple()
        for p in itertools.permutations(sorted(iterable), r):
            if p > previous:
                previous = p
                yield p
    brackets = ["()", "[]"]
    a = "()"*n + "[]"*m
    for e in unique_permutations(a):
        b = "".join(e)
        r = b
        while any(x in b for x in brackets):
            for br in brackets:
                b = b.replace(br, '')
        if b == '':
            yield r
