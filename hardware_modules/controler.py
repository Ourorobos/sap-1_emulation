"""
This is the Controler/Sequencer for the SAP-1.
So basicly the brain of the brain.
"""

# This Will need the Instruction Register to be added
from data_types import Nibble_type

class Controler():
    clock: int

    def __init__(self): -> none
        self.clock_flag = 0

    def getClock(self): -> bool
        remain = clock % 2
        if (remian == 0):
            return False
        else:
            return True

    def update_clock(self): -> none
        self.clock += 1
