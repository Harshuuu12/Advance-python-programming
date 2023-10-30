# Write a Python class named Circle constructed by a radius and two
# methods which will compute the area and the perimeter of a circle

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
radius = float(input("Enter the radius of the circle: "))

circle = Circle(radius)
area = circle.calculate_area()
perimeter = circle.calculate_perimeter()

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)
