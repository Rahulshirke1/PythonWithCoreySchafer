# Python Functions: Complete Notes with Examples

## 🧠 What is a Function?

A **function** in Python is a reusable block of code designed to perform a specific task.

### 🔹 Syntax:

```python
def function_name(parameters):
    # code block
    return result  # optional
```

---

## 📍 Example 1: Basic Function

```python
def hello_func():
    print("hello world")

hello_func()  # Output: hello world
```

---

## 🔸 `pass` Statement

The `pass` keyword is a placeholder used when a statement is syntactically required, but no code needs to run.

```python
def hello_func():
    pass

hello_func()
print(hello_func)   # <function hello_func at 0x000...> (memory address)
print(hello_func()) # None
```

---

## 🔙 `return` Statement

The `return` keyword is used to send back a result from a function.

```python
def hello_func():
    return 'Hello function.'

print(hello_func())         # Hello function.
print(hello_func().upper()) # HELLO FUNCTION.
```

---

## 🧩 Parameters vs Arguments

* **Parameter**: A variable defined in the function signature.
* **Argument**: The actual value passed to a function call.

```python
def greet(name):           # 'name' is a parameter
    print("Hello,", name)

greet("Rahul")             # 'Rahul' is an argument
```

---

## 🎯 String Formatting in Return

```python
def hello_func(greeting):
    return f"{greeting} Function"

print(hello_func("Hello")) # Hello Function
```

```python
def hello_func(greeting):
    return '{} Function'.format(greeting)

print(hello_func("Hello")) # Hello Function
```

---

## ⚙️ Default Parameter Values

You can assign default values to function parameters.

```python
def greet(name="User"):
    print("Hello,", name)

greet()           # Hello, User
greet("Rahul")    # Hello, Rahul
```

```python
def hello_func(greeting, name="you"):
    return '{}, {} Function'.format(greeting, name)

print(hello_func("Hello")) # Hello, you Function
```

```python
def hello_func(greeting, name="you"):
    return '{}, {} are you beauty'.format(greeting, name)

print(hello_func("Hi", name="Corey")) # Hi, Corey are you beauty
```

---

## 🧵 \*args and \*\*kwargs

### ✅ \*args → Arbitrary Positional Arguments

```python
def student_info(*args):
    print(args)

student_info("Math", "Art")
# Output: ('Math', 'Art')
```

### ✅ \*\*kwargs → Arbitrary Keyword Arguments

```python
def student_info(**kwargs):
    print(kwargs)

student_info(name="John", age=22)
# Output: {'name': 'John', 'age': 22}
```

### ✅ Both Together

```python
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info("Math", "Art", name="John", age=22)
# Output:
# ('Math', 'Art')
# {'name': 'John', 'age': 22}
```

```python
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
set_exam = (234, 234, 523, 1, 32, 5, 2356, 7, 32)

student_info(courses, info)
# Output:
# (['Math', 'Art'], {'name': 'John', 'age': 22})
# {}

student_info(courses, set_exam)
# Output:
# (['Math', 'Art'], (234, 234, 523, 1, 32, 5, 2356, 7, 32))
# {}
```

---

## 🧪 Big Example 1 — Days in a Month

```python
month_days = [0, 31, 28, 31, 30, 31, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    '''Return True for leap years, False for non-leap years.'''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2017))        # False
print(days_in_month(2017, 2))  # 28
```

---

## 🧪 Big Example 2 — Month Hours with DST

```python
month_hours = [0, 744, 672, 744, 720, 744, 720, 744, 744, 720, 744, 720, 744]

def is_dst(month):
    '''Return True if the month falls under Daylight Saving Time (Apr–Oct).'''
    return 4 <= month <= 10

def hours_in_month(month):
    """Return number of hours in the month, considering DST."""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if is_dst(month):
        days = month_hours[month] // 24
        return month_hours[month] + days
    return month_hours[month]

print(is_dst(5))         # True
print(hours_in_month(2)) # 672
print(hours_in_month(7)) # 775
```

---

## ✅ Summary

### Topics Covered:

* Function definition & calling
* `pass` keyword
* `return` statement
* Parameters vs Arguments
* String formatting with return
* Default parameter values
* \*args and \*\*kwargs
* Large examples: leap year, DST calculation

> ✍️ Written by: Rahul Shirke
