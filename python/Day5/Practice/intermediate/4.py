#14. Create a function to find the sum of a list.

def list_Sum(numbers):
    total = 0 
    
    for num in numbers:
        total += num

    return total

lis = [122, 324, 212, 423, 213, 1234, 211]

result = list_Sum(lis)

print("List:", lis)
print("sum:", result)