import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from OphirComDriver import OphirComDriver
from MainUITestWindow import Ui_MainWindow
from ArduinoDriver import ArduinoDriver
# comment to better understand the code
#  python -m PyQt5.uic.pyuic UIWindow.ui -o MainUIWindow.py
class main:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.radioButton.clicked.connect(self.testvalue)

    def testvalue(self):
        testKasper = self.ui.radioButton.isChecked()
        hi = 1
    def show(self):
        self.main_win.show()

    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = main()
    main_win.show()
    sys.exit(app.exec_())