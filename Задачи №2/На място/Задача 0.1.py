
import math


class Rectangle:

    def __init__(self, width, height, colour):
        self._width = width
        self._height = height
        self._colour = colour
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

    @property
    def colour(self):
        return self._colour
    
    def calculateArea(self):
        return self.width * self.height

someRectangle = Rectangle(3, 4, "red")
print(f"Calculate area of a triangle with sides {someRectangle.height} and {someRectangle.width} that is red: {someRectangle.calculateArea()}")

class Circle:
    def __init__(self, radius, colour) -> None:
        self._radius = radius
        self._colour = colour

    @property
    def radius(self):
        return self._radius

    @property
    def colour(self):
        return self.colour

    def calculateArea(self):
        return self.radius * self.radius * math.pi

someCircle = Circle(3, "yellow")
print(f"Calculate area of a triangle with radius {someCircle.radius} that is yellow: {someCircle.calculateArea()}")

class Shapes:
    def __init__(self) -> None:
        self.shapes = []

    def addShape(self, shape):
        self.shapes.append(shape)

    def removeShape(self, shape):
        self.shapes.pop()

    def sumOfRectangles(self):
        return sum([(shape.calculateArea() if isinstance(shape, Rectangle) else 0) for shape in self.shapes])

    def sumOfCircles(self):
        return sum([(shape.calculateArea() if isinstance(shape, Circle) else 0) for shape in self.shapes])

    def _indexInBounds(self, index):
        return index >= 0 and index < len(self.shapes) 

    def getShape(self, index):
        return self.shapes[index] if self._indexInBounds(index) else "Ne ba4ka"

shapeCollector = Shapes()

shapeCollector.addShape(someRectangle)
shapeCollector.addShape(someCircle)
shapeCollector.addShape(Rectangle(2, 2, "white"))
shapeCollector.addShape(Circle(1, "blue"))

print(f"Sum of rectangle areas is: Expected 16 --> {shapeCollector.sumOfRectangles()}")
print(f"Sum of circle areas is: Expected ~31 --> {shapeCollector.sumOfCircles()}")

print(f"The element at index 2 should be a white rectangle with sides 2, 2: Expected white, 2, 2 --> {shapeCollector.getShape(2).colour}, {shapeCollector.getShape(2).height}, {shapeCollector.getShape(2).width}")