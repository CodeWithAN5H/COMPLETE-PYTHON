# calc area of circle
import math

radius = float(input("Enter radius of circle: "))
area = math.pi * pow(radius, 2)

print(f"The area of the circle is {round(area, 2)}cm²")