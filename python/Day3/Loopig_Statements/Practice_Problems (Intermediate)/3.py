# 13. Find the largest number in a list.

list = [20, 3994, 2234, 2421 ,4443]
largest = list[0]

for num in list:
    if num > largest:
        largest = num 
    
print("Largest number =", largest)