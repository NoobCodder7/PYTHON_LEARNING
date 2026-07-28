import numpy as np

arr1 = np.array([1,2,3,4])
print(arr1)
print(type(arr1))      # Type of object
print(arr1.dtype)      # Data type of elements
print(arr1.ndim)       # Number of dimensions
print(arr1.shape)      # Shape of array
print(arr1.size)       # Total number of elements




arr2 = np.array([
    [1,2],
    [3,4]
])
print(arr2)
print(type(arr2))      # Type of object
print(arr2.dtype)      # Data type of elements
print(arr2.ndim)       # Number of dimensions
print(arr2.shape)      # Shape of array
print(arr2.size)       # Total number of elements


arr3 = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])
print(arr3)
print(type(arr3))      # Type of object
print(arr3.dtype)      # Data type of elements
print(arr3.ndim)       # Number of dimensions
print(arr3.shape)      # Shape of array
print(arr3.size)       # Total number of elements
