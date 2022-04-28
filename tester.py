import serial
import time
import re




s = 'P1:586P2:1227P3:1374P4:2344D:0P:0.50'
result = re.findall(":(.*[0-9])P", s)
print(result)

# arduino = serial.Serial(port='COM14', baudrate=9600, timeout=1)

# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.1)
#     data = arduino.readline()
#     return data

# while True:
#     num = input("Enter a number: ") # Taking input from user
#     value = write_read(num)
#     print(value.decode('utf-8')) # printing the values 