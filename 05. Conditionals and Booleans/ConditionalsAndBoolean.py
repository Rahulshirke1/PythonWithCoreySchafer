# ---------------------Conditionals------------------

# Comparisions:
# Equal:            ==
# Not Equal:        !=
# Greater Than      >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <= 
# Object identity:  is

# if statement :-  if statement is used to make decisions in your code — it allows you to execute a block of code only if a certain condition is true.
# Basic Syntax:
# if condition:
    # code to run if condition is true


# basic examples:
# if True:
#     print('Conditional was True') # Conditional was True
# if False:
#     print('Conditional was True') # No Output

#  example 1:
# language = 'Python'
# if language == 'Python':
#     print('Conditinoal was True') # Conditional was True


# else :- The else block is used along with if (or if-elif) to run code when none of the if or elif conditions are True.
# Basic Syntax:
# if condition:
    # runs if condition is true
# else:
    # runs if condition is false

# example 1:
# language = 'Python'
# if language == 'Python':
#     print('Language is Python')
# else:
#     print('No Match') 
# output:- Language is Python

# example 2:
# language = 'Java'
# if language == 'Python':
#     print('Language is Python')
# else:
#     print('No Match') 
# output:- No Match

# elif :- The elif (short for "else if") is used when you want to check multiple conditions. It allows you to run different blocks of code depending on which condition is True.
# Basic Syntax:
# if condition1:
    # runs if condition1 is true
# elif condition2:
    # runs if condition2 is true
# elif condition3:
    # runs if condition3 is true
# else:
    # runs if none of the above conditions are true

#example 1: 
# language = 'Java'
# if language == 'Python':
#     print('Language is Python')
# elif language == 'Java':
#     print('Language is Java')
# else:
#     print('No Match') 
# output:- Language is Java

#example 2: 
# language = 'Java'
# if language == 'Python':
#     print('Language is Python')
# elif language == 'Java':
#     print('Language is Java')
# elif language == 'JavaScript':
#     print('Language is JavaScript')
# else:
#     print('No Match') 
# output:- Language is Java

# example:
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b) # True # a == b checks if the values inside the lists are the same.
# print(a is b) # False # a is b checks whether both variables point to the same object in memory.

# id() :-The id() function returns the unique identity (memory address) of an object during its lifetime.
# example 1:
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(id(a)) # memory address : 2280337150144
# print(id(b)) # memory address : 2280338587264

# example 2:
# a = [1, 2, 3]
# b = a
# print(id(a)) # memory address : 1475481669824
# print(id(b)) # memory address : 1475481669824
# print(a is b) # True as both variable point to the same object in memory.
# print(id(a) == id(b)) # True

 # False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# example 1:
# condition = False
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')
# output:- Evaluated to False

# example 2:
# condition = None
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')
# output:- Evaluated to False

# example 3:
# condition = 0 # if the value of condition is 0 then it would turnout false.
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')
# output:- Evaluated to False

# example 4:
# condition = -1 or 1 # if the value of condition is greater or lesser then 0, then it would turnout to be true.
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')
# output:- Evaluated to True

# example 4:
# condition = () or '' or {} or [] # Any empty string, sets, list, dictionary is False.
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')
# output:- Evaluated to False

# example 4:
# condition = ("Rahul", "anil") or 'riya' or {"age":20, "color":"red"} or [88,238, "string", ["jj"]] # Any non-empty string, sets, list, dictionary is True.
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')
# output:- Evaluated to True

# --------------------------Boolean------------------------


# 1. and :-The and operator is a logical operator used to combine multiple conditions.
# It returns True only if all conditions are true.
#  Basic Syntax:
# if condition1 and condition2:
    # runs only if both condition1 and condition2 are True
# example 1:
# user = 'Admin'
# logeed_in = True

# if user == 'Admin' and logeed_in:
#     print('Admin Page')
# else:
#     print('Bad Creds')
# output:- Admin Page

# example 2:
# user = 'Admin'
# logeed_in = False 

# if user == 'Admin' and logeed_in:
#     print('Admin Page')
# else:
#     print('Bad Creds')
# output:- Bad Creds


# 2. and :- The or operator is a logical operator used when at least one condition must be true.
# It returns True if any one conditions are true.
#  Basic Syntax:
# if condition1 or condition2:
    # runs if either condition1 OR condition2 is True
# example 1:
# user = 'Admin'
# logeed_in = False 

# if user == 'Admin' or logeed_in:
#     print('Admin Page')
# else:
#     print('Bad Creds')
# output:- Admin Page

# 3. not :- The not operator is a logical negation operator.
# It reverses the Boolean value of a condition:
# not True becomes False
# not False becomes True

#  Basic Syntax:
# if not condition:
    # runs if condition is False
# example 1:
# user = 'Admin'
# logeed_in = False 
# if not logeed_in:
#     print("Please Log in")
# else:
#     print('welcome')
# output:- Please Log in


