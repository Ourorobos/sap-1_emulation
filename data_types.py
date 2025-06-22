"""
the 8-bit Byte data type and the nibble 4-bit data type
"""

class Bit_type():
    #This is a single bit object
    value: bool

    def __init__(self):
        #start off False
        self.value = False

    def add(self, freind: Bit_type = Bit_type(), carry: Bit_type = Bit_type()) -> Bit_type
        #This will return a Bit_type with the carry bit info
        carry = self.add(self,carry)#Take care of the carry Bit_type first
        if (self.value and freind.value): #if both are True/1
            self.value = False
            carry.value = True
        elif (self.value or freind.value): #if only one is True/1
            self.value = True
            carry.value = False
        else: #if neather are True/1
            self.value = False
            carry.value = False
        return carry

class Word_type():
    #This is an abstract parent class do NOT use
    value: list
    LENGTH: int
    carry_flag: bool

    def __init__(self):
        #set all bit values to False
        for index in range(0,self.LENGTH):
            value[index] = False

    def add(self, freind: Word_type): -> word_type
        carry: bool = false
        for index in value.len():
            if (self.value[index] and freind.value[index]):
                if (carry):
                    self.value[index] == True
                    carry == True
                else:
                    self.value[index] == False
                    carry == True
            elif ((self.value[index] and not freind.value[index]) or (not self.value[index] and freind.value[index])):
                if (carry):
                    self.value[index] == False
                    carry == True
                else:
                    self.value[index] == True
                    carry == Falsec
        if (carry_flag)
        

class Byte_type():
    value:list = []

    __init__(self):
        #we init all 8-bits to False
        for index in range(0,8):
            value[index] = False

class Nibble_type():
    value:list = []

    __init__(self):
        #we init all 4-bits to False
        for index in range(0,4):
            value[index] = False
