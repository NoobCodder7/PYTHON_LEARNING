import numpy as np


"""Practice Questions
"""


"""Add two NumPy arrays.
Subtract two arrays.
Multiply two arrays.
Divide two arrays.
Square every element in an array.
Add 100 to every element.
Find the sum of all elements.
Find the average of an array.
Find the smallest and largest values.
Find the cumulative sum of an array."""

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])


print("The addition of both array is ", a+b)
print("The Subraction of both array is ", a-b)
print("The multiplication of both array is ", a*b)
print("The divison of both array is ", a/b)
print("The floor division of both array is ", a//b)
print("The modulus of both array is ", a%b)
print("Add 100 to every element.", a+5)
print("Add 100 to every element.", b+5)
print("total sum of a = ", sum(a))
print("total sum  of b = ", sum(b))
print("average of a  = ", sum(a))
print("average of b= ", sum(b))
print("min of a  = ", min(a))
print("min of b = ", sum(b))
print("cumulative sum of a = ", np.cumprod(a))
print("cumulative sum of b= ", np.cumprod(a))