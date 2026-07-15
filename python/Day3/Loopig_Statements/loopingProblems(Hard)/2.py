# 2. Find all Armstrong numbers between **1 and 1000**.

for num in range(1 , 1001):
    digits = str(num)
    power = len(digits)

    total = 0

    for digit in digits:
        total += int(digit)**power

        if total == num:
            print(num)