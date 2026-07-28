import numpy as np
#Create a 1D array and print its shape.
arr = np.array([10, 20, 30, 40])
print(arr.shape)
#Create a 2D array and print its size.
arr = np.array([
    [20,23],
    [30,43]
])
print(arr.shape)
#Print the number of dimensions of a 3D array.
arr = np.array([[[1]]])
print(arr.ndim)
#Print the number of dimensions of a 3D array.
arr = np.array([10, 20, 30, 40])
print(arr.dtype)
#Create a float array and check its datatype.
arr = np.array([12.32, 321.32])
print(arr.dtype)
#Print the itemsize of an integer array.
arr = np.array([10, 20, 30, 40])
print(arr.size)
#Print the nbytes of a 10-element array.
arr = np.array([10, 20, 30, 40,23, 42, 243 ,123, 324, 432])
print(arr.nbytes)
#Convert an integer array to float using astype().
arr = np.array([10, 20, 30, 40])
new = arr.astype(float)
print(new.dtype)
#Convert a float array to integer.
arr = np.array([12.32, 321.32])
new = arr.astype(int)
print(new.dtype)
#Create an array and print all its properties.
import numpy as np

# Create an array
arr = np.array([[10, 20, 30],
                [40, 50, 60]])

# Print the array
print("Array:")
print(arr)

# Print properties
print("\nProperties of the Array:")
print("Shape:", arr.shape)
print("Dimensions (ndim):", arr.ndim)
print("Size (Total Elements):", arr.size)
print("Data Type:", arr.dtype)
print("Item Size (bytes):", arr.itemsize)
print("Total Memory (bytes):", arr.nbytes)
print("Array Type:", type(arr))
print("Transpose:")
print(arr.T)