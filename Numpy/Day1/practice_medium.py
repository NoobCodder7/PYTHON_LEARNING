import numpy as np
# Create a 5 × 5 matrix of zeros and replace the center value with 1.
arr = np.zeros((5, 5), dtype=int)
arr[2, 2] = 1
print(arr)
#Create an array of even numbers from 2 to 100.
arr = np.arange(2, 101, 2)
print(arr)
#Create an array of odd numbers from 2 to 100.
arr = np.arange(1, 100, 2)
print(arr)
#Create a 3 × 3 matrix filled with 100.
arr = np.full((3,3), 100)
print(arr)
#Create an identity matrix of size 6 × 6.
arr = np.eye(6)
print(arr)
#Create 20 numbers between 5 and 10 using np.linspace().
arr = np.linspace(5, 10, 20)
print(arr)
#Create a 2 × 3 array of ones and multiply it by 50.
arr = np.ones((2, 3), dtype=int) * 50
print(arr)
#Create a 4 × 4 matrix filled with random (uninitialized) values using np.empty().
arr = np.empty((4, 4))
print(arr)
#Create a NumPy array from a Python tuple (10, 20, 30, 40)

t = (10, 20, 30, 40)
arr = np.array(t)
print(arr)


#Create a 3 × 3 identity matrix using both np.eye() and np.identity() and compare the outputs.


arr1 = np.eye(3)
arr2 = np.identity(3)
print("Using np.eye():")
print(arr1)
print()
print("Using np.identity():")
print(arr2)