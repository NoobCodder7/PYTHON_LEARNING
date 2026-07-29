import numpy as np

# Employee salaries
salary = np.array([35000, 42000, 48000, 51000, 56000,
                   61000, 47000, 53000, 59000, 65000])

print("Original Salary Array:")
print(salary)

# Give every employee a salary increment of 5000
updated_salary = salary + 5000

print("\nUpdated Salary Array:")
print(updated_salary)

# Total salary expense
print("\nTotal Salary Expense:")
print(np.sum(updated_salary))

# Average salary
print("\nAverage Salary:")
print(np.mean(updated_salary))

# Highest salary
print("\nHighest Salary:")
print(np.max(updated_salary))

# Lowest salary
print("\nLowest Salary:")
print(np.min(updated_salary))

# Employees earning more than 50000
print("\nEmployees earning more than 50000:")
print(updated_salary[updated_salary > 50000])

# Create a 2D salary matrix
salary_matrix = updated_salary.reshape(2, 5)

print("\nSalary Matrix:")
print(salary_matrix)

# Row-wise totals
print("\nRow-wise Salary Total:")
print(np.sum(salary_matrix, axis=1))

# Column-wise totals
print("\nColumn-wise Salary Total:")
print(np.sum(salary_matrix, axis=0))

# Add performance bonus using broadcasting
bonus = 2000

final_salary = salary_matrix + bonus

print("\nFinal Salary after Bonus:")
print(final_salary)