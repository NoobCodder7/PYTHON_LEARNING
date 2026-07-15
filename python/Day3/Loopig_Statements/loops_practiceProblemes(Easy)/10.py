#10. Check whether a number is a palindrome.

num = int(input("Enter a number:"))

reverse = 0
orignal = num

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if orignal == reverse:
    print("The num is palindrom")
else:
    print("The number is not a plindrom,")
