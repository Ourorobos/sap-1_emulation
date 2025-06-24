"""
This is the Controler/Sequencer for the SAP-1.
So basicly the brain of the brain.
"""

# This Will need the Instruction Register to be added
from data_types import Nibble
from module import Module

class Controler(Module):
    clock: int

    def __init__(self) -> None:
        super.__init__(self)
        self.clock = 0

    def getClock(self) -> None:
        remain = clock % 2
        if (remian == 0):
            return False
        else:
            return True

    def update_clock(self) -> None:
        self.clock += 1
