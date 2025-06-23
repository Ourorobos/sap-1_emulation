"""
the 8-bit Byte data type and the nibble 4-bit data type
"""

class Word():
    #This is an abstract parent class do NOT use
    value: int
    length: int = 64 #possible max?

    def __init__(self): -> None
        #inti to zero
        value = 0

    def getBitMask(bit_place: int = 0): -> int
        return 2**(bit_place - 1)

    def add(self, freind): -> None
        self.value += freind.value

    def sub(self, freind): -> None
        self.value -= freind.value

    def getBit(bit_place: int = 0): -> bool
        if (self.value & self.getBitMask(bit_place) != 0):
            return True
        else:
            return False

    def getCarryBit(self): -> bool
        return getBit(length+1)

class Byte(Word):
    length: int = 8

class Nibble(Word):
    length: int = 4
