"""
the 8-bit Byte data type and the nibble 4-bit data type
"""

class Word():
    #This is an abstract parent class do NOT use
    value: int
    length: int = 64 #possible max?

    def __init__(self) -> None:
        #inti to zero
        value = 0

    def getBitMask(bit_place: int = 0) -> int:
        return 2**(bit_place - 1)

    def add(self, freind) -> None:
        self.value += freind.value

    def sub(self, freind) -> None:
        self.value -= freind.value

    def getBit(bit_place: int = 0) -> None:
        if (self.value & self.getBitMask(bit_place) != 0):
            return True
        else:
            return False

    def toggleBit(bit_place: int = 0) -> None:
        self.value ^= bit_place

    def getCarryBit(self) -> bool:
        return getBit(length+1)

    def setInt(self, value: int) -> None:
        self.value = value

    def getInt(self) -> int:
        return self.value

class Byte(Word):
    length: int = 8

    def getUpper(self) -> Nibble:
        nibble = Nibble()
        nibble.setInt(self.value & 240)
        return nibble

    def getLower(self) -> Nibble:
        nibble = Nibble()
        nibble.setInt(self.value & 15)

class Nibble(Word):
    length: int = 4

class Command(Word):
    length: int = 12
