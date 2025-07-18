#  Numbers
# num = 3
# print(type(num)) #<class 'int'>

# Arithmethic Operators:
# Addition:       3 + 2
# Subtraction:    3 -2 
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2 # 3 rase to 2
# Modulus:        3 % 2

# print(3 + 2)
# print(3 -2 )
# print(3 * 2)
# print(3 / 2)
# print(3 // 2)
# print(3 ** 2)
# print(3 % 2)

# arithmetic expression in Python
# print(3 * (2 + 1))

# variable reassignment and incrementing a variable
# example 1:
# num = 1
# num = num + 1
# print(num) # 2

# example 2:
# num = 1
# num *= 5
# num /= 5
# num %= 5
# num -= 5
# num += 5
# print(num) # 5


#Comparison:
# Equal:-            3 == 2
# Not Equal:-        3 != 2
# Greater Than:-     3 > 2
# Less Than:-        3 < 2
# Greater or Equal:- 3 >= 2
# less or Equal:-    3 <= 2

# print(3 == 2)
# print(3 != 2 )
# print(3 > 2)
# print(3 < 2)
# print(3 >= 2)
# print(3 <= 2)


# --------------------Number Methods-----------------

# 1. abs(number) 
# -> The absolute value of a number is its distance from 0, regardless of direction.
# print(abs(-3))
# print(abs(3 + 4j))#n Python, j is used to represent the imaginary unit (just like i in math)
# 3 + 4j
# 3 + 4j
# is a complex number, where:
# Real part = 3
# Imaginary part = 4

# 2. round() 
# -> The round() function returns a number rounded to a specified number of decimal places.
# round(number[, ndigits])
# number: The number you want to round.
# ndigits (optional): The number of digits to round to after the decimal point.

# example1:
# print(round(3.75))
# print(round(3.75, 1))

# 3. sum() :- Returns the sum of elements in an iterable (like a list)
# print(sum([1, 2, 3, 4]))  # 10

# 4. max() and min()
# Returns the maximum or minimum of the given values.
# print(max(5, 10, 2))  # 10
# print(min(5, 10, 2))  # 2



# ---------- Type Casting-------
# num_1 = '100'
# num_2 = '200'
# print(num_1 + num_2) # output: 100200
# # convert the num_1 and num_2 into number
# num_1 = int(num_1)
# num_2 = int(num_2)
# # print(type(num_1)) #<class 'int'>
# print(num_1 + num_2) # 300

# -------------Random ---------------

# Random
# ->The random module provides functions to generate random numbers and perform random actions like picking an item from a list.

import random

# 1. random.random()
# Returns a random float between 0.0 and 1.0
# print(random.Random()) # <random.Random object at 0x000002091F0DE070>
# print(random.random()) # 0.16017148204546217
# print(random.random()* 10) #4.278125181792167
# print(round(random.random())) # It will return 1 or 0.
# print(round(random.random()*10)) # this is one method which can generate randome number till 10.


# 2. random.randint(a, b)
# Returns a random integer between a and b (inclusive).
# print(random.randint(1, 6))  # Like rolling a dice (1 to 6)

