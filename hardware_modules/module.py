"""
This is a bace class for all hardware modules
"""

from data_types import Word

class Module():
    input: List[Module]
    output: List[Module]
    value: Word

    def __init__(self, input: List[Module] = [], output: List[Module] = []) -> None:
        self.input = input
        self.output = output

    def value_out(self, output_index: int) -> None:
        self.output[outout_index].value_in(self.value)

    def value_in(self, value: Word) -> None:
        self.value = value
