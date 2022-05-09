# import pyvisa
# rm = pyvisa.ResourceManager()
# print(rm.list_resources())
import pyvisa
import json, os
import time
# import numpy as np
from datetime import datetime


class PiezoDriver:
    def __init__(self):
        rm = pyvisa.ResourceManager()
        self.inst = rm.open_resource('ASRL9::INSTR')
        self.inst.baud_rate = 38400
                
    def moveContinuesUp(self, channel):
        time.sleep(1)
        self.inst.write("setm " + str(channel)+" stp\n")
        self.inst.write("stepu " + str(channel)+" c\n")
        time.sleep(2)
        self.stop(str(channel))
        self.inst.write("setm " + str(channel)+" gnd\n")


    def moveContinuesDown(self, channel):
        # time.sleep(1)
        self.inst.write("setm " + str(channel)+" stp\n")
        self.inst.write("stepd " + str(channel)+" c\n")
        time.sleep(1)
        self.stop(str(channel))
        self.inst.write("setm " + str(channel)+" gnd\n")

    def stop(self, channel):
        print(self.inst.query("stop " + str(channel) + "\n"))
        
    def stepUp(self, channel, numberSteps):
        self.inst.write("setm " + str(channel)+" stp\n")
        self.inst.write("stepu " + str(channel) + " " + str(numberSteps) + "\n")
        self.inst.write("stepw " + str(channel)+"\n")
        self.inst.write("setm " + str(channel)+" gnd\n")
    
    def stepDown(self, channel, numberSteps):
        self.inst.write("setm " + str(channel)+" stp\n")
        self.inst.write("stepd " + str(channel) + " " + str(numberSteps))
        self.inst.write("stepw " + str(channel)+"\n")
        self.inst.write("setm " + str(channel)+" gnd\n")
 

test = PiezoDriver()

test.moveContinuesUp(5) # works
time.sleep(1) # works
test.stepDown(2, 300) # works
time.sleep(1)
test.moveContinuesUp(2)


# https://www.aps.anl.gov/files/APS-Uploads/SECTOR27/Manual%20ANC300%20v3.1.pdf