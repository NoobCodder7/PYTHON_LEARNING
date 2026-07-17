'''
1. Create a set of five numbers.
2. Add an element using `add()`.
3. Add multiple elements using `update()`.
4. Remove an element using `remove()`.
5. Remove an element using `discard()`.
6. Remove a random element using `pop()`.
7. Print all elements using a loop.
8. Check whether an element exists in a set.
9. Find the length of a set.
10. Copy a set.

---

## Intermediate

11. Find the union of two sets.
12. Find the intersection of two sets.
13. Find the difference of two sets.
14. Find the symmetric difference of two sets.
15. Find the maximum element.
16. Find the minimum element.
17. Find the sum of all elements.
18. Remove duplicates from a list using a set.
19. Convert a set into a list.
20. Clear all elements from a set.'''




numbers = {1, 2, 3, 4, 5}
print(numbers)

numbers.add(6)
print(numbers)

numbers.update([7,8,9,10])
print(numbers)

numbers.remove(5)
print(numbers)

numbers.discard(10)
print(numbers)

numbers.pop()
print(numbers)

for num in numbers:
    print(num)


    if 30 in numbers:
        print("30 Found")
else:
    print("30 Not Found")

    print(len(numbers))

    set2 = numbers.copy()


    #--------------------------------------------------------------INTERMEDIATE--------------------------------------------------

A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))



numbers = {10, 40, 20, 60, 30}

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

unique_numbers = list(set(numbers))

print(unique_numbers)


numbers_list = list(numbers)

print(numbers_list)


numbers2 = {10, 20, 30, 40, 50}

numbers.clear()

print(numbers)