#14. Check whether a number is an Armstrong number.
#An Armstrong number (also called a Narcissistic number) is a number that is equal to the sum of its digits, where each digit is raised to the power of the total number of digits.

num = int(input("Enter a number: "))

original = num
digits = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print(original, "is an Armstrong number.")
else:
    print(original, "is NOT an Armstrong number.")