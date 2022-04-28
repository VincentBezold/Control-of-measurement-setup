import serial
import time
import re


class ArduinoDriver:

    def __init__(self):
        self.arduino = serial.Serial(port='COM14', baudrate=9600, timeout=1)


    def write_read(self):
        self.arduino.write(bytes('M', 'utf-8'))
        time.sleep(0.1)
        data = self.arduino.readline().decode('utf-8').split(",")
        return data

