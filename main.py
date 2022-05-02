import sys
import threading
import time
import random
import concurrent.futures
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from OphirComDriver import OphirComDriver
from MainUIWindow import Ui_MainWindow
from ArduinoDriver import ArduinoDriver
# comment to better understand the code
#  python -m PyQt5.uic.pyuic UIWindow.ui -o MainUIWindow.py
class main:
    def __init__(self):
        self.main_win = QMainWindow()
        self.Arduino = ArduinoDriver()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.pushButton.clicked.connect(self.getValue)
        # self.ui.pushButton2.clicked.connect(self.getValuePositionPiezo)
        self.ui.radioButton.clicked.connect(self.threadThreading)
    def show(self):
        self.main_win.show()

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
    app = QApplication(sys.argv)
    main_win = main()
    main_win.show()
    sys.exit(app.exec_())