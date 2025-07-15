# -----------------------Function--------------------------------

# Function :- A function in Python is a reusable block of code that performs a specific task. You define it once and use (or "call") it whenever needed.
# def function_name(parameters):
    # code block
    # return result  # (optional)

# example1:
# def hello_func():
    # print("hello world")
# hello_func() # Call the function

# pass :-
# The pass statement is a placeholder. It’s used when a statement is syntactically required, but you don’t want to execute any code yet.
# 🔹 Why Use pass?
# ✅ To create empty functions, classes, loops, or conditionals that you’ll implement later.
# example:
# def hello_func():
    # pass
# hello_func() # method 1: of calling function
# print(hello_func) # method 2: this prints <function hello_func at 0x0000022319A65800> and in this 0x0000022319A65800 is memory address.
# print(hello_func()) # method 3: output will be none


# return :-The return statement is used inside a function to send back a result to the caller. Once return is executed, the function ends immediately.
# example 1:
# def hello_func():
    # return 'Hello function.'
# hello_func() # nothing in ouput.
# print(hello_func()) # when we use print it give output : Hello function.

# example 2: Function Return + String Manipulation or Using Return Value with String Methods
# def hello_func():
    # return 'Hello function.'
# print(hello_func().upper()) # HELLO FUNCTION.

# Parameter and Argument
# Parameter : 	A variable defined inside a function to receive a value. (Placeholder)
# Argument : The actual value passed to a function when you call it.

# example 1 :
# 'name' is a parameter
# def greet(name):
#     print("Hello,", name)
# # 'Rahul' is an argument
# greet("Rahul")

# example 2 :
# def hello_func(greeting):
#     return f"{greeting} Function" # The f stands for "formatted string literal"
# print(hello_func('Hello')) # Hello Function

# example 3 :
# def hello_func(greeting):
#     return '{} Function'.format(greeting)
# print(hello_func('Hello')) # Hello Function

# Default Parameter Value:- In Python, you can assign default values to function parameters. This means if the caller doesn’t provide an argument, the default will be used.
# Syntax:-
# def function_name(parameter=default_value):
    # code block
    
# example 1:
# def greet(name="User"):
    # print("Hello,", name)
# 
# greet()         # Output: Hello, User
# greet("Rahul")  # Output: Hello, Rahul

# example 2:
# def hello_func(greeting, name = "you"):
    # return '{}, {} Function'.format(greeting, name)
# print(hello_func('Hello')) # Hello, you Function

# example 3:
# def hello_fuc(greeting, name="you"):
#     return '{}, {} are you beauty'.format(greeting, name)
# print(hello_fuc('Hi', name="Corey")) # Hi, Corey are you beauty


# ✅ *args → Variable-length positional arguments
# Officially called: “arbitrary positional arguments”
# The * is known as the unpacking operator for positional values.
# example:
# def student_info(*args):
#     print(args)
# student_info("Math", "Art")
# Output: ('Math', 'Art')

# ✅ **kwargs → Variable-length keyword arguments
# Officially called: “arbitrary keyword arguments”
# The ** is known as the unpacking operator for dictionary-style keyword arguments.
# example:
# def student_info(**kwargs):
#     print(kwargs)
# student_info(name = "John", age = 22)
# Output: {'name': 'John', 'age': 22}


# 🧠 Both Together
# You can combine both *args and **kwargs to accept any number of both types of arguments:
# example 1:
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
# student_info("Math", "Art", name = "john", age = 22)
# Output:
# ('Math', 'Art')
# {'name': 'John', 'age': 22}

# example 2:
# def student_info(*args, **kwargs):
    # print(args)
    # print(kwargs)
# 
# courses = ['Math', 'Art']
# info = {'name': 'John', 'age':22}
# set_exam = (234,234,523,1,32,5,2356,7,32)
# student_info(courses, info) # (['Math', 'Art'], {'name': 'John', 'age': 22})
                            # {}
# student_info(courses, set_exam) # (['Math', 'Art'], (234, 234, 523, 1, 32, 5, 2356, 7, 32))
                                # {}


# _____________________Big example 1_____________________________
# Number of days per month. First value placeholder for inidexing purpose.
# month_days = [0, 31, 28, 31, 30, 31, 31, 30, 31, 31, 30, 31, 30, 31 ]

# def is_leap(year):
#     '''Return True for leap years, False for non-leap years.'''
    
#     return year % 4 ==0 and (year % 100 != 0 or year % 400 == 0)

# def days_in_month(year, month):
#     """Return number of days in that month in that year."""
    
#     if not 1 <= month <= 12:
#         return 'Invalid Month'
    
#     if month == 2 and is_leap(year):
#         return 29
    
#     return month_days[month] 
# print(is_leap(2017))
# print(days_in_month(2017, 2))


# _____________________Big example 2_____________________________

# List representing number of hours in each month without DST effect
# month_hours = [0, 744, 672, 744, 720, 744, 720, 744, 744, 720, 744, 720, 744] 
# (i.e., 31*24=744 for Jan, 28*24=672 for Feb, etc.)

# def is_dst(month):
    # '''Return True if the month falls under Daylight Saving Time (Assume Apr–Oct).'''
    # return 4 <= month <= 10

# def hours_in_month(month):
    # """Return number of hours in the month, considering DST."""
    
    # if not 1 <= month <= 12:
        # return 'Invalid Month'
    
    # Assuming DST adds 1 hour per day for months April–October
    # if is_dst(month):
        # Add 1 hour per day in that month
        # days = month_hours[month] // 24
        # return month_hours[month] + days  # Add extra hour for each day
    # return month_hours[month]

# Example usage
# print(is_dst(5))               # True
# print(hours_in_month(2))       # 672
# print(hours_in_month(7))       # 744 + 31 = 775
