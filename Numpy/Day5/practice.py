import numpy as np
#1. Convert a 1D array into a 3×4 matrix.
arr = np.arange(1, 13)
matrix = arr.reshape(3,4)
print(matrix)

#2. Convert a 4×4 matrix into a 2×8 matrix.
matrix = np.arange(1,17).reshape(4,4)
n_matrix = matrix.reshape(2,8)
print(n_matrix)

#3. Flatten a matrix.

matrix = np.array([[1,2,3],
                   [4,5,6]])

flat = matrix.flatten()

print(flat)


#4. Use ravel().


matrix = np.array([[1,2,3],
                   [4,5,6]])

flat = matrix.ravel()

print(flat)


#5. Transpose a matrix.

matrix = np.array([[1,2,3],
                   [4,5,6]])

print(matrix.T)


#6. Add one dimension.

arr = np.array([10,20,30,40])

new_arr = np.expand_dims(arr, axis=0)

print(new_arr)
print("\n")

#7. Remove one dimension.


arr = np.array([[10,20,30,40]])

new_arr = np.squeeze(arr)

print(new_arr)

#8. Resize an array.

arr = np.array([1,2,3,4])

new_arr = np.resize(arr, (3,4))

print(new_arr)

print("\n")
print("\n")

print("\n")

print("\n")

#11. Convert a 24-element array into a 2×3×4 array.

arr = np.arange(24)

n_arr = arr.reshape(2,3,4)
print(n_arr)


