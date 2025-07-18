# ------------------------ List-----------------------

# 1. append()
# course = ['History', 'Math', 'Physics', 'CompSci']
# course.append("Art")
# print(course)  # Adds 'Art' to the end
# ['History', 'Math', 'Physics', 'CompSci', 'Art']


# 2. insert()
# course = ['History', 'Math', 'Physics', 'CompSci']
# course.insert(0, 'Art')
# print(course) # ['Art', 'History', 'Math', 'Physics', 'CompSci']

# Nested list example
# courses = ['History', 'Math', 'Physics', 'CompSci']
# course_2 = ['Art', "GK"]
# courses.insert(0, course_2)
# print(courses)  # [['Art', 'GK'], 'History', 'Math', 'Physics', 'CompSci']


# 3. extend()
# courses = ['History', 'Math', 'Physics', 'CompSci']
# course_2 = ['Art', "GK"]
# courses.extend(course_2)
# print(courses) # ['History', 'Math', 'Physics', 'CompSci', 'Art', 'GK']


# 4. remove()
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.remove('Math')
# print(courses) # ['History', 'Physics', 'CompSci']

# 5. pop()
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.pop()      # Removes last
# courses.pop(0)     # Removes first
# print(courses) # ['Math', 'Physics']

# 6. reverse()
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.reverse()
# print(courses) # ['CompSci', 'Physics', 'Math', 'History']


# 7. sort()
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.sort()
# print(courses) # ['CompSci', 'History', 'Math', 'Physics']

# nums = [1, 5, 8, 3, 4, 6, 7, 2]
# nums.sort(reverse=True)
# print(nums) # [8, 7, 6, 5, 4, 3, 2, 1]


# 8. sorted()
# courses = ['History', 'Math', 'Physics', 'CompSci']
# sorted_courses = sorted(courses)
# print(sorted_courses) # ['CompSci', 'History', 'Math', 'Physics']
# print(courses)  # Original remains unchanged # ['History', 'Math', 'Physics', 'CompSci']

# 9. min() / max() / sum()
# nums = [1, 5, 8, 3, 4, 6, 7, 2]
# print(min(nums))  # 1
# print(max(nums))  # 8
# print(sum(nums))  # 36

# 10. index()
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses.index('Physics')) # 2

# 11. in keyword
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print('Art' in courses)   # False
# print('Math' in courses)  # True

# 12. Looping
# courses = ['History', 'Math', 'Physics', 'CompSci']
# for item in courses:
#     print(item)
# History
# Math
# Physics
# CompSci

# 13. enumerate()
# courses = ['History', 'Math', 'Physics', 'CompSci']
# for index, item in enumerate(courses):
#     print(index, item)
# History
# Math
# Physics
# CompSci
# With custom start
# for index, item in enumerate(courses, start=1):
#     print(index, item)
# 0 History
# 1 Math
# 2 Physics
# 3 CompSci
# 1 History
# 2 Math
# 3 Physics
# 4 CompSci

# 14. join() and split()
# courses = ['History', 'Math', 'Physics', 'CompSci']
# course_str = '-'.join(courses)
# print(course_str) # History-Math-Physics-CompSci

# location = '/India/Maharashtra/Mumbai/Dahisar/Kandarpada'
# new_list = location.split('/')
# print(new_list) # ['', 'India', 'Maharashtra', 'Mumbai', 'Dahisar', 'Kandarpada']


# ------------------------ Tuples-----------------------
# courses = ('History', 'Math', 'Physics', 'CompSci')
# for item in courses:
#     print(item)
# History
# Math
# Physics
# CompSci

# for index, item in enumerate(courses, start=1):
#     print(index, item)
# 1 History
# 2 Math
# 3 Physics
# 4 CompSci

# Immutable Example
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_1[0] = 'Art'  # ❌ Error: tuples are immutable


# ------------------------ set-----------------------
# Examples:
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Art', 'Design'}
# print(type(cs_courses)) # <class 'set'>
# print(cs_courses) # {'Math', 'Physics', 'CompSci', 'History'}

# 1. intersection()
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Art', 'Design'}
# print(cs_courses.intersection(art_courses))  # {'History'}

# difference()
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Art', 'Design'} 
# print(cs_courses.difference(art_courses))    # {'Math', 'CompSci', 'Physics'}

# union()
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Art', 'Design'}
# print(cs_courses.union(art_courses))  # {'Physics', 'Design', 'Math', 'Art', 'History', 'CompSci'}
