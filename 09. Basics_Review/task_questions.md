# 🧪 Task Execution Questions – Python Basics

Solve the following problems using what you've learned in Episodes 1 to 8.

---

## 🔸 Task 1: Greet the User
Write a function `greet_user(name)` that returns:
> "Hello, <name>! Welcome to Python."

---

## 🔸 Task 2: Even or Odd Checker
Write a function `is_even(num)` that checks whether a number is even or odd and returns:
> "<num> is Even" or "<num> is Odd"

---

## 🔸 Task 3: List Analyzer
Write a function `analyze_list(lst)` that:
- Takes a list of numbers.
- Returns the total, maximum, and minimum.

---

## 🔸 Task 4: Word Counter
Write a function `count_words(text)` that returns the number of words in a given string.

---

## 🔸 Task 5: Reverse a String
Write a function `reverse_string(s)` that returns the reversed version of the input string.

---

## 🔸 Task 6: Number Filter
Write a function `filter_even(numbers)` that takes a list and returns only the even numbers using a loop.

---

## 🔸 Task 7: Factorial Finder
Write a function `find_factorial(n)` to calculate the factorial of a number using a loop.

---

## 🔸 Task 8: Multiplication Table Generator
Write a function `print_table(n)` that prints the multiplication table of `n` from 1 to 10.

---

## ✅ Solutions

<details>
<summary>Click to view solutions</summary>

```python
# Task 1
def greet_user(name):
    return f"Hello, {name}! Welcome to Python."

# Task 2
def is_even(num):
    return f"{num} is Even" if num % 2 == 0 else f"{num} is Odd"

# Task 3
def analyze_list(lst):
    return sum(lst), max(lst), min(lst)

# Task 4
def count_words(text):
    return len(text.split())

# Task 5
def reverse_string(s):
    return s[::-1]

# Task 6
def filter_even(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

# Task 7
def find_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Task 8
def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
