import numpy as np

# ==========================================
# 1. Sort an Array
# ==========================================
arr = np.array([45, 12, 78, 34, 90, 23])

print("1. Sorted Array:")
print(np.sort(arr))

# ==========================================
# 2. Sort in Descending Order
# ==========================================
print("\n2. Descending Order:")
print(np.sort(arr)[::-1])

# ==========================================
# 3. Find Unique Values
# ==========================================
arr = np.array([10, 20, 20, 30, 40, 40, 50])

print("\n3. Unique Values:")
print(np.unique(arr))

# ==========================================
# 4. Find Duplicate Values
# ==========================================
unique, counts = np.unique(arr, return_counts=True)
duplicates = unique[counts > 1]

print("\n4. Duplicate Values:")
print(duplicates)

# ==========================================
# 5. Search Where Value > 50
# ==========================================
arr = np.array([20, 55, 40, 75, 90, 30])

print("\n5. Values Greater Than 50:")
print(arr[arr > 50])

# ==========================================
# 6. Find Non-Zero Values
# ==========================================
arr = np.array([0, 5, 0, 7, 9, 0, 2])

print("\n6. Non-Zero Indices:")
print(np.nonzero(arr))

# ==========================================
# 7. Count Non-Zero Elements
# ==========================================
print("\n7. Count of Non-Zero Elements:")
print(np.count_nonzero(arr))

# ==========================================
# 8. Check if 20 Exists
# ==========================================
arr = np.array([10, 20, 30, 40])

print("\n8. Does 20 Exist?")
print(20 in arr)

# ==========================================
# 9. Find Sorted Indices
# ==========================================
arr = np.array([40, 10, 30, 20])

print("\n9. Sorted Indices:")
print(np.argsort(arr))

# ==========================================
# 10. Insert Value Using searchsorted()
# ==========================================
arr = np.array([10, 20, 30, 40, 50])

index = np.searchsorted(arr, 35)

print("\n10. Insert Position for 35:")
print(index)

# ==========================================
# 11. Remove Duplicate Values
# ==========================================
arr = np.array([1, 2, 2, 3, 4, 4, 5])

print("\n11. Remove Duplicates:")
print(np.unique(arr))

# ==========================================
# 12. Sort Rows Independently
# ==========================================
matrix = np.array([[30, 10, 20],
                   [90, 50, 70],
                   [60, 80, 40]])

print("\n12. Rows Sorted:")
print(np.sort(matrix, axis=1))

# ==========================================
# 13. Sort Columns Independently
# ==========================================
print("\n13. Columns Sorted:")
print(np.sort(matrix, axis=0))

# ==========================================
# 14. Find Students Scoring Above 80
# ==========================================
marks = np.array([65, 85, 90, 72, 88, 45])

print("\n14. Students Scoring Above 80:")
print(marks[marks > 80])

# ==========================================
# 15. Find Salaries Greater Than Average
# ==========================================
salaries = np.array([30000, 45000, 60000, 75000, 50000])

average = np.mean(salaries)

print("\n15. Salaries Greater Than Average:")
print(salaries[salaries > average])

# ==========================================
# 16. Count Students Passing
# ==========================================
marks = np.array([25, 40, 65, 80, 30, 55])

passing = np.count_nonzero(marks >= 35)

print("\n16. Students Passing:")
print(passing)

# ==========================================
# 17. Find All Even Numbers
# ==========================================
arr = np.arange(1, 21)

print("\n17. Even Numbers:")
print(arr[arr % 2 == 0])

# ==========================================
# 18. Filter Employees with Salary Above ₹50,000
# ==========================================
salaries = np.array([25000, 45000, 55000, 65000, 80000])

print("\n18. Salaries Above ₹50,000:")
print(salaries[salaries > 50000])

# ==========================================
# 19. Check if All Marks are Above 35
# ==========================================
marks = np.array([40, 60, 75, 80, 50])

print("\n19. Are All Marks Above 35?")
print(np.all(marks > 35))

# ==========================================
# 20. Check if Any Employee Earns Above ₹100,000
# ==========================================
salaries = np.array([40000, 55000, 70000, 120000, 85000])

print("\n20. Any Employee Earning Above ₹100,000?")
print(np.any(salaries > 100000))