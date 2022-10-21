from ctypes import set_errno
import math
from msilib.schema import Error
from sys import settrace


class Player:
    def __init__(self, name, hp = 10, xp = 0) -> None:
        self._name = name
        self._hp = hp
        self._xp = xp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if(value < 0): 
            raise Exception("Nqma stane batko. HP-to ne moje da e < 0")
        self._hp = value

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        if(self.xp > value): 
            raise Exception("Nqma stane batko. XP-to ne moje da se namalqva")
        self._xp = value

    @property
    def level(self):
        return 1 if self.xp < 300 else (2 + int(math.log2(int(self.xp / 300))))

player1 = Player("Roskata")
player1.hp = 50
print(f"{player1.hp = }")
player1.hp = 0
print(f"{player1.hp = }")
# player1.hp = -1
# print(f"{player1.hp = }")
player1.xp = 50
print(f"{player1.xp = }")
print(f"{player1.level = }")
player1.xp = 300
print(f"{player1.xp = }")
print(f"{player1.level = }")
player1.xp = 678
print(f"{player1.xp = }")
print(f"{player1.level = }")
# player1.xp = 677
# print(f"{player1.xp = }")
# print(f"{player1.level = }")
# player1.xp /= 2
# print(f"{player1.xp = }")
# print(f"{player1.level = }")