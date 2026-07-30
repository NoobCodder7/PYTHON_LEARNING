import numpy as np

# ==========================================
# Mini Project: Employee Department Dataset
# ==========================================

# Step 1: Create salary arrays for three departments
HR = np.array([30000, 35000, 40000, 45000])
IT = np.array([50000, 55000, 60000, 65000])
Sales = np.array([28000, 32000, 36000, 40000])

print("HR Department Salaries:")
print(HR)

print("\nIT Department Salaries:")
print(IT)

print("\nSales Department Salaries:")
print(Sales)

# ==========================================
# Step 2: Join all department salary arrays
# ==========================================

all_salaries = np.concatenate((HR, IT, Sales))

print("\nJoined Salary Dataset:")
print(all_salaries)

# ==========================================
# Step 3: Split the joined dataset
# ==========================================

split_data = np.array_split(all_salaries, 3)

print("\nSplit Salary Dataset:")

for i, dept in enumerate(split_data, start=1):
    print(f"Department {i}: {dept}")

# ==========================================
# Step 4: Stack the department arrays
# ==========================================

stacked_data = np.stack((HR, IT, Sales))

print("\nStacked Department Dataset:")
print(stacked_data)

# ==========================================
# Step 5: Print Final Dataset Information
# ==========================================

print("\nFinal Dataset Shape:", stacked_data.shape)
print("Number of Dimensions:", stacked_data.ndim)
print("Total Elements:", stacked_data.size)
print("Data Type:", stacked_data.dtype)