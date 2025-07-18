# 📘 Python Dictionary Notes

A **dictionary** in Python is a collection of **key-value pairs**. It's:

- 🔓 **Mutable** (you can change it),
- 📍 **Indexed by keys** (not positions),
- 🔄 **Unordered** (before Python 3.7),
- 🚫 Keys must be **unique and immutable** (like strings, numbers, or tuples).

---

## 🧪 Example of a Dictionary:

```python
student = {
    1: 1,
    "name": "Rahul",
    "age": 25,
    "courses": ['Math', "CompSci"]
}

print(student)  
# Output: {1: 1, 'name': 'Rahul', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['courses'])  
# Output: ['Math', 'CompSci']
```
---

## 🛠 Dictionary Methods

### **1. get()**
Safely access values without error if key doesn’t exist.
```python
print(student.get('age'))  # 25
print(student.get('phone'))  # None
print(student.get('skills', 'There are no skills'))  # There are no skills
```

### **2. Adding a New Element**
```python
student['phone'] = '555-555'
print(student['phone'])  # Added phone: 555-555
print(student)
# Output: {1: 1, 'name': 'Rahul', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-555'}
```

### **3. update()**
Add or update multiple key-value pairs.
```python
student.update({'name': 'Jane', 'age': 21, 'tutorail': 'python'})
print(student)
# Output: {1: 1, 'name': 'Jane', 'age': 21, 'courses': ['Math', 'CompSci'], 'tutorail': 'python'}
```

### **4. del **
Delete a key-value pair or entire dictionary.
```python
del student['age']
print(student)
# Output: {1: 1, 'name': 'Rahul', 'courses': ['Math', 'CompSci']}

# Deleting entire dictionary:
del(student)
# print(student) → This will raise an error
```

### **5. pop() **
Remove and return value of a key.
```python
age = student.pop('age')
print(age)  # 25
print(student)
# Output: {1: 1, 'name': 'Rahul', 'courses': ['Math', 'CompSci']}
```

### **6. len() **
Returns the number of items (key-value pairs).
```python
print(len(student))  # 4
```


### **7. keys()**
Returns all the keys.
```python
print(student.keys())
# Output: dict_keys([1, 'name', 'age', 'courses'])
```

### **8. values() **
Returns all the values.
```python
print(student.values())
# Output: dict_values([1, 'Rahul', 25, ['Math', 'CompSci']])
```

### **9. items()**
Returns all key-value pairs as tuples.
```python
print(student.items())
# Output: dict_items([(1, 1), ('name', 'Rahul'), ('age', 25), ('courses', ['Math', 'CompSci'])])
```

---

## 🔁 Looping Through a Dictionary

### Example 1: Keys Only
```python
for key in student:
    print(key)
# Output:
# 1
# name
# age
# courses
```

### Example 2: Keys and Values
```python
for key, value in student.items():
    print(key, value)
# Output:
# 1 1
# name Rahul
# age 25
# courses ['Math', 'CompSci']
```

## Summary
| Feature     | Description                                  |
| ----------- | -------------------------------------------- |
| Mutable     | ✅ Yes                                        |
| Ordered     | ⚠️ Only in Python 3.7+                       |
| Key Types   | Strings, numbers, tuples (must be immutable) |
| Value Types | Any (can be list, string, int, etc.)         |


---

## ✍️ Created By

**Rahul Anil Shirke**  
[GitHub](https://github.com/Rahulshirke1) • [LinkedIn](https://www.linkedin.com/in/rahul-shirke/)  
🎓 B.E. in Information Technology | Passionate about Python, Web Dev & AI 🚀