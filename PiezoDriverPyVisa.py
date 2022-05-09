import pyvisa
import json, os
import time
from datetime import datetime
# https://www.aps.anl.gov/files/APS-Uploads/SECTOR27/Manual%20ANC300%20v3.1.pdf

class PiezoDriver:
    def __init__(self):
        rm = pyvisa.ResourceManager() # some visa magic
        self.inst = rm.open_resource('ASRL9::INSTR') # opens port
        self.inst.baud_rate = 38400 # sets baudrate
                
    def moveContinuesUp(self, channel):
        time.sleep(1)
        self.inst.write("setm " + str(channel)+" stp\n") # sets mode to stp (step)
        self.inst.write("stepu " + str(channel)+" c\n") # starts continues mode
        time.sleep(2)
        self.stop(str(channel))
        self.inst.write("setm " + str(channel)+" gnd\n") # set piezos back to ground


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
        self.inst.write("stepu " + str(channel) + " " + str(numberSteps) + "\n") # starts starts step mode
        self.inst.write("stepw " + str(channel)+"\n") # waits until steps are done
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


