'''11. Find the largest element in a list.
12. Find the smallest element in a list.
13. Find the sum of all elements.
14. Find the average of all elements.
15. Reverse a list.
16. Sort a list in ascending order.
17. Sort a list in descending order.
18. Copy a list.
19. Merge two lists.
20. Remove duplicate elements from a list.
'''
 

list = [15, 8, 45, 22, 10]
print(max(list))


print(min(list))

print(sum(list))

print(sum(list) / len(list))

list.reverse()
print(list)

list.sort()

print(list)

list.sort(reverse=True)
print(list)


list2 = list.copy()
print("Original:", list)
print("Copied:", list2)


list3 = [2, 34, 22, 10, 15]
print(list3)

list3 = list3 + list
print(list3)

unique_numbers = set(list3)

print(unique_numbers)
