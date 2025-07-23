# 🧠 Python Variable Scope & LEGB Rule

Understanding **variable scope** is fundamental in Python programming. It determines **where** a variable is accessible and how long it lives. Python follows a hierarchy known as the **LEGB Rule** to resolve variable names.

---

## 🔍 What is Variable Scope?

In Python, **variable scope** refers to the region of your code where a variable is recognized and can be accessed or modified.

There are four types of scopes in Python:

- **Local (L):** Defined inside a function or block
- **Enclosing (E):** Inside any enclosing function (nested functions)
- **Global (G):** Defined at the top level of a script or module
- **Built-in (B):** Predefined in Python (like `len()`, `range()`)

---

## 🧭 The LEGB Rule

When Python encounters a variable name, it searches for it in the following order:

1. **Local** – Variables defined within the current function
2. **Enclosing** – Variables in the local scope of enclosing functions
3. **Global** – Variables defined at the top-level of the module
4. **Built-in** – Names preassigned in the built-in names module

---

## 💡 Code Examples

### 🔸 Example 1: Local Scope
```python
x = 'Global x'

def test():
    y = 'Local y'   # Local variable y
    print(y)        # Accessible within the function only

test()
```

### 🔸 Example 2: Accessing Global Inside Function
```python
x = 'Global x'

def test():
    y = 'Local y'
    print(x)  # Accesses global variable x

test()
```

### 🔸 Example 3: Local Variable Not Accessible Outside
```python
x = 'Global x'

def test():
    y = 'Local y'   # Local to function
    print(x)        # Accesses global x

test()
print(y)  # Error: y is not defined outside the function
```

### 🔸 Example 4: Local vs Global with Same Name
```python
x = 'Global x'

def test():
    x = 'Local x'   # Shadows the global x inside the function
    print(x)        # Prints local x

test()
print(x)            # Prints global x, unaffected by local change
```
**Output:**
```
Local x
Global x
```

### 🔸 Example 5: Using `global` Keyword
```python
x = 'Global x'

def test():
    global x        # Refers to the global x, not creating a new one
    x = 'Local x'   # Changes the global x
    print(x)        # Prints the updated global x

test()
print(x)            # Still 'Local x' because we modified the global
```
**Output:**
```
Local x
Local x
```

### 🔸 Example 6: Checking Scope Membership
```python
x = 'Global x'

def test(z):
    print(z in globals())  # False: z is not a global variable
    print(z in locals())   # True: z is local to this function

test("Local z")
```

### 🔸 Example 7: Built-in Scope
```python
print(len("hello"))  # 'len' is a built-in function in Python
```

---

## 🧪 Enclosing Scope Examples

### 🔸 Example 8: Inner Function Has Its Own Local Variable
```python
def outer():
    x = 'outer x'        # Local to outer

    def inner():
        x = 'inner x'    # Local to inner
        print(x)         # Prints inner x

    inner()
    print(x)             # Prints outer x

outer()
```
**Output:**
```
inner x
outer x
```

### 🔸 Example 9: Inner Function Accesses Enclosing Variable
```python
def outer():
    x = 'outer x'        # Enclosing variable

    def inner():
        print(x)         # Accesses enclosing variable x

    inner()
    print(x)             # Prints the same enclosing x

outer()
```
**Output:**
```
outer x
outer x
```

---

## 🔁 Example: Combined Global and Enclosing Access
```python
x = "Global x"

def outer():
    x = 'outer x'        # Local to outer function
    print(x)             # Prints outer x

    def inner():
        print(x)         # Accesses outer's x due to enclosing scope

    inner()
    print(x)             # Again prints outer x

outer()
print(x)                 # Global x remains unchanged
```
**Output:**
```
outer x
outer x
outer x
Global x
```

---

## ✅ Final Example: No Shadowing
```python
x = "Global x"

def outer():
    print(x)             # Accesses global x

    def inner():
        print(x)         # Also accesses global x

    inner()
    print(x)             # Again global x

outer()
print(x)                 # Global x
```
**Output:**
```
Global x
Global x
Global x
Global x
```

---

## 📌 Summary

- Python resolves variable names using the **LEGB rule**.
- Always check variable scope before using or modifying it.
- Use the `global` and `nonlocal` keywords cautiously to access variables outside their normal scope.

---
