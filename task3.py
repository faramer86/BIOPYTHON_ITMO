#   2
#   Implement the following functions in file task3/task3.py
#   using map, filter, zip, reduce:

from functools import reduce


def extractnumbers(s):
    return filter(lambda x: x.isdigit(), s)


def changecase(s):
    return map(lambda x: x.lower() if x.isupper() else x.upper(), s)


def productif(elems, conds):
    return reduce(lambda x, y: x*y, list(map(lambda x, y: x if y is True
                                             else 1, elems, conds)))
