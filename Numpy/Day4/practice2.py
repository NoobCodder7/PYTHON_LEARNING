import numpy as np
""""Intermediate (10)
Calculate row-wise sums of a matrix.
Calculate column-wise sums of a matrix.
Find all elements greater than 50.
Use np.sqrt() on an array.
Find the product of all elements.
."""

a = np.array([
    [10, 20, 30, 40],
    [40, 20, 43, 20]
])

print(np.sum(a, axis = 1))
print(np.sum(a, axis = 0))
print(a > 50)
print(np.sqrt(a))
print(np.prod(a))
print(a+10)
print(a*5)
