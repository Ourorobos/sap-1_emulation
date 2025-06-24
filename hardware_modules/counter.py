"""
This is the 'Program Counter' module.
It's job is to send to the memory the address of the next instruction
"""

from data_types import Nibble
from module import Module
from bus import Bus
from controler import Controler

class Counter(Module):

    value: Nibble
    bus: Bus
    control: Controler

    def __init__(self, bus: Bus, control: Controler) -> None:
        self.bus = bus
        self.control = Controler

    def update(self) -> None:
        #more to be added
        if (not self.control.getClock()):
            self.value.add(Nibble().value = 1)
