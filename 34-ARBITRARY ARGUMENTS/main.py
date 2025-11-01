# *args       = allows you to pass multiple non-key arguments
# **kwargs    = allows you to pass multiple keyword-arguments
#              * unpacking operator
#              1. positional 2. default 3. keyword 4. ARBITRARY

# EXAMPLE 1
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1,2,3))

# EXAMPLE 2
# def display_name(*args):
#     print("Hello!", end=" ")
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Ansh", "Singh", 1)