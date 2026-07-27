import numpy as np
#Create an integer NumPy array with values [10, 20, 30, 40, 50].
arr = np.array([10, 20, 30, 40, 50])
print(arr)
#Create a float array with values [1.5, 2.5, 3.5].
arr1 = np.array([1.5, 2.5, 3.5])
print(arr1)
#Create a string array with names of five fruits.
fruits = np.array(["MANGO", "BANANA", "PINEAPPLE", "MUSKMELON", "KIWI"])
print(fruits)
#Create a boolean array with both True and False.
arr = np.array([True, False, True, False, True])
print(arr)
#Create a 4 × 4 matrix of zeros.
arr = np.zeros((4, 4))
print(arr)
#Create a 3 × 5 matrix of ones.
arr = np.ones((3,5))
print(arr)
#Create numbers from 1 to 50 using np.arange().
arr = np.arange(1, 51)
print(arr)
#Create 11 evenly spaced values from 0 to 100 using np.linspace()
arr = np.linspace(0, 100, 11)
print(arr)
#Create a 5 × 5 identity matrix
arr = np.ones((5,5))
print(arr)
#Create a 4 × 4 matrix filled with the value 9
arr = np.full((4,4), 9)
print(arr)