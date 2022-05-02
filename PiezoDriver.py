# import pyvisa
# rm = pyvisa.ResourceManager()
# print(rm.list_resources())
import pyvisa
import json, os
# import numpy as np
from datetime import datetime

class PiezoDriver:
    def __init__(self):
        rm = pyvisa.ResourceManager()
        self.inst = rm.open_resource('ASRL9::INSTR')
        test = 1
        
    

test = PiezoDriver()
# test.setUnit('a', 'l')
# print(test.readTemp('a'))