"""
some notes here that I have not made
"""

from data_types import Command, Nibble

class Instruction():
    name: str
    code: Nibble
    command: List[Command]

#Tools 0-4
class NOP(Instruction):

    def __init__(self) -> None:
        self.name = "No Operation"
        self.code = Nibble()
        self.code.setInt(0)
        self.command = [
            
        ]

#Registers 5-10
class LDA(Instruction):

    def __init__(self):
        self.name = "Load A Register"
        self.code = Nibble()
        self.code.setInt(5)
        self.command = [
            #stuff
        ]

class LDB(Instruction):

    def __init__(self) -> None:
        self.name = "Load B Register"
        self.code = Nibble()
        self.code.setInt(6)
        self.commad = [
            #more stuff
        ]

class LDO(Instruction):

    def __init__(self) -> None:
        self.name = "Load Output Register"
        self.code = Nibble()
        self.code.setInt(7)
        self.command = [
            #Other stuff
        ]

#Alu 10-15
class ADD(Instruction):

    def __init__(self) -> None:
        self.name = "ADD A & B Register"
        self.code = Nibble()
        self.code.setInt(10)
        self.command = [
            
        ]

class SUB(Instruction):

    def __init__(self) -> None:
        self.name = "Subtract A & B Register"
        self.code = Nibble()
        self.code.setInt(11)
        self.command = [
            
        ]
