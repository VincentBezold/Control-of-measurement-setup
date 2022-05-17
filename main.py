import sys
import threading
import sys
import time
import random
import concurrent.futures
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from OphirComDriver import OphirComDriver
from MainUIWindow import Ui_MainWindow
from ArduinoDriver import ArduinoDriver
from PiezoDriverPyVisa import PiezoDriver

# To do: integration of slider with help of dynamcly creating varibel names

# comment to better understand the code
#  python -m PyQt5.uic.pyuic UIWindow.ui -o MainUIWindow.py
class main:
    def __init__(self):
        
        self.main_win = QtWidgets.QMainWindow()
        
        # self.Arduino = ArduinoDriver()
        self.ui = Ui_MainWindow()
        self.piezoDriver = PiezoDriver()
        self.ui.setupUi(self.main_win)
        self.ui.pushButton.clicked.connect(self.getValue)
        self.ui.radioButton.clicked.connect(self.threadThreading)
        self.ui.contUpGroup.buttonClicked.connect(self.contUp)
        self.ui.stepUpGroup.buttonClicked.connect(self.stepUp)
        
        
        aa = 1
        # self.ui.contDownGroup.buttonClicked.connect(self.contDown)
        # self.ui.stepDownGroup.buttonClicked.connect(self.stepDown)

    def show(self):
        self.main_win.show()
        

    def contUp(self, button):
        button_number = int(button.objectName()[7:])
        self.test = self.ui.horizontalSlider.value()
        # self.piezoDriver.moveContinuesUp(button_number)

    def stepUp(self, button):
        button_number = int(button.objectName()[7:])
        # self.piezoDriver.stepUp(button_number, numberSteps)

    def getValue(self):
        OphirValue = OphirComDriver()
        power = OphirValue.getData()
        self.ui.Label1.setText(str(power))

    def threadThreading(self, devicefunction):
        if self.ui.radioButton.isChecked():
            t1 = threading.Thread(target=self.getValuePositionPiezo)
            t1.start()

    # def threading(self):
    #     if self.ui.radioButton.isChecked():
    #         with concurrent.futures.ThreadPoolExecutor() as executor:
    #             f = executor.submit(self.getValuePositionPiezo)

    def getValuePositionPiezo(self):
        # start = time.perf_counter()
        while self.ui.radioButton.isChecked():
            position = self.Arduino.write_read()
            self.ui.Label2.setText(str(position))
            # finish = time.perf_counter()

            # print(f'Finished in {round(finish-start, 2)} second(s)')




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = main()
    
    File = open("theme/SpyBot.qss",'r')
    with File:
        qss = File.read()
        app.setStyleSheet(qss)

    main_win.show()
    sys.exit(app.exec_())