#sets
# A set is a collection of unordered, unindexed, and unique items.
# ✅ Key properties:
# No duplicates allowed ❌
# Unordered (items don't have a fixed position)
# Mutable (you can add or remove elements)
# Cannot contain unhashable types (like lists or other sets

# example1:
# cs_courses = {1, 'Math', 'CompSci','Physics', 'History'}
# print(type(cs_courses))
# print(cs_courses) # Because it is unordered as many times we run it it will give us different same value but in different order.

# intersection() :-The intersection() method returns a new set containing only the elements common to both (or all) sets.
# example1:
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Art', 'Design'}
# remove common courses in  both sets
# print(cs_courses.intersection(art_courses)) # {'History'}

# difference() :-The difference() method returns a new set that contains elements that are in the first set but not in the second.
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Art', 'Design'}
#  it will check whether cs_courses were in art_courses
# as Math, Physics and CompSci is not in the art courses it will print.
# print(cs_courses.difference(art_courses)) # {'CompSci', 'Math', 'Physics'}

# union() :- The union() method returns a new set that contains all unique elements from the sets involved.
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Art', 'Design'}
print(cs_courses.union(art_courses)) # {'Physics', 'Design', 'Math', 'Art', 'History', 'CompSci'}




