import numpy as np


def getdimension(a):
    return a.ndim


def getdiagonal(a):
    return a.diagonal()


def cutarray(a, minvalue, maxvalue):
    return np.clip(a, minvalue, maxvalue)


def getmoments(a):
    return tuple([a.mean(), a.var()])


def getdotproduct(a, b):
    return np.dot(a, b)


def checkequal(a, b):
    return a == b


def comparewithnumber(a, bound):
    return a < bound


def matrixproduct(a, b):
    return np.dot(a, b)


def matrixdet(a):
    return np.linalg.det(a)


def getones(n, k):
    return np.fromfunction(lambda i, j: j - i == k, (n, n)) * 1.0
