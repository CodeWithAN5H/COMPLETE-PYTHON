# list comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# EXAMPLE 1
doubles = [x * 2 for x in range(1,11)]
print(doubles)

# EXAMPLE 2
fruits = ['apple', 'banana', 'orange', 'strawberry']
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

# EXAMPLE 3
numbers = [1,-2, 3, -4, 5, -6]
positive_num = [num for num in numbers if num >= 0]
print(positive_num)