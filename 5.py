# 15. Create a function to find the maximum element in a list.

def max_Element(num):
    max = num[0]

    for n in num:
        if n > max:
            max = n
    
    return max

lst = [21 , 2334, 423 ,2323, 42345, 224 ,234, 2532, 2634 ]

result = max_Element(lst)

print("maximum element", result)