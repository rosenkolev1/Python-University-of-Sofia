from lib2to3.pgen2.token import STRING
import math

class SomeClass:
    x = [10]

    def __init__(self) -> str:
        self.y = [30]

    def __repr__(self):
        return "Hahaha"

inst1 = SomeClass()
inst2 = SomeClass()

inst1.x.append(42)
inst1.y.append(100)

print(f"{inst1.x = }")
print(f"{inst1.y = }")
print(f"{inst2.x = }")
print(f"{inst2.y = }")
print(inst1)

print(math.inf / math.inf)

