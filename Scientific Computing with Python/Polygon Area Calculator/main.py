"""
To explain this code, first let's start with the imports. The shape_calculator module is imported, which contains the classes Rectangle and Square.

Then, an instance of Rectangle is created with a width of 5 and a height of 10. The get_area() method of this instance is called and the result is printed. The width of the Rectangle instance is then set to 3 using the set_width() method. The get_perimeter() method is called on the Rectangle instance and the result is printed. Finally, the Rectangle instance is printed using the __repr__() method.

Next, an instance of Square is created with a side length of 9. The get_area() method is called on this instance and the result is printed. The side length of the Square instance is then set to 4 using the set_side() method. The get_diagonal() method is called on the Square instance and the result is printed. Finally, the Square instance is printed using the __repr__() method.
"""

# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator


rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

