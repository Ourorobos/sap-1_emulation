"""
This is the Controler/Sequencer for the SAP-1.
So basicly the brain of the brain.
The Clock is part of the 'layout'.
"""

# This Will need the Instruction Register to be added
from data_types import Nibble, Byte, Command
from routine import Instruction, NOP, LDA
from module import Module

class Controler(Module):
#atributes
    value: Byte
    instruction: Instruction
    tState: int
    tStateLen: int = 6
    wControl: Command #This is layed out the same as in the book Lo at the lowest and Cp at the highest

    wAddress: Command
    wIncrement: Command
    wMemory: Command

#methods
    def __init__(self) -> None:
        super.__init__(self)
        self.tState = 0
        self.wControl.setInt(0)

    def getInstruction(self) -> None:
        temp = self.value.getUpper()
        #this is just hard coded for now
        #how long until I fix this?
        match temp.getInt():
            
            case NOP().code.getInt():
                self.instruction = NOP()
            case LDA().code.getInt():
                self.instruction = LDA()
    
            #default
            case _:
                self.instruction = NOP()

    def getCommand(self) -> Word:
        #find state
        match self.tState:
            case 0:
                return self.wAddress
            case 1:
                return self.wIncrement
            case 2:
                return self.wMemory
            case 3:
                self.getInstruction()
                return self.instruction.command[0]
            case 4:
                return self.instruction.command[1]
            case 5:
                return self.instruction.command[2]
            case _:
                self.tState = 0
                #self.tState = 4
                #self.instruction = RESET()
               # return self.instruction.command[0]

    def getCommandFlag(self, index: int) -> bool:
        return self.wControl.getBit(index)

    def update(self) -> None:
        self.wControl = self.getCommand()
        self.tState += 1
        self.tState %= self.tStateLen
