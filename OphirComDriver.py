# Use of Ophir COM object. 
# Works with python 3.5.1 & 2.7.11
# Uses pywin32
import win32gui
import win32com.client
import time
import traceback

class OphirComDriver:

    def __init__(self):
        self.OphirCOM = win32com.client.Dispatch("OphirLMMeasurement.CoLMMeasurement")
         # Stop & Close all devices
        self.OphirCOM.StopAllStreams() 
        self.OphirCOM.CloseAll()
        self.device = self.OphirCOM.ScanUSB()
        self.DeviceHandle = self.OphirCOM.OpenUSBDevice(self.device[0])	# open first device

    def getData(self):
        self.OphirCOM.StartStream(self.DeviceHandle, 0)
        time.sleep(.2)	
        data = self.OphirCOM.GetData(self.DeviceHandle, 0)
        return data[0][0]



# try:
#  OphirCOM = win32com.client.Dispatch("OphirLMMeasurement.CoLMMeasurement")
#  # Stop & Close all devices
#  OphirCOM.StopAllStreams() 
#  OphirCOM.CloseAll()
#  # Scan for connected Devices
#  DeviceList = OphirCOM.ScanUSB()
#  print(DeviceList)
#  for Device in DeviceList:   	# if any device is connected
#   DeviceHandle = OphirCOM.OpenUSBDevice(Device)	# open first device
#   exists = OphirCOM.IsSensorExists(DeviceHandle, 0)
#   if exists:

#    # An Example for Range control. first get the ranges
#    ranges = OphirCOM.GetRanges(DeviceHandle, 0)
#    print (ranges)
#    # change range at your will
#    if ranges[0] > 0:
#     newRange = ranges[0]-1
#    else:
#     newRange = ranges[0]+1
#    # set new range
#    OphirCOM.SetRange(DeviceHandle, 0, newRange)
   
#    # An Example for data retrieving
#    OphirCOM.StartStream(DeviceHandle, 0)		# start measuring
#    for i in range(10):		
#     time.sleep(.2)				# wait a little for data
#     data = OphirCOM.GetData(DeviceHandle, 0)
#     if len(data[0]) > 0:		# if any data available, print the first one from the batch
#      print('Reading = {0}, TimeStamp = {1}, Status = {2} '.format(data[0][0] ,data[1][0] ,data[2][0]))
     
#   else:
#    print('\nNo Sensor attached to {0} !!!'.format(Device))
# except OSError as err:
#  print("OS error: {0}".format(err))
# except:
#  traceback.print_exc()

# win32gui.MessageBox(0, 'finished', '', 0)
# # Stop & Close all devices
# OphirCOM.StopAllStreams()
# OphirCOM.CloseAll()
# # Release the object
# OphirCOM = None
