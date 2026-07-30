import numpy as np

# ============================================
# 1. Join Two Arrays
# ============================================
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

joined = np.concatenate((arr1, arr2))
print("1. Joined Arrays:")
print(joined)

# ============================================
# 2. Join Matrices Horizontally
# ============================================
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

horizontal = np.hstack((A, B))
print("\n2. Horizontal Join:")
print(horizontal)

# ============================================
# 3. Join Matrices Vertically
# ============================================
vertical = np.vstack((A, B))
print("\n3. Vertical Join:")
print(vertical)

# ============================================
# 4. Split an Array into Three Parts
# ============================================
arr = np.arange(1, 10)

parts = np.array_split(arr, 3)
print("\n4. Split into Three Parts:")
for part in parts:
    print(part)

# ============================================
# 5. Split into Unequal Parts
# ============================================
arr = np.arange(1, 11)

unequal = np.array_split(arr, [3, 7])
print("\n5. Unequal Split:")
for part in unequal:
    print(part)

# ============================================
# 6. Stack Arrays
# ============================================
stacked = np.stack((arr1, arr2))
print("\n6. Stacked Arrays:")
print(stacked)

# ============================================
# 7. Split Matrix Horizontally
# ============================================
matrix = np.arange(1, 17).reshape(4, 4)

horizontal_split = np.hsplit(matrix, 2)
print("\n7. Horizontal Split:")
for part in horizontal_split:
    print(part)

# ============================================
# 8. Split Matrix Vertically
# ============================================
vertical_split = np.vsplit(matrix, 2)
print("\n8. Vertical Split:")
for part in vertical_split:
    print(part)

# ============================================
# 9. Join Three Arrays
# ============================================
arr3 = np.array([7, 8, 9])

joined_three = np.concatenate((arr1, arr2, arr3))
print("\n9. Join Three Arrays:")
print(joined_three)

# ============================================
# 10. Stack Three Matrices
# ============================================
C = np.array([[9, 10],
              [11, 12]])

stack_three = np.stack((A, B, C))
print("\n10. Stack Three Matrices:")
print(stack_three)

# ============================================
# 11. Merge Student Datasets
# ============================================
classA = np.array(["Amit", "Riya", "Karan"])
classB = np.array(["Neha", "Rahul", "Priya"])

students = np.concatenate((classA, classB))
print("\n11. Student Dataset:")
print(students)

# ============================================
# 12. Merge Employee Records
# ============================================
dept1 = np.array([[101, "John"],
                  [102, "Alice"]])

dept2 = np.array([[103, "David"],
                  [104, "Emma"]])

employees = np.vstack((dept1, dept2))
print("\n12. Employee Records:")
print(employees)

# ============================================
# 13. Split Sales Dataset
# ============================================
sales = np.array([100, 200, 300, 400, 500, 600, 700, 800])

quarters = np.array_split(sales, 4)

print("\n13. Sales Dataset:")
for i, q in enumerate(quarters, 1):
    print(f"Quarter {i}: {q}")

# ============================================
# 14. Train-Test Split
# ============================================
data = np.arange(1, 21)

train, test = np.array_split(data, [16])

print("\n14. Training Data:")
print(train)

print("Testing Data:")
print(test)

# ============================================
# 15. Combine Image Matrices
# ============================================
image1 = np.array([[10, 20],
                   [30, 40]])

image2 = np.array([[50, 60],
                   [70, 80]])

horizontal_image = np.hstack((image1, image2))
vertical_image = np.vstack((image1, image2))

print("\n15. Horizontal Image Combination:")
print(horizontal_image)

print("\nVertical Image Combination:")
print(vertical_image)