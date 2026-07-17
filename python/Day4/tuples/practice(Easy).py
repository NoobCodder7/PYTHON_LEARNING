'''
1. Create a tuple of five numbers.
2. Print the first and last element.
3. Print the third element.
4. Find the length of a tuple.
5. Count the occurrences of an element.
6. Find the index of an element.
7. Check whether an element exists.
8. Print all elements using a loop.
9. Find the maximum value.
10. Find the minimum value.
'''

tuple = (1 ,23 ,34, 3, 53)

print(tuple[0], tuple[4], tuple[2])

print("lenght of tuple" ,len(tuple))

print(tuple.count(3))

print(tuple.index(23))

if 3 in tuple:
    print("YES")
else:
    print("False")

for num in tuple:
    print(num)

print(max(tuple))

print(min(tuple))