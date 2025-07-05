# 🐍 Python Basics – Strings, Methods, and Utilities

This section of the **Learning Python** repository covers the **fundamentals of string manipulation**, **methods**, and useful **built-in functions** like `dir()` and `help()`.

---

## 📌 Topics Covered
- Printing Strings
- Handling Quotes
- String Length, Indexing & Slicing
- Common String Methods
- String Concatenation & Formatting
- Utility Functions: dir() & help()
- Summary & Key Takeaways


## 1. **Printing a String**

```python
message = 'Hello World'
print(message)
```

## 2. **Handling Quotes in Strings**
❌ Incorrect:
```python
message = 'Rahul's World'  # ❌ SyntaxError
```
✅ Solution using triple quotes:
```python
message = """Rahul's World"""
print(message)
```

## 3. **📏 String Length and Indexing**
#### 🔹 Get Lengt
```python
message = 'Hello World'
print(len(message))  # Output: 11
```

#### 🔹 Accessing Characters:
```python
print(message[8])  # Output: 'r'
```

#### 🔹 ✂️ Slicing Strings
```python
message = 'hello World'
print(message[2:7])  # Output: 'llo W'
```

---
<br/>


# 🔤 String Methods

### 1. lower() & upper()
lower(): Converts all characters in a string to lowercase. upper(): Converts all characters in a string to uppercase.
```python
print('Hello WORLD'.lower())  # hello world
print('hello World'.upper())  # HELLO WORLD
```

### 2. count()
count(): Returns the number of occurrences of a specified substring in the string.
```python
print('Hello World'.count('l'))     # 3
print('Hello World'.count('Hello')) # 1
```

### 3. find()
find(): Returns the index of the first occurrence of a specified substring; returns -1 if not found.
```python
print('Hello World'.find('World'))  # 6
print('Hello World'.find('world'))  # -1
```

### 4. replace()
replace(): Returns a new string where all occurrences of a specified substring are replaced with another substring.
```python
message = 'Hello World'
print(message.replace('World', 'Universe'))  # Hello Universe
```
---
<br/>

# ➕ String Concatenation
String Concatenation: Combines two or more strings into one using the + operator or string formatting methods.
```python
greeting = 'Hello'
name = 'Michael'
print(greeting + ", " + name)  # Hello, Michael
```

## 🔹 Using .format():
```python
message = "{}, {}. Welcome".format(greeting, name)
```

## 🔹 Using f-strings:
```python
message = f'{greeting}, {name}!'
print(message)  # Hello, Michael!
```
With method chaining:
```python
print(f'{greeting.upper()}, {name}!')
```

---
<br/>

# 🧰 Utility Functions

## 1. dir()
Gives a list of available methods for an object.
```python
print(dir(str))
```
Example output:
```text
['capitalize', 'casefold', 'center', 'count', 'encode', ...]
```

## 2. help()
Displays documentation for built-in objects, classes, or functions.
```python
print(help(str))
```
---
<br>

# ✅ Summary
### This section introduces:

### String handling basics

### Method chaining with f-strings

### Built-in tools to explore Python: dir() and help()

### This is a crucial step toward mastering string manipulation, one of the most important skills in Python programming.

---

## ✍️ Created By

**Rahul Anil Shirke**  
[GitHub](https://github.com/Rahulshirke1) • [LinkedIn](https://www.linkedin.com/in/rahul-shirke/)  
🎓 B.E. in Information Technology | Passionate about Python, Web Dev & AI 🚀
