# 🐍 Python Notes: Conditionals, Comparisons & Booleans

---

## 🔹 Comparisons in Python:

| Operator         | Meaning             |
|------------------|----------------------|
| `==`             | Equal                |
| `!=`             | Not Equal            |
| `>`              | Greater Than         |
| `<`              | Less Than            |
| `>=`             | Greater or Equal     |
| `<=`             | Less or Equal        |
| `is`             | Object identity      |

---

## 🔸 `if` Statement
The `if` statement is used to make decisions in your code — it allows you to execute a block of code only if a certain condition is true.

### ✅ Basic Syntax:
```python
if condition:
    # code to run if condition is true
```

### 🔸 Examples:
```python
if True:
    print('Conditional was True')  # Output: Conditional was True

if False:
    print('Conditional was True')  # No Output
```

### Example 1:
```python
language = 'Python'
if language == 'Python':
    print('Conditional was True')  # Output: Conditional was True
```

---

## 🔸 `else` Statement
The `else` block runs when the `if` condition is false.

### ✅ Basic Syntax:
```python
if condition:
    # runs if condition is true
else:
    # runs if condition is false
```

### Example 1:
```python
language = 'Python'
if language == 'Python':
    print('Language is Python')
else:
    print('No Match')
# Output: Language is Python
```

### Example 2:
```python
language = 'Java'
if language == 'Python':
    print('Language is Python')
else:
    print('No Match')
# Output: No Match
```

---

## 🔸 `elif` Statement
Used to check multiple conditions.

### ✅ Basic Syntax:
```python
if condition1:
    # runs if condition1 is true
elif condition2:
    # runs if condition2 is true
else:
    # runs if none are true
```

### Example 1:
```python
language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')
# Output: Language is Java
```

### Example 2:
```python
language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Match')
# Output: Language is Java
```

---

## 🔸 `is` vs `==`

### Example:
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (same values)
print(a is b)  # False (different memory addresses)
```

---

## 🔸 `id()` Function
Returns the memory address of an object.

### Example 1:
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))  # memory address like 2280337150144
print(id(b))  # different memory address like 2280338587264
```

### Example 2:
```python
a = [1, 2, 3]
b = a
print(id(a))  # same as id(b)
print(id(b))
print(a is b)  # True
print(id(a) == id(b))  # True
```

---

## 🔸 False Values in Python
- `False`
- `None`
- `0`
- Empty string: `''`
- Empty list: `[]`
- Empty tuple: `()`
- Empty dict: `{}`

### Example 1:
```python
condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# Output: Evaluated to False
```

### Example 2:
```python
condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# Output: Evaluated to False
```

### Example 3:
```python
condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# Output: Evaluated to False
```

### Example 4:
```python
condition = -1 or 1
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# Output: Evaluated to True
```

### Example 5:
```python
condition = () or '' or {} or []
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# Output: Evaluated to False
```

### Example 6:
```python
condition = ("Rahul", "anil") or 'riya' or {"age":20, "color":"red"} or [88,238, "string", ["jj"]]
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# Output: Evaluated to True
```

---

## 🔸 Boolean Operators

### 1. `and` Operator:
Returns True only if **both** conditions are True.

### Example 1:
```python
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
# Output: Admin Page
```

### Example 2:
```python
user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
# Output: Bad Creds
```

### 2. `or` Operator:
Returns True if **any one** condition is True.

### Example:
```python
user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
# Output: Admin Page
```

### 3. `not` Operator:
Reverses the Boolean value.
- `not True` becomes `False`
- `not False` becomes `True`

### Example:
```python
user = 'Admin'
logged_in = False

if not logged_in:
    print("Please Log in")
else:
    print('Welcome')
# Output: Please Log in
```

---

## 🎉 **End of Notes**

#### ✅ Keep practicing these concepts and apply them in small Python scripts to master control flow!

---

## ✍️ Created By

**Rahul Anil Shirke**  
[GitHub](https://github.com/Rahulshirke1) • [LinkedIn](https://www.linkedin.com/in/rahul-shirke/)  
🎓 B.E. in Information Technology | Passionate about Python, Web Dev & AI 🚀