# Variable Scope
# ChatGPT said:
# In Python, variable scope refers to the region of your code where a variable is recognized and can be accessed or modified.
# Python uses a specific set of rules to determine which variable is accessible at a given point in your code. 
# This concept is managed by what’s called the LEGB Rule.

# 🔍 What is Variable Scope?
# Variable scope determines the visibility and lifetime of a variable. In Python, there are four main types of scopes:
# Local – inside a function or block
# Enclosing – inside nested functions
# Global – at the top level of a script or module
# Built-in – provided by Python itself

# 🧭 The LEGB Rule
# LEGB stands for:
# L – Local
# E – Enclosing
# G – Global
# B – Built-in
# Python searches for a variable in this order when trying to resolve its name.

# example1:
# x = 'Global x'

# def test():
#     y = 'Local y'
#     print(y)
    
# test()

# example2:
# x = 'Global x' 

# def test():
#     y = 'Local y'
#     print(x) # Global x
# test()

# example3:
# x = 'Global x' 

# def test():
#     y = 'Local y'
#     print(x) # Global x
# test()
# print(y) # NameError: name 'y' is not defined

# example4:
# x = 'Global x'

# def test():
    # x = 'Local x'
    # print(x) # Global x
# test()
# print(x)
# output:- 
# Local x
# Global x

# example5:
# x = 'Global x' 

# def test():
#     global x
#     x = 'Local x'
#     print(x) # Global x
# test()
# print(x)
# output:-
# Local x
# Local x

# example6:
# x = 'Global x' 

# def test(z):
#     print(z in globals()) # False
#     print(z in locals()) # True

# test("Local z")

# example7:  Built-in (B)
# Names that are predefined in Python.
# print(len("hello"))  # 'len' is a built-in function

# example8:
# def outer():
#     x = 'outer x'
    
#     def inner():
#         x = 'inner x'
#         print(x)
        
#     inner()
#     print(x)
    
# outer()
# output:-
# inner x 
# outer x

# example9:
# def outer():
#     x = 'outer x'
    
#     def inner():
#         print(x)
        
#     inner()
#     print(x)
    
# outer()
# output:-
# outer x 
# outer x

# example9:
# x = "Global x"
# def outer():
#     x = 'outer x'
#     print(x)
    
#     def inner():
#         print(x)
        
#     inner()
#     print(x)
    
# outer()
# print(x)
# output:-
# outer x
# outer x
# outer x
# Global x

# example9:
x = "Global x"
def outer():
    print(x)
    
    def inner():
        print(x)
        
    inner()
    print(x)
    
outer()
print(x)
# output:-
# outer x
# outer x
# outer x
# Global x