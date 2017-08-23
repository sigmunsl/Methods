import numpy as np


def cda_matrix(matrix):
    """Returns the upper, centre and lower diagonal of a matrix. Takes a matrix as input. Must be array."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Matrix must be of type ndarray')

    c = matrix.diagonal(1).copy().astype(np.float)
    d = matrix.diagonal(0).copy().astype(np.float)
    a = matrix.diagonal(-1).copy().astype(np.float)

    return a, d, c

###############################################################################

def trifactor(a, d, c):
    """Calculates the LU factorization of a strictly diagonal matrix. The function takes a, d, c as inputs where all
    are arrays of length n-1, n, n-1."""
    n = len(d)
    if len(a) != n-1 or len(c) != n-1:
        raise IndexError('a and c must have length n-1 where n is length of d')

    u = d.astype(np.float)
    l = a.astype(np.float)
    for k in range(n-1):
        l[k] = a[k]/u[k]
        u[k+1] = d[k+1]-l[k]*c[k]
    return l, u, c


###############################################################################

def trisolve(l, u, c, b):
    """Function takes l, u, c from trifactor and a vector b. Solves the equation Ax = B for x"""
    x = b
    n = len(b)
    for k in range(1, n):
        x[k] = b[k] - l[k-1]*x[k-1]

    x[n-1] = x[n-1]/u[n-1]
    for k in range(n-2, -1, -1):
        x[k] = (x[k] - c[k]*x[k+1])/u[k]

    return np.array(x)

