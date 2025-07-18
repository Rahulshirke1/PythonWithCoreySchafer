# For loop :-
# A for loop is used to iterate over a sequence (like a list, tuple, string, or dictionary).
# 🔹 Syntax:
# for variable in sequence:
    # code block
    
# example :
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     print(num)
# output:
# 1
# 2
# 3
# 4
# 5

# break :-
# The break statement is used to exit a loop early — as soon as a specific condition is met.
# 🔹 Syntax:
# for item in sequence:
#     if condition:
#         break
    # code block
    
# example:
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num == 3:
#         print('Found!' , num)
#         break
#     print(num)
# output:
# 1
# 2
# Found! 3

# continue :-
# The continue statement is used to skip the current iteration of a loop and move to the next one, without breaking the loop.
# 🔹 Syntax:
# for item in sequence:
#   if condition:
#       continue
#   code block

# example:
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     if num == 3:
#         print('Found!' , num)
#         continue
#     print(num)
# output:
# 1
# 2
# Found! 3
# 4
# 5

# example on loop inside loop:
# nums = [1, 2, 3, 4, 5]
# for num in nums:
#     for letter in 'abc':
#         print(num , letter)
        
# 🧠 What’s happening:
# Outer loop runs for each number in nums

# Inner loop runs for each letter in 'abc'

# For every combination, it prints the pair
# 🖨️ Output:
# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c
# 4 a
# 4 b
# 4 c
# 5 a
# 5 b
# 5 c

# 🔢 range() Function in Python
# The range() function generates a sequence of numbers, which is commonly used in for loops.
# ✅ Syntax:
# range(stop)              # From 0 to stop-1  
# range(start, stop)       # From start to stop-1  
# range(start, stop, step) # From start to stop-1, incremented by step

# example 1:
# for i in range(10):
#     print(i)
# output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# example 2:
# for i in range(1, 11):
#     print(i)
# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# 🔁 while Loop in Python
# A while loop keeps running as long as a condition is True.
# 🔹 Syntax:
# while condition:
    # code block
# example 1:
# x = 0
# while x < 10: # condition
    # print(x)
    # x += 1 # x = x + 1
# output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# example 2:
# x = 0
# while x < 10: # condition
#     if x == 5:
#         print("x =",x)
#         break
#     print(x)
#     x += 1
# output:
# 0
# 1
# 2
# 3
# 4
# x = 5

# example 3:
# x = 0
# while True:
#     if x == 5:
#         break
#     print(x)
#     x += 1
# 0
# 1
# 2
# 3
# 4

# example 4: (It's an example of infinite loop)
# Don't run this it would rost you computer.
# If you did run it try to press ctrl + c to esc.
# while True:
#     print(x)
#     x += 1
#     print(x)
