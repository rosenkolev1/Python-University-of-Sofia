import math
from re import X
import string

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        if (isinstance(other, Vector3D)):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        return Vector3D(self.x + other, self.y + other, self.z + other)      

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self = self + other
        return self
    
    def __mul__(self, other):
        if (isinstance(other, Vector3D)):
            newVectorX = self.y * other.z - self.z * other.y 
            newVectorY = self.z * other.x - self.x * other.z 
            newVectorZ = self.x * other.y - self.y * other.x
            return Vector3D(newVectorX, newVectorY, newVectorZ) 
        return Vector3D(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        if (isinstance(other, Vector3D)):
            other.__mul__(self)
        return self * other

    def __imul__(self, other):
        self = self * other
        return self

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other) -> bool:
        return not self == other

    def __abs__(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def __getattr__(self, name):
        if(name.lower() == "x"): 
            return self.x
        elif(name.lower() == "y"):
            return self.y
        elif(name.lower() == "z"):
            return self.z

    def __setattr__(self, name, value):
        if(name.lower() == "x"): 
            self.__dict__[name.lower()] = value
        elif(name.lower() == "y"):
            self.__dict__[name.lower()] = value
        elif(name.lower() == "z"):
            self.__dict__[name.lower()] = value

    def __iter__(self):
        return iter([self.x, self.y, self.z])

vector1 = Vector3D(1, 1, 2)
vector2 = Vector3D(2, 3, 1)

print(f"Add {vector1} to 10 --> {vector1 + 10 = }")
print(f"Add 10 to {vector1} --> {10 + vector1 = }")
vector1 += 10
print(f"Add {vector1} to 10 and return {vector1}, then print it --> {vector1}")
#reverse the vector1 back to its original value
vector1 += -10
print(f"Add {vector1} to {vector2} --> {vector1 + vector2 = }")

print(f"Multiply {vector1} by -2 --> {vector1 * -2 = }")
print(f"Multiply -2 by {vector1} --> {-2 * vector1 = }")
vector1 *= -2
print(f"Multiply {vector1} by -2 and return {vector1}, then print it --> {vector1}")
#reverse the vector1 back to its original value
vector1 *= -0.5
print(f"Multiply {vector1} to {vector2} --> {vector1 * vector2 = }")
print(f"Multiply {vector2} to {vector1} --> {vector2 * vector1 = }")

print(f"Check if {vector1} == {vector2} --> {(vector1 == vector2) = }")    
print(f"Check if {vector1} != {vector2} --> {(vector1 != vector2) = }")  
vector1Copy = Vector3D(vector1.x, vector1.y, vector1.z)
print(f"Check if {vector1} == {vector1Copy} --> {(vector1 == vector1Copy) = }")
print(f"Check if {vector1} != {vector1Copy} --> {(vector1 != vector1Copy) = }")            
print(f"Check if {vector1} has the same hash as {vector2} --> {(hash(vector1) == hash(vector2)) = }")   
print(f"Check if {vector1} has the same hash as {vector1Copy} --> {(hash(vector1) == hash(vector1Copy)) = }")  

print(f"Magnitude/Abs of {vector1} is --> {abs(vector1) = }")

print(f"X of {vector1} is --> {vector1.X = }")
print(f"Y of {vector1} is --> {vector1.Y = }")
print(f"Z of {vector1} is --> {vector1.Z = }")

vector1.X = 5
print(f"Setting x of {vector1} to 5 --> {vector1.x =  }")
vector1.Y = 6
print(f"Setting y of {vector1} to 6 --> {vector1.Y = }")
vector1.Z = 7
print(f"Setting z of {vector1} to 7 --> {vector1.Z = }")

for coord in vector1:
    print(f"The coordinate of {vector1} is --> {coord}")

