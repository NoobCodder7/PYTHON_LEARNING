import numpy as np

#Create a 1D array and print the first element.
arr = np.array([20, 34, 53, 345, 634, 436])
print(arr[0])
#Print the last element using negative indexing.
print(arr[-1])
#Slice the first five elements of an array.
print(arr[0:5])
#Reverse an array.
print(arr[::-1])
#Print every second element.
print(arr[0:6:2])
#Create a 3×3 matrix and print the center element.
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matrix[1,1])
#Print the first row.
print(matrix[0])
#Print the last column.
print(matrix[:,-1])
#Print the first two rows
print(matrix[:2, :])
# Print the second column
print(matrix[:,1])
