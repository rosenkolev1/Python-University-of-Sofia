from math import sqrt, sin, cos, atan  # you will need these
from math import pi, isclose
import math  # the tests below will need these

class PolarCoordinate:
    def __init__(self, radius, angle) -> None:
        self._radius = radius
        self._angle = angle

    @property
    def radius(self):
        return self._radius

    @property
    def angle(self):
        return self._angle

    def to_cartesian(self):
        return (self.radius * math.cos(self.angle), self.radius * math.sin(self.angle))

    def from_cartesian(x, y):
        return PolarCoordinate(math.sqrt(x*x + y*y), math.atan(y / x))

    def __repr__(self) -> str:
        return f"PolarCoordinate({self.radius}, {self.angle})"
    
    def __str__(self) -> str:
        return f"(r: {self.radius}, angle: {self.angle})"

    def __hash__(self) -> int:
        return hash((self.radius, self.angle))

    def __eq__(self, other) -> bool:
        return self.radius == other.radius and self.angle == other.angle

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)


p1 = PolarCoordinate(1, pi/6)

print(p1.radius == 1)
print(p1.angle == pi/6)

p2 = PolarCoordinate.from_cartesian(3, 4)
print(isclose(p2.radius, 5))
print(isclose(p2.angle, atan(4/3)))

x, y = p2.to_cartesian()
print(isclose(x, 3))
print(isclose(y, 4))

p3 = PolarCoordinate(1, 0)
print(str(p3) == "(r: 1, angle: 0)")
print(repr(p3) == "PolarCoordinate(1, 0)")

pp1, pp2, pp3 = PolarCoordinate(1, pi/6), PolarCoordinate.from_cartesian(3, 4), PolarCoordinate(1, 0)
print(p1 == pp1)
print(p2 == pp2)
print(p3 == pp3)

d = {p1: "A", p2: "B", p3: "C"}
print(d[pp1] == "A")
print(d[pp2] == "B")
print(d[pp3] == "C")

s = {p1, p2, p3, pp1, pp2, pp3, p1, p2, p3}
print(len(s) == 3)

somePolarShit = PolarCoordinate(10, pi/9)
someOtherPolarShit = PolarCoordinate(20, pi/9)
somePolarShitCopy = PolarCoordinate(10, pi/9)
print(f"{somePolarShit} and {someOtherPolarShit} are equal --> {(somePolarShit == someOtherPolarShit) = }")
print(f"{somePolarShit} and {someOtherPolarShit} are not equal --> {(somePolarShit != someOtherPolarShit) = }")
print(f"{somePolarShit} and {someOtherPolarShit} have the same hash --> {hash(somePolarShit) == hash(someOtherPolarShit) = }")
print(f"{somePolarShit} and {somePolarShitCopy} are equal --> {(somePolarShit == somePolarShitCopy) = }")
print(f"{somePolarShit} and {somePolarShitCopy} are not equal --> {(somePolarShit != somePolarShitCopy) = }")
print(f"{somePolarShit} and {somePolarShitCopy} have the same hash --> {hash(somePolarShit) == hash(somePolarShitCopy) = }")