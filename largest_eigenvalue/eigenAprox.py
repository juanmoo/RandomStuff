import numpy as np
from numpy.linalg import inv, norm

V = np.array([
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])
L = np.array([
    [1, 0, 0, 0],
    [0, 5, 0, 0],
    [0, 0, 4, 0],
    [0, 0, 0, 2]
])

A = V@L@inv(V)
print(A)

v0 = np.random.random((4, 1))
v = v0

for n in range(10000):
    v = (A@v)/norm(A@v, ord='fro')**.5
    if n % 100 == 0:
        print("Iteration:", n)
        print(v)
