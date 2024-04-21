# ALX Higher Level Programming - 0x0C Python Almost a Circle

This repository contains solutions to the tasks in the ALX Higher Level Programming sprint for the Python Almost a Circle section. The tasks involve implementing classes and methods to create a representation of shapes, with a focus on circles and rectangles.

## Solutions

1. **[Rectangle Class](./models/rectangle.py)** - Contains the implementation of the Rectangle class.
2. **[Square Class](./models/square.py)** - Contains the implementation of the Square class, a subclass of Rectangle.
3. **[Base Class](./models/base.py)** - Contains the implementation of the Base class, with methods for JSON serialization and deserialization.
4. **[JSON File Handling](./models/__init__.py)** - Implements methods for saving and loading instances to and from JSON files.

## Usage

To use the classes provided in this repository, simply import them into your Python script and instantiate objects as needed. For example:

```python
from models.rectangle import Rectangle

# Create a rectangle with width 5 and height 10
my_rectangle = Rectangle(5, 10)

# Get the area of the rectangle
area = my_rectangle.area()
print("Area:", area)


## About the Author
This repository was created by Emmanuel Odenyire Anyira, a student at ALX Africa, currently enrolled in the ALX Software Engineering Program.
Emmanuel is also a Senior Data Analytics Engineer at Safaricom PLC in Kenya.

For collaborations or inquiries, feel free to contact Emmanuel via:

Email: eodenyire@gmail.com
LinkedIn: Emmanuel Odenyire Anyira
