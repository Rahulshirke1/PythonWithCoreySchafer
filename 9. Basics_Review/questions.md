# 🧠 Python Interview Questions – Basics Review (Episodes 1–8)

A quick reference of beginner-friendly Python interview questions, based on the concepts learned in Episodes 1 through 8.

### **There might be some questions which are not covered in above episode like oops(class and object), error handling and so on... . I will cover them in later episodes.**

---

### 🔹 1. What is the difference between a list, tuple, and set?
**Answer:**
- **List** – Ordered, mutable, allows duplicates → `[]`
- **Tuple** – Ordered, immutable, allows duplicates → `()`
- **Set** – Unordered, mutable, no duplicates → `{}`

---

### 🔹 2. What is the difference between `is` and `==`?
**Answer:**
- `==` compares **values**
- `is` compares **memory/reference**

```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False
```

---

### 🔹 3. What are Python's built-in data types?
**Answer:**

- **Numeric:** `int`, `float`, `complex`  
- **Sequence:** `list`, `tuple`, `range`, `str`  
- **Set:** `set`, `frozenset`  
- **Mapping:** `dict`  
- **Boolean:** `bool`  
- **None:** `NoneType`

---

### 🔹 4. How do you create a function in Python?
**Answer:**
```python
def greet(name):
    return f"Hello, {name}"
```

---

### 🔹 5. What are default parameters in functions?
**Answer:**
```python
def greet(name="Guest"):
    return f"Hello, {name}"
```

---

### 🔹 6. How do you handle errors in Python?
**Answer:**
Using try-except blocks:
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

```

---

### 🔹 7. How do you import modules in Python?
**Answer:**
```python
import math
from math import sqrt
import math as m
```

---

### 🔹 8. What is a dictionary in Python?
**Answer:**
A collection of key-value pairs:
```python
student = {"name": "Rahul", "age": 20}
```

---

### 🔹 9. What does the range() function do?
**Answer:**
Generates a sequence of numbers:
```python
for i in range(3):
    print(i)  # 0, 1, 2

```

---

### 🔹 10. What is the purpose of enumerate() and zip()?
**Answer:**
enumerate() → Adds index while looping

zip() → Combines two sequences

python
Copy
Edit
```python
for i, val in enumerate(["a", "b"]):
    print(i, val)

for x, y in zip([1, 2], ["a", "b"]):
    print(x, y)
```

---

### 11. What is the difference between global and local scope?
**Answer:**
- **Local variables exist only within the function they're defined.**
- **Global variables are accessible throughout the program.**

---

### 12. What is an iterator in Python?
**Answer:**
- **An object with a countable number of values, implementing `__iter__()` and `__next__()` methods.**

---

### 13. What is the `__init__()` function?
**Answer:**
- **A special method run when a class is instantiated, used to initialize object attributes.**

---

### 14. When should you use lambda functions?
**Answer:**
- **When you need a short, anonymous function for a brief task.**

---

### 15. How can you check if all characters in a string are alphanumeric?
**Answer:**
- **Use `.isalnum()` method.**

---

### 16. How can you convert a string to an integer?
**Answer:**
- **Use `int("5")` to convert the string `"5"` to integer `5`.**

---

### 17. What is indentation in Python?
**Answer:**
- **Python uses indentation to define blocks of code. It is mandatory.**

---

### 18. How to check the type of a variable?
**Answer:**
- **Use: `print(type(x))`**

---

### 19. Which collection does not allow duplicate members?
**Answer:**
- **`set`**

---

### 20. What is inheritance in Python?
**Answer:**
- **A class (child) can inherit attributes and methods from another class (parent).**

---

### 21.  What is the output of the code below?
**Answer:**
```python
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
```
Output:
```output
Above ten,
and also above 20!
``` 
---

### 22. What are Python's built-in data types?
**Answer:**
- **Text:**str
- **Numeric:** int, float, complex
- **Sequence:** list, tuple, range
- **Mapping:** dict
- **Set:** set, frozenset
- **Boolean:** bool
- **Binary:** bytes, bytearray, memoryview


---

### 23. What are membership operators?
**Answer:**
- **Operators like in, not in used to test membership in sequences.**

---

### 24. Which statement is used when an if block is empty?
**Answer:**
- **pass**

---

### 25. What are *args in Python?
**Answer:**
- **Allows passing a variable number of non-keyword arguments into a function.**

---

### 26. How to create and use a module?
**Answer:**
```python
# mymodule.py
def greet(name):
  print("Hello", name)
```
```python
# another file
import mymodule
mymodule.greet("Jonathan")
```

---

### 27. Can you copy a list using list2 = list1?
**Answer:**
- **No. It only creates a reference. Use .copy() or list(list1) to make an actual copy.**

---

### 28. How can you return a substring?
**Answer:**
Using slice syntax:
```python
s = "Hello"
print(s[1:4])  # 'ell'
```

---

### 29. What is a class in Python?
**Answer:**
A blueprint for creating objects.
```python
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)
```

---

👨‍💻 Happy Looping! You're mastering the core concepts of Python.
Want to add flowcharts or diagrams next? Just let me know! 😄
We’re building a powerful review series here 💪
