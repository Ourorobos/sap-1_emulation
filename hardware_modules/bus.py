"""
This is the Bus Modules file
"""

from data_types import Byte
from module import Module

class Bus(Module):
    value: Byte

    def __init__(self) -> None:
        self.value = Byte()
