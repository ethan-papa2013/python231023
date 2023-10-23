# chatGPT로 생성한 코드

# Lists:
my_list = [1, 2, 3, 4, 5]

# Tuples:
my_tuple = (1, 2, 3, 4, 5)

# Sets:
my_set = {1, 2, 3, 4, 5}

# Dictionaries:
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

# Accessing elements:
print("List:")
print(my_list[0])  # Accessing the first element
print(my_list[1:4])  # Slicing

print("\nTuple:")
print(my_tuple[2])  # Accessing the third element
# Tuples also support slicing like lists

print("\nSet:")
# Sets are unordered, so they don't support indexing
# You can check for membership
print(3 in my_set)
# You can also loop through the elements
for item in my_set:
    print(item)

print("\nDictionary:")
# Accessing values by keys
print(my_dict['two'])  # Accessing value associated with 'two'
# Loop through keys and values
for key, value in my_dict.items():
    print(key, value)

# Mutability:
print("\nMutability:")
# Lists are mutable
my_list[0] = 0
print("List after modification:", my_list)

# Tuples are immutable
# This will result in an error: my_tuple[0] = 0

# Sets are mutable (you can add and remove elements)
my_set.add(6)
my_set.remove(3)
print("Set after modification:", my_set)

# Dictionaries are mutable
my_dict['six'] = 6
del my_dict['three']
print("Dictionary after modification:", my_dict)

# Unique elements:
print("\nUnique elements:")
my_list = [1, 2, 2, 3, 3, 4, 4, 5, 5]
my_set = set(my_list)
print("List with duplicates:", my_list)
print("Set with unique elements:", my_set)
