# 1. Print the first **20 Fibonacci numbers**.

a = 0
b = 1

for i in range(1, 21):
    print(a, end=" ")

    c = a+b
    a = b 
    b = c
