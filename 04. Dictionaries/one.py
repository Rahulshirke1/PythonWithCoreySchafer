# Dictionary 
# A dictionary is a collection of key-value pairs. 
# It's unordered (as of Python <3.7), mutable, and indexed by keys,
# which must be unique and immutable (like strings, numbers, or tuples).

# example:
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }
# print(student) # {1: 1, 'name': 'Rahul', 'age': 25, 'courses': ['Math', 'CompSci']}
# print(student['courses']) # ['Math', 'CompSci']

# ---------------------------Mehtods------------------------------

# 1.get() :-  Method in Python (used with dictionaries)
# :- The get() method is used to safely access the value of a key in a dictionary without raising an error if the key doesn't exist.
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }
# print(student.get('age')) # 25
# print(student.get('phone')) #None
# print(student.get('skills', 'There are no skills')) # There are no siklls


# 2. One way to add an element in dictionary.
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }
# student['phone'] = '555-555'
# print(student['phone']) # 555-555
# print(student) # {1: 1, 'name': 'Rahul', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-555'}



# 3. update() :-The update() method is used to add new key-value pairs or update existing ones in a dictionary.
# print(student)
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }
# student.update({'name':'Jane', 'age':21, 'tutorail':'python'})
# print(student) # {1: 1, 'name': 'Jane', 'age': 21, 'courses': ['Math', 'CompSci'], 'tutorail': 'python'}

# 4. del() :-The del statement is used to delete elements from:
# Dictionaries
# Lists
# Variables
# Objects
# example 1:
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }
# del student['age'] # delete the age from student dictionary
# print(student) # {1: 1, 'name': 'Rahul', 'courses': ['Math', 'CompSci']}

# example 2:
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }
# del(student) # Deletes the student dictionary
# print(student) # errors as student dictionary doesn't exists anymore.

 
# pop() :-The pop() method is used to:
# Remove a key-value pair from a dictionary
# Return the value of the removed key
# Syntax:- dict.pop(key, default)
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }
# age = student.pop('age')
# print(age) # 25
# print(student) # {1: 1, 'name': 'Rahul', 'courses': ['Math', 'CompSci']}


# len() :- The len() function is used to get the number of items in an object.
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }
# print(len(student)) # 4

# keys()
# :-🔑 keys() Method in Python (for dictionaries)
# The keys() method is used to get a view object that displays all the keys in a dictionary.
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }
# print(student.keys()) # dict_keys([1, 'name', 'age', 'courses'])

# values():- The values() method returns a view object that contains all the values from a dictionary.
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }
# print(student.values()) # dict_values([1, 'Rahul', 25, ['Math', 'CompSci']])

# items() :- The items() method returns a view object that contains key-value pairs as tuples from the dictionary.
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }
# print(student.items()) # dict_items([(1, 1), ('name', 'Rahul'), ('age', 25), ('courses', ['Math', 'CompSci'])])

# -------------------------------looping in dictionaries-------------------------------------
# example 1: using normal for loop
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }
# for key in student:
    # print(key) # It will provide us only the keys.
# 1
# name
# age
# courses

# example 2: In order to get both key and value we can use items method in loop.
# student = {
#     1:1,
#     "name": "Rahul",
#     "age" : 25,
#     "courses":['Math', "CompSci"]
# }

# for key, value in student.items():
#     print(key, value)
