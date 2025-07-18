# Tuples
# A tuple is an ordered, immutable collection of items.
# ✅ Key properties:
# Ordered ✅
# Immutable ❌ (you can’t change the values after creation)
# Allows duplicates ✅
# Can contain different data types ✅

# example1:
# courses = ('History', 'Math', 'Physics', 'CompSci')
# for item in courses:
#     print(item)

# example2:
# courses = ('History', 'Math', 'Physics', 'CompSci')
# for item in enumerate(courses, start=1):
#     print(item)
# output:
#     (1, 'Math')
#     (2, 'CompSci')
#     (3, 'Physics')
#     (4, 'History')

# example3(immutable example):
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'
# print(tuple_1)
# print(tuple_2) # As tuple are immutable it doesn't support changes.
# This will give an error.

