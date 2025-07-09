# 🔁 Python Loops: `for`, `while`, `break`, `continue`, `range()`

Welcome to the **Loops in Python** guide! In this section of your Python repository, you'll learn how to control the flow of your program using loops.

---

## 🔂 For Loop

A **for loop** is used to iterate over a sequence (like a list, tuple, string, or dictionary).

### 🔹 Syntax:

```python
for variable in sequence:
    # code block
```

### ✅ Example:

```python
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
```

📤 Output:

```
1
2
3
4
5
```

---

## 🔓 break Statement

The `break` statement is used to exit a loop early — as soon as a specific condition is met.

### 🔹 Syntax:

```python
for item in sequence:
    if condition:
        break
```

### ✅ Example:

```python
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found!', num)
        break
    print(num)
```

📤 Output:

```
1
2
Found! 3
```

---

## 🔁 continue Statement

The `continue` statement skips the current iteration and moves to the next one.

### ✅ Example:

```python
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found!', num)
        continue
    print(num)
```

📤 Output:

```
1
2
Found! 3
4
5
```

---

## 🔁 Nested Loops

You can run a loop inside another loop.

### ✅ Example:

```python
nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in 'abc':
        print(num, letter)
```

📤 Output:

```
1 a
1 b
1 c
2 a
...
5 c
```

🧠 **How it works:**

* Outer loop runs for each number in `nums`
* Inner loop runs for each letter in `'abc'`
* Each pair is printed

---

## 🔢 range() Function

The `range()` function generates a sequence of numbers, commonly used in `for` loops.

### 🔹 Syntax:

* `range(stop)`
* `range(start, stop)`
* `range(start, stop, step)`

### ✅ Examples:

```python
for i in range(10):
    print(i)
```

📤 Output:

```
0 to 9
```

```python
for i in range(1, 11):
    print(i)
```

📤 Output:

```
1 to 10
```

---

## 🔄 while Loop

The `while` loop runs as long as a condition is `True`.

### 🔹 Syntax:

```python
while condition:
    # code block
```

### ✅ Example 1:

```python
x = 0
while x < 10:
    print(x)
    x += 1
```

📤 Output:

```
0 to 9
```

### ✅ Example 2 (with break):

```python
x = 0
while x < 10:
    if x == 5:
        print("x =", x)
        break
    print(x)
    x += 1
```

📤 Output:

```
0 to 4 then x = 5
```

### ✅ Example 3 (infinite with break):

```python
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1
```

📤 Output:

```
0 to 4
```

### ⚠️ Example 4: Infinite Loop

```python
# ⚠️ Don't run this unless needed. Use Ctrl+C to stop.
while True:
    print(x)
    x += 1
```

---

### 🧠 Tip:

Use `break` and `continue` wisely to control the flow of loops and avoid infinite loops!

---

👨‍💻 Happy Looping! You're mastering the core concepts of Python.
Want to add flowcharts or diagrams next? Just let me know! 😄
