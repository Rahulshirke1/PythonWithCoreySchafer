# This line prints a message indicating that the module has been imported.
print('Imported my_module...')

# A variable named 'test' is defined and assigned a string value.
test = 'Test String'

# A function named 'find_index' is defined. It takes two arguments:
# 'tosearch' - the sequence to be searched,
# 'target' - the value to search for in the sequence.
def find_index(tosearch, target):
    '''Find the index of a value in a sequence'''  # This is a docstring describing the function.

    # 'enumerate' returns both the index (i) and the value for each item in 'tosearch'
    for i, value in enumerate(tosearch):
        # If the current value matches the target value, return its index
        if value == target:
            return i

    # If the loop completes without finding the target, return -1 to indicate "not found"
    return -1
