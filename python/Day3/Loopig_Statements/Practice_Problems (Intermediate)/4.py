# 14. Find the smallest number in a list.

number = [203 , 2323 ,42, 129, 1,21]
smallest = number[0]

for num in number:
    if num < smallest:
        smallest = num 
    
print("The samallest number is", smallest)
