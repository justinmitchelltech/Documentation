import numpy as np

A = np.array([[2,1],[1,2]])
eig, Q = np.linalg.eigh(A)
print('eig = ', eig)
print('Q = ', Q)

A = np.array([[1, 2], [3, 4]])
print('A.T = ', A.T)  # Transposed

A = np.array([[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20]])

print('\n', A[-2,:])

# "sympy is good"
print('\n\n\n\n')

from random import choices
population = [-1, 2]
weights = [0.5, 0.5]
pls = choices(population, weights, k=10)
cumpls = np.cumsum(pls)
print(pls)
print(cumpls)