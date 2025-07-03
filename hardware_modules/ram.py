"""
This is the RAM class
"""

from data_types import Byte, Nibble
from module import Module
from controler import Controler
from bus import Bus

class Ram(Module):
    value: Nibble
    size: Nibble
    mem: List[Byte]
    bus: Bus
    control : Controler

    def __init__(self, bus: Bus, control: Controler, size: Nibble) -> None:
        self.bus = bus
        self.control = control
        self.size = size

    def value_out(self, target: Module) -> None:
        target.value.setInt(self.mem[self.value.getInt()].getInt())

    def update(self):
        if (self.control.getCommandFlag()):
            self.value_out(self.bus)
