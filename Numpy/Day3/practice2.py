import numpy as np

#Create a 5×5 matrix and print the diagonal elements.
arr = np.array([
    [1,2,3,4,5],
    [6,7,8,9,1],
    [1,2,3,4,5],
    [6,7,8,9,1],
    [6,7,8,9,1]
])
print(np.diagonal(arr))

#Extract the last two rows.
print(arr[-2:,])
#Extract the middle three columns.
print(arr[:, 1:4])
#Reverse the rows of a matrix.
print(arr[::-1])
#Reverse the coulumns of a matrix.
print(arr[:, ::-1])
#Print all elements greater than 50 using Boolean Indexing
arr = np.array([10, 35, 60, 90, 12, 51, 72, 45])
print(arr[arr > 50])
#Print all elements greater than 50 using Boolean Indexing
arr = np.array([3, 6, 8, 11, 14, 19, 20, 25])
print(arr[arr % 2 == 0])
#Select elements at indices [1, 3, 5, 7] using Fancy Indexing
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[[1, 3, 5, 7]])


# Create a 3D array and access the last element

arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("3D Array:")
print(arr)

print("\nLast Element:")
print(arr[-1, -1, -1])