"""
This is the Controler/Sequencer for the SAP-1.
So basicly the brain of the brain.
"""

# This Will need the Instruction Register to be added
from data_types import Nibble
from module import Module

class Controler(Module):
    clock: int
    tState: int
    tStateLen: int

    #command flags
    fClock: bool #clk and inverted clk
    fClear: bool #clr and inverted clr
    
    fCount_next: bool #cp
    fCount_out: bool #ep
    
    fload_mar: bool #inverted lm
    fWrite_ram: bool #inverted ce
    
    fload_inst: bool #inverted li
    fWrtie_inst: bool #inverted ei
    
    fLoad_a: bool #inverted la
    fWrite_a: bool #inverted ea
    fSub: bool #su
    fWrite_alu: bool #eu
    fLoad_b: bool #inverted lb
    
    fload_o: bool #inverted lo

    def __init__(self) -> None:
        super.__init__(self)
        self.clock = 0
        self.tState = 0
        self.tStateLen = 6

    def getClock(self) -> None:
        remain = clock % 2
        if (remian == 0):
            return False
        else:
            return True

    def update_clock(self) -> None:
        self.clock += 1    
