#  List
# 📚 What is a List in Python?
# A list is a collection of items (values, variables, or objects) stored in a single variable.
# Lists are ordered (you can access by index)
# Lists are mutable (you can change the values)
# Lists can contain any data type, even mixed types

# example1
# -



# Acessing the elements throught index number as you can see below. 
#          [0]        [1]     [2]        [3]
# course = ['History', 'Math', 'Physics', 'CompSci']
# print(course)
# print(len(course))
# # map the location of elements through index value.
# print(course[0])
# # This is negative indexing
# print(course[-1])

# list Slicing
# course = ['History', 'Math', 'Physics', 'CompSci']
# list[start: stop -1]
# example 1:
# print(course[0:2]) #0 is starting 
#example 2:
# print(course[:2])
# print(course[2:])

# ---------------------Methods------------------

# 1. append() :- The append() method adds a single item to the end of a list.
# course = ['History', 'Math', 'Physics', 'CompSci']
# course.append("Art")
# print(course) #['History', 'Math', 'Physics', 'CompSci', 'Art']

# 2. insert() :- The insert() method adds an item at a specified index in a list.
# example1:
# course = ['History', 'Math', 'Physics', 'CompSci']
# course.insert(0, 'Art') ['Art', 'History', 'Math', 'Physics', 'CompSci']
# print(course)

# example2:
# courses = ['History', 'Math', 'Physics', 'CompSci']
# course_2 = ['Art', "GK"]

# courses.insert(0, course_2)
# print(courses) # [['Art', 'GK'], 'History', 'Math', 'Physics', 'CompSci']


# 3. extend() :- The extend() method is used to add multiple elements from an iterable (like another list, tuple, string) to the end of the current list.
# courses = ['History', 'Math', 'Physics', 'CompSci']
# course_2 = ['Art', "GK"]

# courses.extend(course_2)
# print(courses) ['Art', "GK", 'History', 'Math', 'Physics', 'CompSci']

# 4. remove():-The remove() method removes the first occurrence of a specific value from a list.
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.remove('Math')
# print(courses) # ['History', 'Physics', 'CompSci']

# 5. pop():-The pop() method removes and returns the item at a given index (default is the last item).
#by default it removes last element
#example1 :
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.pop()
# print(courses) #['History', 'Math', 'Physics']

# example2 :
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.pop(0) 
# print(courses)

# 6. reverse():-The reverse() method reverses the elements of a list in place — meaning it modifies the original list directly.
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses.reverse() 
# print(courses) # ['CompSci', 'Physics', 'Math', 'History']

# 7. sort():-The sort() method sorts a list in place — meaning it modifies the original list directly instead of returning a new one.
# example 1:
# courses = ['History', 'Math', 'Physiscs', 'CompSci']
# courses.sort() 
# print(courses) # ['CompSci', 'History', 'Math', 'Physics']

#example 2:
# nums = [1, 5, 8, 3, 4, 6, 7, 2]
# nums.sort()
# print(nums) # [1, 2, 3, 4, 5, 6, 7, 8]

# example 3: If we want in descinding order
# nums = [1, 5, 8, 3, 4, 6, 7, 2]
# nums.sort(reverse=True)
# print(nums) # [8, 7, 6, 5, 4, 3, 2, 1]

# 8. sorted() :- The sorted() function returns a new sorted list from the elements of any iterable (like a list, tuple, string, etc.), without changing the original.
# courses = ['History', 'Math', 'Physics', 'CompSci']
# sorted_course = sorted(courses)
# print(courses) # original doesnt change. # ['History', 'Math', 'Physics', 'CompSci']
# print(sorted_course) # ['CompSci', 'History', 'Math', 'Physics']

# 9. min() :-The min() function returns the minimum (smallest) value from an iterable or from multiple arguments.
# nums = [1, 5, 8, 3, 4, 6, 7, 2]
# print(min(nums)) # 1

# 10. max() :-The max() function returns the maximum (largest) element from an iterable or among multiple values.
# nums = [1, 5, 8, 3, 4, 6, 7, 2]
# print(max(nums))# 8

# 11. sum():-The sum() function returns the total (sum) of all the elements in an iterable (like a list or tuple) containing numbers.
# nums = [1, 5, 8, 3, 4, 6, 7, 2]
# print(sum(nums)) #36

# 12. index():-The index() method returns the index (position) of the first occurrence of a specified value in a list.
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print(courses.index('Pysiscs')) # 2
# print(courses.index('Art')) # error

# 13. using in to check the value exists inside the list or not.
# courses = ['History', 'Math', 'Physics', 'CompSci']
# print('Art' in courses) # False
# print('Math' in courses) # True

# 14. using for loop to print list

# courses = ['History', 'Math', 'Physics', 'CompSci']
# for item in courses:
#     print(item)
# Output:
# History
# Math
# Pysiscs
# CompSci

# 15. enumerate() :- The enumerate() function adds a counter (index) to an iterable like a list, tuple, or string — allowing you to loop with both index and value.
# enumerate(iterable, start=0)
# iterable: The list (or any iterable) you want to loop over.
# start: (optional) index to start counting from (default is 0).

#example1:
# courses = ['History', 'Math', 'Physics', 'CompSci']

# for index, item in enumerate(courses):
#     print(index, item)
# output:
# 0 History
# 1 Math
# 2 Physics
# 3 CompSci

    
# example2:
# courses = ['History', 'Math', 'Physics', 'CompSci']

# for index, item in enumerate(courses, start=1):
#     print(index, item)
# output:
# 1 History
# 2 Math
# 3 Physics
# 4 CompSci

# 16. join() :-The join() method is used to combine elements of a list into a single string, with a specified separator between each item.
# note:- The join() method is used to combine elements of a list into a single string, with a specified separator between each item.
# courses = ['History', 'Math', 'Physics', 'CompSci']
# course_str = '-'.join(courses)
# print(course_str) # History-Math-Physics-CompSci


# 17. split() :- The split() method breaks a string into a list of substrings, based on a separator.
# example:
# location = '/India/Maharashtra/Mumbai/Dahisar/Kandarpada'
# new_list = location.split('/')
# print(new_list)