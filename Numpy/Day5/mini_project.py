import numpy as np

# Create a grayscale image (4 × 4 matrix)
image = np.array([
    [10, 40, 70, 100],
    [30, 60, 90, 120],
    [50, 80, 110, 140],
    [70, 100, 130, 160]
])

# Original Image
print("Original Image:")
print(image)
print("Shape:", image.shape)

# --------------------------------------------------

# 1. Reshape (4×4 → 2×8)
reshaped = image.reshape(2, 8)

print("\nReshaped Image (2 × 8):")
print(reshaped)
print("Shape:", reshaped.shape)

# --------------------------------------------------

# 2. Flatten
flat = image.flatten()

print("\nFlattened Image:")
print(flat)
print("Shape:", flat.shape)

# --------------------------------------------------

# 3. Transpose
transposed = image.T

print("\nTransposed Image:")
print(transposed)
print("Shape:", transposed.shape)

# --------------------------------------------------

# 4. Resize (2 × 10)
resized = np.resize(image, (2, 10))

print("\nResized Image (2 × 10):")
print(resized)
print("Shape:", resized.shape)

# --------------------------------------------------

# 5. Expand Dimensions
expanded = np.expand_dims(image, axis=0)

print("\nExpanded Dimensions:")
print(expanded)
print("Shape:", expanded.shape)

# --------------------------------------------------

# 6. Squeeze Dimensions
squeezed = np.squeeze(expanded)

print("\nSqueezed Dimensions:")
print(squeezed)
print("Shape:", squeezed.shape)