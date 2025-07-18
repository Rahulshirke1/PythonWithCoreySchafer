# 1. print message
# message = 'Hello World'
# print(message)

# 2. print message (It will through an error)
# message = 'Rahul's World'
# print(message)
#   File "c:\2022-2023\All the python program\Corey Schafer\learning\1.strings\one.py", line 6
#     message = 'Rahul's World'
#                             ^
# SyntaxError: unterminated string literal (detected at line 6)

# 3. To solve upper problem we can use this method 
# message = """ Booby's World was a good cartoon in the 1990's """
# print(message)

# Length of String
# To find the lenght of (array, string, object) we use len() method.
# message = 'hello World'
# print(len(message)) # It will work. ()
# print(len message) # It will cause an Error.
# print(message[8]) # r is output


# Slicing: Here we are taking a part of an string through index value.
# message = 'hello World'
# print(message[2:7]) # We can insert starting and ending value of the string which we want.

#----------------------Methods--------------

# 1. lower() - Makes the string small letters
# message = 'hello WORLD'
# print(message.lower()) # hello world

# 2. upper() - Makes the string Capital letters
# message = 'hello World'
# print(message.upper()) # HELLO WORLD

# 3. count() - If we want to count certern number of words in our string.
# message = 'Hello World'
# print(message.count()) # This will give you error
# print(message.count('Hello')) # 1
# print(message.count('l')) #3

# 4. find() - If we want to find the index of where certain characters can be found.
# message = 'Hello World'
# print(message.find('World')) # 6
# print(message.find('world')) # -1
# This searches for 'world' (all lowercase), but since the string contains 'World' with a capital W, it's not found.
# Therefore, .find() returns -1, which means "not found".

# 5. replace - It is used to replace the worlds/string in variable.
# message = 'Hello World'
# message = message.replace('World', 'Universe')
# print(message) # Hellow Universe


# 6. concatination of straing - concatination means combining.Which means combining string.
# example 1:
# greeting = 'hello'
# name = 'Michael'
# message = greeting+ name
# print(message) # helloMichael

# example 2:
# greeting = 'hello'
# name = 'Michael'
# message = greeting+ ", " + name
# print(message) # hello, Michael

#example 3:
# name = 'Michael'
# greeting = 'hello'
# message = greeting+ ", " + name + ' Welcome!'
# print(message) # hello, Michael Welcome!

#example 4:
# greeting = 'hello'
# name = 'Michael'
# message = '{}, {}. Welcome'.format(greeting, name)
# print(message) # hello, Michael. Welcome

#example 5: f strings
# name = 'Michael'
# greeting = 'hello'
# message = f'{greeting}, {name}!'
# print(message) # hello, Michael!

#example 6: practicse for f string
# name = 'Michael'
# greeting = 'hello'
# message = f'{greeting.upper()}, {name}!'
# print(message) # hello, Michael!

# 7. dir() method
# The dir() function in Python is a built-in utility that helps you inspect the attributes (methods, variables, etc.) of:
# an object,
# a module, or
# any variable.
# example: 
# greeting = 'Hello'
# name = 'Michael'
# print(dir(name))

# output:['__add__', '__class__', '__contains__', '__delattr__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
# '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
# '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', 
# '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 
# 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
# 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
# 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 
# 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
# 'translate', 'upper', 'zfill']


# 8. help() method
# The help() function in Python is your built-in documentation assistant 🧠📘.
# It gives you a detailed description of:
# Modules
# Functions
# Classes
# Methods
# Objects
# example
# print(help(str))

print('Hello World'.count('l'))     # 3