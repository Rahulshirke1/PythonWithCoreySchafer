# 📘 Python: Lists, Tuples & Sets

Welcome to the **Python Notes Repository**! This document contains beginner-friendly explanations and examples of three core Python data structures:

* Lists
* Tuples
* Sets

---

## 📚 What is a List in Python?

A **list** is a collection of items stored in a single variable.

### ✅ Features:

* **Ordered**: You can access items by index.
* **Mutable**: You can change the values.
* **Flexible**: Can store different data types.

---

### 🔢 Accessing Elements:

```python
course = ['History', 'Math', 'Physics', 'CompSci']
print(course)
print(len(course))
print(course[0])       # Indexing
print(course[-1])      # Negative indexing
```

### 📏 Slicing:

```python
course = ['History', 'Math', 'Physics', 'CompSci']
print(course[0:2])     # ['History', 'Math']
print(course[:2])      # ['History', 'Math']
print(course[2:])      # ['Physics', 'CompSci']
```

---

## 🔧 List Methods

### 1. `append()`
The append() method adds a single item to the end of a list.
```python
course = ['History', 'Math', 'Physics', 'CompSci']
course.append("Art")
print(course)  # Adds 'Art' to the end
```

### 2. `insert()`
The insert() method adds an item at a specified index in a list.
```python
course = ['History', 'Math', 'Physics', 'CompSci']
course.insert(0, 'Art')
print(course) # ['Art', 'History', 'Math', 'Physics', 'CompSci']

# Nested list example
courses = ['History', 'Math', 'Physics', 'CompSci']
course_2 = ['Art', "GK"]
courses.insert(0, course_2)
print(courses)  # [['Art', 'GK'], 'History', 'Math', 'Physics', 'CompSci']
```

### 3. `extend()`
The extend() method is used to add multiple elements from an iterable (like another list, tuple, string) to the end of the current list.
```python
courses = ['History', 'Math', 'Physics', 'CompSci']
course_2 = ['Art', "GK"]
courses.extend(course_2)
print(courses)# ['History', 'Math', 'Physics', 'CompSci', 'Art', 'GK']
```

### 4. `remove()`
remove():-The remove() method removes the first occurrence of a specific value from a list.
```python
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('Math')
print(courses) # ['History', 'Physics', 'CompSci']
```

### 5. `pop()`
The pop() method removes and returns the item at a given index (default is the last item).
#by default it removes last element
```python
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.pop()      # Removes last
courses.pop(0)     # Removes first
print(courses)  # ['Math', 'Physics']
```

### 6. `reverse()`
The reverse() method reverses the elements of a list in place — meaning it modifies the original list directly.
```python
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()
print(courses) # ['CompSci', 'Physics', 'Math', 'History']
```

### 7. `sort()`
The sort() method sorts a list in place — meaning it modifies the original list directly instead of returning a new one.
```python
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort()
print(courses) # ['CompSci', 'History', 'Math', 'Physics']

nums = [1, 5, 8, 3, 4, 6, 7, 2]
nums.sort(reverse=True)
print(nums)  # [8, 7, 6, 5, 4, 3, 2, 1]
```

### 8. `sorted()`
The sorted() function returns a new sorted list from the elements of any iterable (like a list, tuple, string, etc.), without changing the original.
```python
courses = ['History', 'Math', 'Physics', 'CompSci']
sorted_courses = sorted(courses)
print(sorted_courses)  # ['CompSci', 'History', 'Math', 'Physics']
print(courses)  # Original remains unchanged # ['History', 'Math', 'Physics', 'CompSci']
```

### 9. `min()` / `max()` / `sum()`
🪄The min() function returns the minimum (smallest) value from an iterable or from multiple arguments.
🪄The max() function returns the maximum (largest) element from an iterable or among multiple values.
🪄The sum() function returns the total (sum) of all the elements in an iterable (like a list or tuple) containing numbers.
```python
nums = [1, 5, 8, 3, 4, 6, 7, 2]
print(min(nums))  # 1
print(max(nums))  # 8
print(sum(nums))  # 36
```

### 10. `index()`
The index() method returns the index (position) of the first occurrence of a specified value in a list.
```python
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses.index('Physics')) # 2
```

### 11. `in` keyword
using in to check the value exists inside the list or not.
```python
courses = ['History', 'Math', 'Physics', 'CompSci']
print('Art' in courses)   # False
print('Math' in courses)  # True
```

### 12. Looping

```python
courses = ['History', 'Math', 'Physics', 'CompSci']
for item in courses:
    print(item)
# History
# Math
# Physics
# CompSci
```

### 13. `enumerate()`
The enumerate() function adds a counter (index) to an iterable like a list, tuple, or string — allowing you to loop with both index and value.
```python
courses = ['History', 'Math', 'Physics', 'CompSci']
for index, item in enumerate(courses):
    print(index, item)
# 0 History
# 1 Math
# 2 Physics
# 3 CompSci
# With custom start
for index, item in enumerate(courses, start=1):
    print(index, item)
# 1 History
# 2 Math
# 3 Physics
# 4 CompSci
```

### 14. `join()` and `split()`
🪄The join() method is used to combine elements of a list into a single string, with a specified separator between each item.
 '🪄note:- The join() method is used to combine elements of a list into a single string, with a specified separator between each item.
 🪄The split() method breaks a string into a list of substrings, based on a separator.
```python
courses = ['History', 'Math', 'Physics', 'CompSci']
course_str = '-'.join(courses)
print(course_str)  # History-Math-Physics-CompSci

location = '/India/Maharashtra/Mumbai/Dahisar/Kandarpada'
new_list = location.split('/')
print(new_list) # ['', 'India', 'Maharashtra', 'Mumbai', 'Dahisar', 'Kandarpada']
```

---

## 🧊 Tuples in Python

A **tuple** is like a list, but **immutable**.

### ✅ Features:

* Ordered
* Immutable
* Allows duplicates
* Can contain any type

### Examples:

```python
courses = ('History', 'Math', 'Physics', 'CompSci')
for item in courses:
    print(item)
# History
# Math
# Physics
# CompSci

for index, item in enumerate(courses, start=1):
    print(index, item)
# 1 History
# 2 Math
# 3 Physics
# 4 CompSci
# Immutable Example
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_1[0] = 'Art'  # ❌ Error: tuples are immutable
```

---

## 🟣 Sets in Python

A **set** is a collection of **unordered, unindexed**, and **unique** items.

### ✅ Features:

* No duplicates
* Unordered
* Mutable

### Examples:

```python
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Art', 'Design'}
print(type(cs_courses))  # <class 'set'>
print(cs_courses)  # {'Math', 'Physics', 'CompSci', 'History'}
```

### `intersection()`
The intersection() method returns a new set containing only the elements common to both (or all) sets.
```python
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))  # {'History'}
```

### `difference()`
The difference() method returns a new set that contains elements that are in the first set but not in the second.
```python
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Art', 'Design'}
print(cs_courses.difference(art_courses))    # {'Math', 'CompSci', 'Physics'}
```

### `union()`
The union() method returns a new set that contains all unique elements from the sets involved.
```python
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Art', 'Design'}
print(cs_courses.union(art_courses))  # {'Physics', 'Design', 'Math', 'Art', 'History', 'CompSci'}
```

---

### 👨‍💻 Happy Learning!

Keep practicing and experimenting to get comfortable with Python data structures.

Contributions and pull requests are welcome. ⭐ this repo if you found it helpful!
