"""
This file contains a class that hold all the modules
Provides all the needed conections
"""

from data_types import Command

from hardware_modules.module import Register
from hardware_modules.bus import Bus
from hardware_modules.counter import Counter
from hardware_modules.ram import Ram
from hardware_modules.controler import Controler

class SAP-1():
    self.command: Command
    
    self.bus: Bus
    self.counter: Counter
    self.mar: Register
    self.ram: Ram
    self.ir: Register
    self.controler: Controler
    self.adr: Register
    #alu
    self.bdr: Register
    self.odr: Register
    #display

    def __init__(self) -> None:
        self.bus = Bus()
        self.mar = Register(self.ram)
        self.ram = Ram(self.bus)
        self.ir = Register(self.controler)
        self.controler = Controler()
        self.adr = Register(self.bus)
        #alu
        self.bdr = Register()
        self.odr = Register()#self.display

    def update(self) -> None:
        pass
    
        
