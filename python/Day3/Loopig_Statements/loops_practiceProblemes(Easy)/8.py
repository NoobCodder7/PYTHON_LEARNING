# 8. Count the number of digits in a number

num = int(input("Enter a number: "))

count = 0

# Handle the case when the number is 0
if num == 0:
    count = 1
else:
    num = abs(num)  # Convert negative numbers to positive
    while num > 0:
        num //= 10
        count += 1

print("Number of digits =", count)