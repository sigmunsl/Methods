import numpy as np


def sms_diag(matrix):
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Matrix must be of type ndarray')

    c = matrix.diagonal(1).copy().astype(np.float)
    d = matrix.diagonal(0).copy().astype(np.float)
    a = matrix.diagonal(-1).copy().astype(np.float)

    return a, d, c

###############################################################################

def trifactor(a, d, c):
    n = len(d)
    if len(a) != n-1 or len(c) != n-1:
        raise IndexError('a and c must have length n-1 where n is length of d')

    u = d
    l = a
    print(l.dtype)
    for k in range(n-1):
        l[k] = a[k]/u[k]
        u[k+1] = d[k+1]-l[k]*c[k]
    return l, u, c


###############################################################################

#def trisolve(l, u, c, b):


