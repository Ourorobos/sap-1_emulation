"""
This is the 'Program Counter' module.
It's job is to send to the memory the address of the next instruction
"""

from data_types import Nibble_type
from bus import Bus
from controler import Controler

class Counter():
    value: Nibble_type
    bus: Bus
    control: Controler

    def __init__(self, bus: Bus, control: Controler): -> none
        self.bus = bus
        self.control = Controler

    def update(self):
        if (self.control.getClock() == False):
            #next address
