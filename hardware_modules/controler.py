"""
This is the Controler/Sequencer for the SAP-1.
So basicly the brain of the brain.
"""

# This Will need the Instruction Register to be added
from data_types import Nibble
from module import Module

class Controler(Module):
#atributes
    clock: int
    tState: int
    tStateLen: int

    #command flags
    fClock: bool #clk and inverted clk
    fClear: bool #clr and inverted clr
    
    fCount_next: bool #cp
    fCount_out: bool #ep
    
    fLoad_mar: bool #inverted lm
    fWrite_ram: bool #inverted ce
    
    fLoad_inst: bool #inverted li
    fWrite_inst: bool #inverted ei
    
    fLoad_a: bool #inverted la
    fWrite_a: bool #inverted ea
    fSub: bool #su
    fWrite_alu: bool #eu
    fLoad_b: bool #inverted lb
    
    fload_o: bool #inverted lo

#methods
    def __init__(self) -> None:
        super.__init__(self)
        self.clock = 0
        self.tState = 0
        self.tStateLen = 6

    def setFlags(flags: List[bool] = []) -> None:
        if (flags == []):
            return
        else:
            self.fCount_next = flags[0]
            self.fCount_out = flags[1]
            self.fLoad_mar = flags[2]
            self.fWrite_ram = flags[3]
            self.fLoad_inst = flags[4]
            self.fWrite_inis = flags[5]
            self.fLoad_a = flags[6]
            self.fWrite_a = flags[7]
            self.sub = flags[8]
            self.Write_alu = flags[9]
            self.load_b = flags[10]
            self.load_0 = flags[11]

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
        self.fCount_next: = False
        
