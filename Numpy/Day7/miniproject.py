import numpy as np

# ==========================================
# Mini Project: Student Database Analysis
# ==========================================

# Create a marks dataset
marks = np.array([78, 92, 45, 67, 89, 92, 34, 56, 78, 99, 21, 65, 45, 88, 73])

print("Original Marks Dataset:")
print(marks)

# ==========================================
# 1. Sorting
# ==========================================
print("\n1. Sorted Marks (Ascending):")
print(np.sort(marks))

print("\nSorted Marks (Descending):")
print(np.sort(marks)[::-1])

# ==========================================
# 2. Searching
# ==========================================
search_mark = 92

if search_mark in marks:
    print(f"\n2. {search_mark} is present in the dataset.")
    print("Index Positions:", np.where(marks == search_mark)[0])
else:
    print(f"\n2. {search_mark} is not present.")

# ==========================================
# 3. Filtering
# ==========================================
print("\n3. Marks Greater Than 50:")
print(marks[marks > 50])

# ==========================================
# 4. Unique Values
# ==========================================
print("\n4. Unique Marks:")
print(np.unique(marks))

# ==========================================
# 5. Highest Marks
# ==========================================
print("\n5. Highest Marks:")
print(np.max(marks))

# ==========================================
# 6. Lowest Marks
# ==========================================
print("\n6. Lowest Marks:")
print(np.min(marks))

# ==========================================
# 7. Students Above 80
# ==========================================
above_80 = marks[marks > 80]

print("\n7. Students Scoring Above 80:")
print(above_80)
print("Count:", len(above_80))

# ==========================================
# 8. Passing Students (Marks >= 35)
# ==========================================
passing = marks[marks >= 35]

print("\n8. Passing Students:")
print(passing)
print("Count:", len(passing))

# ==========================================
# 9. Count Failures (Marks < 35)
# ==========================================
failures = marks[marks < 35]

print("\n9. Failed Students:")
print(failures)
print("Count:", len(failures))

# ==========================================
# 10. Find Duplicate Marks
# ==========================================
unique, counts = np.unique(marks, return_counts=True)
duplicates = unique[counts > 1]

print("\n10. Duplicate Marks:")
print(duplicates)

# ==========================================
# Dataset Summary
# ==========================================
print("\n========== Dataset Summary ==========")
print("Total Students :", marks.size)
print("Highest Marks  :", np.max(marks))
print("Lowest Marks   :", np.min(marks))
print("Average Marks  :", np.mean(marks))
print("Passing Count  :", np.count_nonzero(marks >= 35))
print("Failure Count  :", np.count_nonzero(marks < 35))
print("Unique Marks   :", len(np.unique(marks)))
print("====================================")