"""
This is the Bus Modules file
"""

from data_types import Byte
from register import Register

class Bus(Register):
    #This is just a fancy Register
    value: Byte

    def __init__(self): -> None
        self.value = Byte()
