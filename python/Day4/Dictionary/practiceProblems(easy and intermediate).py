'''1. Create a dictionary for a student.
2. Print the value of a key.
3. Add a new key-value pair.
4. Update an existing value.
5. Remove a key using `pop()`.
6. Remove a key using `del`.
7. Print all keys.
8. Print all values.
9. Print all key-value pairs using a loop.
10. Check whether a key exists.
'''

student = {
    "name": "Viraj",
    "age": 20,
    "course": "Python"
}
print(student)

print(student["name"])
print(student["age"])
print(student["course"])

student["city"] = "Valsad"

print(student)

student["age"] = 21
print(student)

student.pop("city")
print(student)
del student["age"]
print(student)

for key in student.keys():
    print(key)

for val in student.values():
    print(val)


    for key, val in student.items():
        print(key, ":", val)

if "age" in student.keys():
    print("Key found")
else:
    print("Key not found")



## Intermediate

'''11. Count the number of key-value pairs.
12. Copy a dictionary.
13. Clear a dictionary.
14. Create a nested dictionary.
15. Access a value from a nested dictionary.
16. Merge two dictionaries.
17. Find the maximum value in a dictionary.
18. Find the minimum value in a dictionary.
19. Find the sum of all values in a dictionary.
20. Create a dictionary from two lists.'''



print("Total Keys:", len(student))

new_dict = student.copy()
print(new_dict)

student.clear()
print(student)


students = {
    "student1": {
        "name": "Viraj",
        "age": 20
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    }
}

print(students)




print(students["student1"]["name"])
print(students["student2"]["age"])


dict1 = {
    "a" : 1,
    "b": 3
}

dict2 = {
    "c" : 4,
    "d" : 20
}

dict3 = dict1 | dict2

print(dict3)



marks = {
    "Math": 85,
    "Science": 92,
    "English": 78
}

print("Maximum Marks:", max(marks.values()))




marks = {
    "Math": 85,
    "Science": 92,
    "English": 78
}

print("Minimum Marks:", min(marks.values()))


marks = {
    "Math": 85,
    "Science": 92,
    "English": 78
}

print("Total Marks:", sum(marks.values()))


keys = ["name", "age", "course"]
values = ["Viraj", 20, "Python"]

student = dict(zip(keys, values))

print(student)