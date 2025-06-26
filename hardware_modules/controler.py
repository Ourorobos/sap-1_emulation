"""
This is the Controler/Sequencer for the SAP-1.
So basicly the brain of the brain.
"""

# This Will need the Instruction Register to be added
from data_types import Nibble, Word
from module import Module

class Controler(Module):
#atributes
    clock: int
    tState: int
    tStateLen: int
    wControl: Word #This is layed out the same as in the book Lo at the lowest and Cp at the highest

#methods
    def __init__(self) -> None:
        super.__init__(self)
        self.clock = 0
        self.tState = 0
        self.tStateLen = 6
        self.wControl.length = 12
        self.wControl.setInt(0)
    #clock
    def getClock(self) -> None:
        remain = clock % 2
        if (remian == 0):
            return False
        else:
            return True

    def update_clock(self) -> None:
        self.clock += 1    

    #states    
    def address(self) -> None:
        #undo the last state(the instruction state)
        self.wControl.setInt(0)
        #set the program counter out bit
        self.wControl.toggleBit(11)
        #set the Load MAR bit
        self.wControl.toggleBit(10)

    def increment(self) -> None:
        #undo the last state(the addres state)
        self.wControl.setInt(0)
        #set program counter count bit
        self.wControl.toggleBit(12)

    def memory(self) -> None:
        #undo the last state(the increment state)
        self.wControl.setInt(0)
        #set the RAM out bit
        self.wControl.toggleBit(9)
        #set the instruction in bit
        self.wControl.toggleBit(8)

    def instruction(self) -> None:
        #undo the last state(the memory state)
        self.wControl.setInt(0)
        
