#  1
#  Implement the following generators in file task3/task3.py

import itertools
from functools import reduce


def squares(a):
    for i in a:
        yield i*i


def repeatntimes(elems, n):
    elems = list(elems)
    for i in range(n):
        yield from elems


def evens(x):
    if x % 2 == 0:
        yield from itertools.count(x, 2)
    else:
        yield from itertools.count(x+1, 2)


def digitsumdiv(p):
    yield from itertools.count(p, p)

#   2
#   Implement the following functions in file task3/task3.py
#   using map, filter, zip, reduce:


def extractnumbers(s):
    return filter(lambda x: x.isdigit(), s)


def changecase(s):
    return map(lambda x: x.lower() if x.isupper() else x.upper(), s)


def productif(elems, conds):
    return reduce(lambda x, y: x*y, list(map(lambda x, y: x if y is True
                                             else 1, elems, conds)))
