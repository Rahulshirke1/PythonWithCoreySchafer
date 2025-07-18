# Python: Modules and Exploring the Standard Library

## 📂 What is a Module?

A module in Python is a file containing Python definitions and statements. You can reuse code by importing it in other files.

---

## 🪡 `my_module.py` (Custom Module)

```python
# my_module.py
print('Imported my_module...')

test = 'Test String'

def find_index(tosearch, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(tosearch):
        if value == target:
            return i
    return -1
```

### 💡 Usage Examples

#### Method 1: Basic Import

```python
import my_module
courses = ['History', 'Math', 'Pyhsiscs', 'CompSci']
index = my_module.find_index(courses, 'Math')
print(index)
# Output:
# Imported my_module...
# 1
```

#### Method 2: Import with Alias

```python
import my_module as mm
index = mm.find_index(courses, 'Math')
print(index)
```

#### Method 3: Import Specific Functions

```python
from my_module import find_index, test
index = find_index(courses, 'Math')
print(index)
print(test)
```

#### Method 4: Import with Aliased Function

```python
from my_module import find_index as fi, test
index = fi(courses, 'Math')
print(index)
print(test)
```

#### Method 5: Import Everything

```python
from my_module import *
index = find_index(courses, 'Math')
print(index)
print(test)
```

---

## 📤 `sys` and `os` Modules

### 🔄 sys.path

Used to view and manipulate the list of paths Python searches for modules.

```python
import sys
print(sys.path)
```

### ➕ Adding a Custom Module Path

```python
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'your module is here'))
import here_It_Is
```

### ✅ Set PYTHONPATH Permanently (Windows)

1. Open Environment Variables
2. Add New:

   * Variable name: `PYTHONPATH`
   * Variable value: `C:\...\your module is here`
3. Restart terminal

---

## 🌐 Standard Library Modules

### 🎮 `random`

```python
import random
courses = ['History', 'Math', 'Pysics', 'CompSci']
random_course = random.choice(courses)
print(random_course)
```

### 🔢 `math`

```python
import math
rads = math.radians(90)
print(math.sin(rads))  # Output: 1.0
```

### 📅 `datetime` and `calendar`

```python
import datetime
import calendar

today = datetime.date.today()
print(today)  # e.g., 2025-07-16

print(calendar.isleap(2017))  # False
print(calendar.isleap(2020))  # True
```

### 🗃️ `os`

```python
import os
print(os.getcwd())   # Current working directory
print(os.__file__)   # Location of the os module source
```

### 🚀 `antigravity`

```python
import antigravity
# Opens https://xkcd.com/353/ in your browser
```

---

## ✅ Summary

* Created and imported a custom module (`my_module.py`)
* Used different import techniques: full, alias, selective, wildcard
* Explored standard library modules:

  * `sys`, `os`: system interaction
  * `random`: randomness
  * `math`: mathematical operations
  * `datetime`, `calendar`: date and time
  * `antigravity`: easter egg module

> ✍️ Compiled by: Rahul Shirke
