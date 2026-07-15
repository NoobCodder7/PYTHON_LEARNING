# 9. Find the sum of all even numbers from **1 to 100**.


sum = 0

for i in range(2, 101, 2):
    sum += i

print("Sum of even numbers from 1 to 100 is:", sum)