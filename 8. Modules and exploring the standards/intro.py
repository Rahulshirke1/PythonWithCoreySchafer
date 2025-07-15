# method 1:
# import my_module
# courses = ['History', 'Math', 'Pyhsiscs', 'CompSci']

# index = my_module.find_index(courses, 'Math')
# print(index)
# output :
# Imported my_module...
# 1

# Method 2 : 
# import my_module as mm
# courses = ['History', 'Math', 'Pyhsiscs', 'CompSci']

# index = mm.find_index(courses, 'Math')
# print(index)
# output :
# Imported my_module...
# 1

# Method 3 : 
# example 1:
# from my_module import find_index
# courses = ['History', 'Math', 'Pyhsiscs', 'CompSci']

# index = find_index(courses, 'Math')
# print(index)
# output :
# Imported my_module...
# 1

# example 2:
# from my_module import find_index, test
# courses = ['History', 'Math', 'Pyhsiscs', 'CompSci']

# index = find_index(courses, 'Math')
# print(index)
# print(test)
# output :
# Imported my_module...
# 1
# Test String

# example 3:
# from my_module import find_index as fi, test
# courses = ['History', 'Math', 'Pyhsiscs', 'CompSci']

# index = fi(courses, 'Math')
# print(index)
# print(test)
# output:
# Imported my_module...
# 1
# Test String


# using * to import all the methods withing that module.
# example 1:
# from my_module import *
# courses = ['History', 'Math', 'Pyhsiscs', 'CompSci']

# index = find_index(courses, 'Math')
# print(index)
# print(test)
# output:
# Imported my_module...
# 1
# Test String


# sys : sys is a standard library module that provides access to some variables and functions that interact directly with the Python interpreter.
# example 1:
# from my_module import find_index, test
# import sys 
# courses = ['History', 'Math', 'Pyhsiscs', 'CompSci']

# index = find_index(courses, 'Math')
# sys.path : A list of directories Python searches for modules (affects import).
# print(sys.path)


# example 2: Here we are using sys.append to import module.
# import sys
# import os

# # Add "your module is here" to the Python path
# sys.path.append(os.path.join(os.getcwd(), 'your module is here'))

# # Import the module (exact filename, without .py)
# import here_It_Is
# print("CWD:", os.getcwd())
# print("PATH ADDED:", os.path.join(os.getcwd(), 'your module is here'))
# print("sys.path:", sys.path)


# # Use a function from that module
# here_It_Is.say_hello()


# ✅ Step-by-Step: Set PYTHONPATH Permanently on Windows

# 🪟 1. Open Environment Variables Window
# Press Windows + S (Search)

# Type: “Environment Variables”

# Click: “Edit the system environment variables”

# ⚙️ 2. In the System Properties Window
# Click the “Environment Variables...” button at the bottom.

# ➕ 3. Create a New Environment Variable
# Under User variables (or System variables, if you want all users to have access):

# Click “New...”

# Fill in the fields as follows:

# Field     	   Value
# Variable name	   PYTHONPATH
# Variable value   C:\2022-2023\All the python program\Corey Schafer\learning\8. Modules and exploring the standards\your module is here

# 💾 4. Save & Restart
# Click OK on all windows to save

# Restart VS Code, Command Prompt, or any terminal where you want to run Python

# 5. Go to cmd
# >> python
# >> import my_module
# >> sys.path

# example:
# import sys
# import os

# Add the folder, not the file
# sys.path.append(r'C:\2022-2023\All the python program\Corey Schafer\learning\8. Modules and exploring the standards')

# Now import from the module
# from my_module import find_index, test

# Use the imported function
# courses = ['History', 'Math', 'Pysics', 'CompSci']
# index = find_index(courses, 'Math')

# print("Index of 'Math':", index)
# print("Test variable from module:", test)



# import random
# import random
# courses = ['History', 'Math', 'Pysics', 'CompSci']
# random_course = random.choice(courses)
# print(random_course) # gives random items of list itmes.

# import math
# import math
# rads = math.radians(90)
# print(math.sin(rads)) # output : 1.0

#import datetime and calendar
# The datetime module is used for working with dates and times.
# 🔹 Common Classes:
# datetime.date — only the date (YYYY-MM-DD)
# datetime.time — only time (HH:MM:SS)
# datetime.datetime — date + time
# datetime.timedelta — duration (difference between dates or times)

# The calendar module lets you output calendars and check day/month info.
# 🧠 Summary Table
# Module	Function	Use
# datetime.now()	Current date & time	
# date.today()	Just the current date	
# timedelta(days=5)	Date math (add/subtract days)	
# calendar.month(y, m)	Print calendar of a month	
# calendar.isleap(y)	Check leap year	
# calendar.weekday(y, m, d)	Day of the week (0=Monday)

# import datetime
# import calendar
# 
# today = datetime.date.today() # output: 2025-07-16
# print(today)
# 
# print(calendar.isleap(2017)) # False
# print(calendar.isleap(2020)) # True

# import os
# ->The os module in Python provides a way to interact with the operating system — like working with files, directories, environment variables, and running shell commands.
# import os
# print(os.getcwd()) # output: c:\2022-2023\All the python program\Corey Schafer
# print(os.__file__)
# output:
# C:\Program Files\WindowsApps\PythonSoftwareFoundation.
# Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\os.py

# import antigravity
# -> opens your default web browser and loads this URL: https://xkcd.com/353/
# -> It's a famous XKCD comic poking fun at how easy Python makes things feel — as if you're defying gravity.

import antigravity