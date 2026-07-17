'''11. Find the sum of all elements.
12. Find the average of all elements.
13. Convert a tuple into a list.
14. Convert a list into a tuple.
15. Concatenate two tuples.
16. Repeat a tuple three times.
17. Create a nested tuple and access an element.
18. Count duplicate elements in a tuple.
19. Find the second largest element in a tuple.
20. Remove duplicates by converting the tuple to a set.'''


tuple = (2 ,4 ,53, 23 , 443, 32 ,532 ,234,43,)
print(tuple)


sum = sum(tuple)
print(sum)

average = sum / len(tuple)
print(average)

list1 = list(tuple)
print(type(list1))

numbers = [10, 20, 30, 40, 50]

numbers_tuple = tuple(numbers)

print(numbers_tuple)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2

print(tuple3)

numbers = (1, 2, 3)

print(numbers * 3)


matrix = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90)
)

print(matrix[1][2])


numbers = (10, 20, 20, 30, 20, 40)

print("20 appears", numbers.count(20), "times")


numbers = (10, 40, 25, 60, 35)

unique_numbers = sorted(set(numbers))

print("Second Largest:", unique_numbers[-2])


numbers = (10, 20, 20, 30, 40, 40, 50)

unique_numbers = tuple(set(numbers))

print(unique_numbers)