"""
This is a bace class for the register modules
"""

from data_types import Word

class Register():
    value: Word

    def __init__(self):
        self.value = Word()

    def value_in(self, data: Word): -> None
        self.value = data.value

    def value_out(self): -> Word
        return self.value
