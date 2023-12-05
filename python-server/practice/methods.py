import typing

# List Methods and Comprehension Examples
def list_examples():
    my_list = [1, 2, 3]
    my_list.append(4)   # Append
    my_list.extend([5, 6])  # Extend
    my_list.insert(2, 'a')  # Insert
    my_list.remove('a')  # Remove
    last_item = my_list.pop()  # Pop
    unsorted_list = [3, 1, 4, 1]
    unsorted_list.sort()  # Sort
    my_list.reverse()  # Reverse
    sliced_list = my_list[1:3]  # Slicing

    # List Comprehension
    squared_list = [x * x for x in my_list]

    # Iterating over a list
    for item in my_list:
        print("List iteration:", item)

    print("List methods:", my_list, unsorted_list, sliced_list, squared_list)

# Set Methods and Iteration Examples
def set_examples():
    my_set = {1, 2}
    my_set.add(3)  # Add
    my_set.remove(2)  # Remove
    my_set.discard(4)  # Discard
    another_set = {3, 4}
    union_set = my_set.union(another_set)  # Union
    intersect_set = my_set.intersection(another_set)  # Intersection
    difference_set = my_set.difference(another_set)  # Difference

    # Iterating over a set
    for item in my_set:
        print("Set iteration:", item)

    print("Set methods:", my_set, union_set, intersect_set, difference_set)

# Dictionary Methods and Iteration Examples
def dictionary_examples():
    my_dict = {'a': 1, 'b': 2}
    keys = my_dict.keys()  # Keys
    values = my_dict.values()  # Values
    items = my_dict.items()  # Items
    value = my_dict.get('a')  # Get
    my_dict.update({'c': 3})  # Update

    # Dictionary Comprehension
    squared_dict = {x: x * x for x in range(4)}

    # Iterating over a dictionary
    for key, value in my_dict.items():
        print("Dict iteration:", key, value)

    print("Dictionary methods:", keys, values, items, value, squared_dict)

# String Methods and Iteration Examples
def string_examples():
    text = "hello world"
    words = text.split()  # Split
    joined_text = ' '.join(words)  # Join
    first_word = text[:5]  # Slicing

    # Iterating over a string
    for char in text:
        print("String iteration:", char)

    print("String methods:", words, joined_text, first_word)

# General Functions Examples
def general_functions():
    my_list = [1, 2, 3, 4, 5]
    length = len(my_list)  # Len
    for i in range(5):  # Range
        print("Range example:", i)
    for index, value in enumerate(my_list):  # Enumerate
        print("Enumerate example:", index, value)
    for num, letter in zip([1, 2, 3], ['a', 'b', 'c']):  # Zip
        print("Zip example:", num, letter)

def tuple_examples():
    my_tuple = (1, 2, 3, 1, 1, 4)
    print(my_tuple.count(1))  # Output: 3
    print(my_tuple.index(3))  # Output: 2
    a, b, c, _, _, d = my_tuple
    print(a, b, c, d)  # Output: 1 2 3 4
    sliced_tuple = my_tuple[1:4]  # (2, 3, 1)

# Lambda functions:
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

points = [(1, 2), (3, 3), (5, 1), (2, 4)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(5, 1), (1, 2), (3, 3), (2, 4)]

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10, 12]

# Running all examples
list_examples()
set_examples()
dictionary_examples()
string_examples()
general_functions()
