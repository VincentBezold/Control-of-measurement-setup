import serial
import time


class ArduinoDriver:

    def __init__(self):
        self.arduino = serial.Serial(port='COM14', baudrate=9600, timeout=1)


    def write_read(self):
        self.arduino.write(bytes('M', 'utf-8'))
        time.sleep(0.1)
        data = self.arduino.readline()
        return data

    # while True:
    #     num = input("Enter a number: ") # Taking input from user
    #     value = write_read(num)
    #     value.decode('utf-8') # printing the values