# ------------------------lambda---------------------------
# 🔍 What is lambda in Python?
# A lambda is a small anonymous function in Python.
# It’s used when you need a quick function but don’t want to formally define it with def.

# ✅ Syntax:
# lambda arguments: expression

# lambda – keyword
# arguments – input(s) to the function
# expression – the single expression the function returns

# example 1:
# square = lambda n: n * n
# print(square(5))
# This is equivalent to:
# def square(n):
#     return n * n

# example 2:
# add = lambda a, b: a + b
# print(add(3, 4)) # output: 7

# 🔄 Where is lambda useful?
# When you need a short, throwaway function
# Commonly used with functions like:
# map()
# filter()
# sorted()

# lambda example with map:
# nums = [1, 2, 3]
# square = list(map(lambda x: x *x, nums))
# print(square)  # [1, 4, 9]

# ⚠️ Limitations:
# lambda can only have one expression
# You can’t write multiple lines or statements inside it


# ---------------------Comprehensions-----------------

# example 1:
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# # I want 'n' for each 'n' in in nums
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# List comprehension of example 1:
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# my_list = [n for n in nums] # List comprehension
# print(my_list)
# explanation:
# means:
# For each element n in the list nums,
# Add n to the new list my_list.
# output:- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# example 2:
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# I want n*n for each 'n' in nums
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)
# output:-[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List comprehension of example 2:
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# my_list = [n*n for n in nums]
# print(my_list)

# List comprehension of example 2 with map
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# Using a map + lambda
# my_list = map(lambda n: n*n, nums)
# exaplation:
# map() – a built-in Python function that applies a function to each item in an iterable (like a list).
# lambda n: n*n – an anonymous function that takes a number n and returns its square (n * n).
# So this line means:
# 👉 “Take each number in nums, square it, and return a new object containing those squared values.”

# But important note:
# The result of map() is a map object (not a list). It's a special iterable that you can loop over, but you won't see the values directly unless you convert it to a list.
# print(my_list) # output:- <map object at 0x000002264B570F10> Because my_list is a map object.
# print(list(my_list)) # It first need to be converted into list
# output:-[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# example 3:
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# # I want 'n' for each 'n' in nums if 'n' is even.
# my_list = []
# for n in nums:
#     if n % 2 ==0:
#         my_list.append(n)
# print(my_list)
# output:- [2, 4, 6, 8, 10]

# List comprehension of example 3
# ex1:
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# my_list = [n % 2 == 0 for n in nums]
# print(my_list) 
# output:- [False, True, False, True, False, True, False, True, False, True]
# ex2:
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)
# output:- [2, 4, 6, 8, 10]

# List comprehension of example 3 with filter
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# my_list = list(filter(lambda n: n % 2 == 0, nums))
# print(my_list) 

# example 4:
# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)
# output:-[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]

# List Comprehension of example 4:
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)
# output:-[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]

# example 5:
# ex1:
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman']
# print(dict(zip(names, heros)))
# output:- {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman'}

# ex2:
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman']
# I want a dict{'name':'hero'} for each name, hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)
# explanation:

# ✅ zip(names, heros):
# The zip() function combines the two lists pairwise.
# It will create pairs like:
# ('Bruce', 'Batman')
# ('Clark', 'Superman')
# ('Peter', 'Spiderman')
# Note: zip() stops at the shortest list, so 'Logan' and 'Wade' are ignored.

# ✅ Loop:
# You're creating a dictionary where each name maps to a hero:
# 'Bruce' → 'Batman'
# 'Clark' → 'Superman'
# 'Peter' → 'Spiderman'

# my_dict[name] = hero
# This line is saying:
# "Take the variable name as a key"
# "Assign it the value hero in the dictionary my_dict"

# output:-{'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman'}

# Dictionary Comperhensions

# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman']
# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)

# If name not equal to peter
# my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(my_dict)


# example 6:
# nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
# set is a non repitative data type
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)
# output:- {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Set Comprehensions
# my_set = {n for n in nums}
# print(my_set)

#----------------------Generator Expressions----------------------
# I wnat to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,10] 

def gen_func(nums):
    for n in nums:
        yield n*n
# 🔍 What is yield?
# | `return`                       | `yield`                              |
# | ------------------------------ | ------------------------------------ |
# | Exits the function immediately | Pauses the function, keeps its state |
# | Returns a single value         | Returns a **generator** (lazy)       |
# | Can’t resume later             | Can resume where it left off         |
# | Used in normal functions       | Used in **generator functions**      |

my_gen = gen_func(nums)
print(set(my_gen))