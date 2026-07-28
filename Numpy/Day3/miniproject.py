""""⭐ Mini Project — Student Marks Analysis

Create a program that:

Imports NumPy.
Creates a 5 × 5 matrix of marks for five students in five subjects.
Prints the complete matrix.
Prints:
First student's marks
Last student's marks
Marks of the third subject
Marks of the first two students
Marks greater than 80
Even marks
Reverse the order of students.
Select students at index 0, 2, and 4 using Fancy Indexing."""




import  numpy as np 
marks = np.array([
   [85, 78, 92, 88, 76],
    [67, 81, 74, 90, 85],
    [95, 89, 84, 79, 91],
    [72, 65, 80, 87, 94],
    [88, 93, 77, 82, 69]    
                 ])
print("\nMarks table")
print(marks)

print("\nFirst student marks")
print(marks[0])

print("\n2. Last Student's Marks:")
print(marks[-1])

print("\n3. Marks of the Third Subject:")
print(marks[:, 2])

print("\n4. Marks of the First Two Students:")
print(marks[:2])

print("\n5. Marks Greater Than 80:")
print(marks[marks > 80])

print("\n Even marks")
print(marks[marks %2==0])

print("\n7. Students in Reverse Order:")
print(marks[::-1])

print("\n8. Students at Index 0, 2, and 4:")
print(marks[[0, 2, 4]])