# object = A "bundle" of related attributes (variables) and methods (functions)
# Ex. phone, cup, book
# You need a "class" to create many objects
#
# class  = (blueprint) used to design the structure and layout of an object

from car import Car

c1 = Car('Mercedes', 2020, 'White', False)
c2 = Car('BMW', 2025, 'Black', True)
c3 = Car('Bugatti', 2026, 'Blue', True)

c3.drive()
c3.describe()