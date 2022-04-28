import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from OphirComDriver import OphirComDriver
from MainUIWindow import Ui_MainWindow
# comment to better understand the code
// python -m PyQt5.uic.pyuic UIWindow.ui -o MainUIWindow.py
class test:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        # self.ui.Label1.setText("asd")
        self.ui.pushButton.clicked.connect(self.getValue)

    def show(self):
        self.main_win.show()

    def getValue(self):
        OphirValue = OphirComDriver()
        power = OphirValue.getData()
        self.ui.Label1.setText(str(power))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = test()
    main_win.show()
    sys.exit(app.exec_())