import sys
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
        self.ui.pushButton2.clicked.connect(self.getValuePositionPiezo)

    def show(self):
        self.main_win.show()

    def getValue(self):
        OphirValue = OphirComDriver()
        power = OphirValue.getData()
        self.ui.Label1.setText(str(power))

    def getValuePositionPiezo(self):
        position = self.Arduino.write_read()
        self.ui.Label2.setText(str(position))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = main()
    main_win.show()
    sys.exit(app.exec_())