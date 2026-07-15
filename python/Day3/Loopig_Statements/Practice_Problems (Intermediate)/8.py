# 20. Find the GCD (Greatest Common Divisor) of two numbers.


num_1 = int(input("Enter a number 1 "))
num_2 = int(input("Enter a number 2 "))

gcd = 1 

for i in range(1 , min(num_1, num_2) + 1):
    if num_1 % i == 0 and num_2 % i == 0:
        gcd = i

print("The greateast common Divisor is ", gcd)