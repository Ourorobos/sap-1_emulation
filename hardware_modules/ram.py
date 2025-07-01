"""
This is the RAM class
"""

from data_types import Byte, Nibble
from module import Module

class Ram(Module):
    value: Nibble
    size: Nibble
    mem: List[Byte]

    def __init__(self, size) -> None:
        self.size = size

    def value_out(self, target: Module) -> None:
        target.value.setInt(self.mem[self.value.getInt()].getInt())
