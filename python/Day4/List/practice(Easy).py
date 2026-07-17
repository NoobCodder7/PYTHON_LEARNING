'''
1. Create a list of five fruits.
2. Print the first and last element.
3. Add a new element using `append()`.
4. Insert an element at index 2.
5. Remove an element using `remove()`.
6. Remove the last element using `pop()`.
7. Find the length of a list.
8. Check if an element exists in a list.
9. Print all elements using a loop.
10. Count the occurrences of an element.
'''

#1. Create a list of five fruits.

My_list = ["Mango", "Banana", "Watermelon", "Chickoo", "pear"]
print(My_list)

#2. Print the first and last element.
print(My_list[0])
print(My_list[4])

#3. Add a new element using `append()`.
My_list.append("apple")
print(My_list)

#4. Insert an element at index 2.

My_list.insert(2, "lichi")
print(My_list)
#5. Remove an element using `remove()`.
My_list.remove("lichi")
print(My_list)

#6. Remove the last element using `pop()`.

My_list.pop()
print(My_list)

#7. Find the length of a list.
print("length of the lsit is ", len(My_list))

#8. Check if an element exists in a list.

if "Banana" in My_list:
    print("banana is there")
else:
    print("Not Found")


#9. Print all elements using a loop

for i in My_list:
    print(My_list)


#10. Count the occurrences of an element.
new_list = [ 1, 3,4 ,3 ,2 ,3, 23, 2, 3]
print(new_list.count(3))