# Entrypoint file 
# The shape_calculator module is imported, which contains the classes Rectangle and Square.
import shape_calculator

# An instance of Rectangle is created with a width of 5 and a height of 10.
rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area()) # The get_area() method of this instance is called and the result is printed.
rect.set_width(3) # The width of the Rectangle instance is then set to 3 using the set_width() method
print(rect.get_perimeter()) # The get_perimeter() method is called on the Rectangle instance and the result is printed
print(rect) # The Rectangle instance is printed using the __repr__() method.

# An instance of Square is created with a side length of 9.
sq = shape_calculator.Square(9)
print(sq.get_area()) # The get_area() method is called on this instance and the result is printed.
sq.set_side(4) #  The side length of the Square instance is then set to 4 using the set_side() method.
print(sq.get_diagonal()) # The get_diagonal() method is called on the Square instance and the result is printed.
print(sq) # The Square instance is printed 

