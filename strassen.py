import sys
import numpy as np


def split_in_quarters(a):
    return np.hsplit(np.vsplit(a, 2)[0], 2) + np.hsplit(np.vsplit(a, 2)[1], 2)


def strassen(a, b):
    if np.size(a) == 1:
        return np.dot(a, b)
    else:
        a11, a12, a21, a22 = split_in_quarters(a)
        b11, b12, b21, b22 = split_in_quarters(b)
        p1 = strassen(a11 + a22, b11 + b22)
        p2 = strassen(a21 + a22, b11)
        p3 = strassen(a11, b12 - b22)
        p4 = strassen(a22, b21 - b11)
        p5 = strassen(a11 + a12, b22)
        p6 = strassen(a21 - a11, b11 + b12)
        p7 = strassen(a12 - a22, b21 + b22)
        c11 = p1 + p4 - p5 + p7
        c12 = p3 + p5
        c21 = p2 + p4
        c22 = p1 - p2 + p3 + p6
        return np.vstack((np.hstack((c11, c12)),
                          np.hstack((c21, c22))))


n = int(input())
k = 1
while k < n:
    k *= 2
a = np.zeros((k, k), dtype=np.int)
b = np.zeros((k, k), dtype=np.int)
for i in range(n):
    a[i, :] = list(map(int, input().split(' ')))
for i in range(n):
    b[i, :] = list(map(int, input().split(' ')))
d = strassen(a, b)[:n, :n]
for row in d:
    print(' '.join(map(str, row)))
