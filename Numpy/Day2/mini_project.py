"""⭐ Mini Project — Employee Salary Dataset

Create a program that:

Imports NumPy.
Creates an array of salaries for 10 employees.
Prints the array.
Prints:
Shape
Size
Number of dimensions
Data type
Item size
Total memory (nbytes)
Converts the salary array to float.
Creates a copy() of the salary array and modifies one value.
Creates a view() of the salary array and modifies one value.
Compare the outputs of the original array, copied array, and view array."""



import numpy as np 

salary = np.array([ 2300, 3234, 2542, 6423, 32445, 6424 ,63355, 2245, 5235, 2535])
print(salary)
print(salary.size)
print(salary.shape)
print(salary.ndim)
print(salary.dtype)
print(salary.nbytes)


new_Salary = salary.astype(float)
print(new_Salary)


copy_salary = salary.copy()
new_Salary[0] = 293923

print(salary, new_Salary)

view_salary = salary.view()
view_salary[1] = 12221

print(salary, view_salary)
