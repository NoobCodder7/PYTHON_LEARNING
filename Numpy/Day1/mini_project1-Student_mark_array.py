import numpy as np

# 1. Create an array of marks for 10 students
marks = np.array([85, 72, 90, 68, 95, 80, 76, 88, 91, 79])

print("Student Marks:")
print(marks)

# 2. Create a 5 × 5 attendance matrix of ones
attendance = np.ones((5, 5), dtype=int)

print("\nAttendance Matrix:")
print(attendance)

# 3. Create a 3 × 3 matrix filled with the passing mark (35)
passing_marks = np.full((3, 3), 35)

print("\nPassing Marks Matrix:")
print(passing_marks)

# 4. Create a 4 × 4 identity matrix
identity = np.eye(4, dtype=int)

print("\nIdentity Matrix:")
print(identity)

# 5. Create roll numbers from 1 to 10
roll_numbers = np.arange(1, 11)

print("\nRoll Numbers:")
print(roll_numbers)

# 6. Create five evenly spaced percentages from 0 to 100
percentages = np.linspace(0, 100, 5)

print("\nPercentages:")
print(percentages)