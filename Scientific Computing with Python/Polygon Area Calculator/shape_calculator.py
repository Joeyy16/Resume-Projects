"""
The __init__ method is a special method in Python classes that is called when an instance of the class is created. It is often referred to as the constructor of the class.

In this case, the __init__ method of the Rectangle class takes two arguments: w and h. These arguments represent the width and height of the rectangle, respectively. The method assigns the values of these arguments to the instance variables self.width and self.height, respectively.

For example, if you create an instance of the Rectangle class like this: rect = Rectangle(5, 10), then rect.width would be equal to 5 and rect.height would be equal to 10.
"""

class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        
    """
    The __str__ method is used to define a string representation of the Rectangle class. This method returns a string that can be used to represent the object when printed. In this case, the string representation of the Rectangle object will contain the values of the width and height attributes. This method is useful when you want to print an object and have it display a more human-readable representation of itself.
    """
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    """
    This is a method of the Rectangle class that sets the width of the rectangle to a new value w. The method takes in an argument w, which is the new value for the width of the rectangle. The method sets the value of the width attribute of the Rectangle instance to the value of w. This method allows the user to change the width of the rectangle after it has been initialized.
    """
    def set_width(self, w):
        self.width = w

    """
    This is a method of the Rectangle class that allows you to set the value of the height attribute of an instance of the Rectangle class. The method takes in a single argument h, which is the new value that will be assigned to the height attribute of the instance. The value of the height attribute is updated by using the assignment operator = to set the value of self.height to the value of the h argument. This method does not return any value.
    """
    def set_height(self, h):
        self.height = h

    """
    The method get_area() is a function defined within the Rectangle class that calculates and returns the area of the rectangle object. It does this by multiplying the values stored in the object's width and height attributes. The width and height attributes represent the dimensions of the rectangle object and are set when the object is created using the __init__() method.
    """
    def get_area(self):
        return self.width * self.height

    """
    The get_perimeter() method is a member function of the Rectangle class. It calculates the perimeter of a rectangle object by multiplying the width and height of the object and returning the result. The perimeter is defined as the distance around the outer edges of a shape. In the case of a rectangle, the perimeter is equal to twice the sum of the width and height of the rectangle. This method takes no arguments and returns a single value, which is the perimeter of the rectangle object on which the method is called.
    """
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    """
    "get_diagonal" is a method of the "Rectangle" class that calculates and returns the length of the diagonal of the rectangle. The diagonal is a line segment connecting two non-adjacent vertices of the rectangle. It is calculated using the Pythagorean theorem, which states that the square of the hypotenuse (the diagonal in this case) is equal to the sum of the squares of the other two sides (the width and the height of the rectangle). In this method, the width and the height of the rectangle are squared and their sum is then taken to the power of 0.5 to find the square root, which is the length of the diagonal.
    """
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    """
    This is a method of the Rectangle class that returns a string representation of the rectangle as an ASCII art picture. The method first checks if the width or height of the rectangle is greater than 50, and if either is, it returns a string saying that the rectangle is too big to fit in a picture. Otherwise, it creates a string with self.width number of * characters, followed by a newline character, and then repeats this string self.height number of times. Finally, it returns the resulting string.
    """
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        pic = '*' * self.width + '\n'
        pic = pic * self.height
        return pic

    """
    This method get_amount_inside calculates the number of instances of the object ob that can fit inside the current rectangle object. It does this by dividing the area of the current rectangle by the area of the object ob. The result of this division is returned as an integer, since it represents a count of objects that can fit inside the rectangle.

    For example, if the current rectangle has a width of 10 and a height of 20, and ob has a width of 5 and a height of 5, then the number of instances of ob that can fit inside the rectangle is calculated as follows:

    (10 * 20) // (5 * 5) = 200 // 25 = 8

    Therefore, the method would return 8 as the result.
    """
    def get_amount_inside(self, ob):
        return self.get_area() // ob.get_area()

    """
    The Square class is a subclass of Rectangle. It has the same methods as Rectangle, but the set_width and set_height methods have been overridden to set both the width and height to the same value, since a square has equal sides. The __init__ method of the Square class calls the __init__ method of the Rectangle class with the same value for the width and height, which sets the width and height of the Square object to the same value. The __str__ method of the Square class has also been overridden to return a string with the side length of the square, rather than the width and height of the rectangle.
    """
class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, s):
        self.width = s
        self.height = s
