# 📘 Python Basics – Numbers, Operators, Type Casting, and Random

### This section covers Python fundamentals related to **numbers**, **arithmetic operations**, **comparisons**, **number methods**, **type casting**, and the **random module**.

---

## 🔢 Numbers in Python

### Checking the type of a number:
```python
num = 3
print(type(num))  # <class 'int'>
```

---


## Arithmetic Operators
| Operation      | Syntax | Example  | Result |
| -------------- | ------ | -------- | ------ |
| Addition       | `+`    | `3 + 2`  | `5`    |
| Subtraction    | `-`    | `3 - 2`  | `1`    |
| Multiplication | `*`    | `3 * 2`  | `6`    |
| Division       | `/`    | `3 / 2`  | `1.5`  |
| Floor Division | `//`   | `3 // 2` | `1`    |
| Exponentiation | `**`   | `3 ** 2` | `9`    |
| Modulus        | `%`    | `3 % 2`  | `1`    |

```python
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 ** 2)
print(3 % 2)
```

## 🧮 Arithmetic Expression Evaluation
```python
print(3 * (2 + 1))  # Output: 9
```

---


## 🔁 Variable Reassignment and Incrementing
Example 1:
```python
num = 1
num = num + 1
print(num)  # Output: 2
```

Example 2:
```python
num = 1
num *= 5
num /= 5
num %= 5
num -= 5
num += 5
print(num)  # Output: (practise each and check the output)
```

---

## ⚖️ Comparison Operators
| Operation           | Syntax | Example  | Result  |
| ------------------- | ------ | -------- | ------- |
| Equal to            | `==`   | `3 == 2` | `False` |
| Not equal to        | `!=`   | `3 != 2` | `True`  |
| Greater than        | `>`    | `3 > 2`  | `True`  |
| Less than           | `<`    | `3 < 2`  | `False` |
| Greater or equal to | `>=`   | `3 >= 2` | `True`  |
| Less or equal to    | `<=`   | `3 <= 2` | `False` |


---

## 🧰 Number Methods

### 1. abs() – Absolute Value
The abs() function in Python returns the absolute value of a number. That means it returns the number without its sign.
```python
print(abs(-3))         # 3
print(abs(3 + 4j))     # 5.0 (magnitude of complex number)
```

### 2. round() – Rounding Numbers
The round() function in Python is used to round a number to the nearest integer or to a given number of decimal places.
```python
print(round(3.75))      # 4
print(round(3.75, 1))   # 3.8
```

### 3. sum() – Sum of an Iterable
The sum() function in Python is used to calculate the total (sum) of all elements in an iterable (like a list, tuple, etc.).
```python
print(sum([1, 2, 3, 4]))  # 10
```

### 4. max() and min() – Maximum and Minimum
the max() and min() functions are used to find the largest and smallest values from a set of values or an iterable (like a list, tuple, etc.).
```python
print(max(5, 10, 2))  # 10
print(min(5, 10, 2))  # 2
```

---


## 🔄 Type Casting
Type casting means converting one data type to another. Python allows explicit and implicit type casting.
```python
num_1 = '100'
num_2 = '200'
print(num_1 + num_2)  # '100200' (string concatenation)

# Convert to integers
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)  # 300
```

---

## 🎲 Random Module
#### Python's random module provides ways to generate random numbers and perform random operations.

Importing:
```python
import random
```

---

### 1. random.random() – Returns float between 0.0 and 1.0
```python
print(random.random())         # e.g. 0.834
print(random.random() * 10)    # e.g. 6.12
print(round(random.random()))  # 0 or 1
print(round(random.random() * 10))  # Random number 0–10
```

### 2. random.randint(a, b) – Random integer between a and b (inclusive)
The randint() function is used to generate a random integer between two given numbers inclusive (i.e., both the start and end values are included).
```python
print(random.randint(1, 6))  # Simulates a dice roll (1 to 6)
```

---

# ✅ Summary
### This section introduces:
### Basic arithmetic and comparison operations
### Common number methods like abs(), round(), sum()
### Type casting from strings to numbers
### Generating random numbers using the random module

---

## ✍️ Created By

**Rahul Anil Shirke**  
[GitHub](https://github.com/Rahulshirke1) • [LinkedIn](https://www.linkedin.com/in/rahul-shirke/)  
🎓 B.E. in Information Technology | Passionate about Python, Web Dev & AI 🚀
