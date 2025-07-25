# 🐍 Lambda and Comprehension in Python

Welcome to your Python learning notes on **lambda**, **comprehensions**, and **generator expressions**. This covers essential concepts with examples and clear explanations to boost your Python fundamentals.

---

## 🔹 Lambda in Python

### 🔍 What is `lambda`?

A **lambda** is a small anonymous function in Python.
It is useful when you need a short, quick function without using `def`.

### ✅ Syntax:

```python
lambda arguments: expression
```

* `lambda` – the keyword
* `arguments` – inputs to the function
* `expression` – the single expression to return (no statements or multiple lines)

---

### 🔸 Examples

**Example 1: Square a number**

```python
square = lambda n: n * n
print(square(5))  # Output: 25
```

Equivalent using `def`:

```python
def square(n):
    return n * n
```

**Example 2: Add two numbers**

```python
add = lambda a, b: a + b
print(add(3, 4))  # Output: 7
```

---

### 🔄 Where is lambda useful?

Lambda functions are commonly used with higher-order functions like:

* `map()`
* `filter()`
* `sorted()`

**Example with `map()`**

```python
nums = [1, 2, 3]
square = list(map(lambda x: x * x, nums))
print(square)  # Output: [1, 4, 9]
```

---

### ⚠️ Limitations of Lambda

* Can only contain **one expression**
* No multi-line logic
* No statements like `if`, `for`, etc.

---

## 🔹 Comprehensions

Comprehensions are a concise way to create collections like lists, dictionaries, and sets.

---

### 🔸 List Comprehension

**Example 1: Copy a list**

```python
nums = [1, 2, 3, 4, 5]
my_list = [n for n in nums]
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

**Example 2: Square each number**

```python
my_list = [n*n for n in nums]
print(my_list)  # Output: [1, 4, 9, 16, 25]
```

Using `map()` and `lambda`:

```python
my_list = map(lambda n: n*n, nums)
print(list(my_list))
```

**Example 3: Filter even numbers**

```python
my_list = [n for n in nums if n % 2 == 0]
print(my_list)  # Output: [2, 4, 6, 8, 10]
```

Using `filter()` and `lambda`:

```python
my_list = list(filter(lambda n: n % 2 == 0, nums))
print(my_list)
```

---

### 🔸 Nested Loops in List Comprehension

**Example 4: Create (letter, number) pairs**

```python
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)
# Output: [('a', 0), ..., ('d', 3)]
```

---

### 🔸 Dictionary Comprehension

**Example 5: Names and Heroes**

```python
names = ['Bruce', 'Clark', 'Peter']
heros = ['Batman', 'Superman', 'Spiderman']
my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)
# Output: {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman'}
```

**With condition:**

```python
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)
# Output: {'Bruce': 'Batman', 'Clark': 'Superman'}
```

**Explanation:**

* `zip(names, heros)` pairs elements from two lists.
* `{key: value for key, value in zip(...)}`
* Stops at the shorter list.

---

### 🔸 Set Comprehension

**Example 6: Remove duplicates**

```python
nums = [1, 1, 2, 3, 4, 3, 4]
my_set = {n for n in nums}
print(my_set)
# Output: {1, 2, 3, 4}
```

---

## 🔹 Generator Expressions

Generators are like list comprehensions, but they don’t store the entire result in memory – they yield items one at a time.

---

### 🔍 `yield` vs `return`

| Feature       | `return`                  | `yield`                           |
| ------------- | ------------------------- | --------------------------------- |
| Returns value | Yes                       | Yes                               |
| Function ends | Yes                       | No, resumes later                 |
| Memory use    | High (stores all at once) | Low (generates values on the fly) |
| Use case      | Regular functions         | Generator functions               |

---

### Example: Generator Function to Square Numbers

```python
def gen_func(nums):
    for n in nums:
        yield n * n

nums = [1, 2, 3, 4, 5]
my_gen = gen_func(nums)

print(set(my_gen))  # Output: {1, 4, 9, 16, 25}
```

---

## ✅ Summary

| Concept              | Use Case                                      |
| -------------------- | --------------------------------------------- |
| `lambda`             | Small, anonymous function                     |
| `list comprehension` | Create a new list from an existing iterable   |
| `dict comprehension` | Build a dictionary from iterable data         |
| `set comprehension`  | Build a set (unique items) from iterable data |
| `yield`              | Create generators for memory-efficient loops  |

---

**📘 Tip:**
Use comprehensions and lambda when you want to write **clean**, **efficient**, and **Pythonic** code – but avoid overusing them when readability suffers.

---
