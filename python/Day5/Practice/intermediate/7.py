#19. Create a function using `*args` to find the sum of numbers.

def find_sum(*args):
    total = 0

    for num in args:
        total += num

    return total


# Main Program
result = find_sum(10, 20, 30, 40, 50)

print("Sum =", result)