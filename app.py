from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from root import Ui_Root

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.title = "Awesome SMS"
        self.date = datetime.now().strftime("%B %d, %Y")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 343)
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        MainWindow.setWindowIcon(QtGui.QIcon('ed.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(2, 210, 175, 30))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 240, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.quit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 9, 438, 108))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(62)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 119, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 150, 151, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 150, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 120, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 240, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.init_root)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(28, 240, 100, 91))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("ed.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.title))
        self.label_2.setText(_translate("MainWindow", self.date))
        self.pushButton_2.setText(_translate("MainWindow", "Quit"))
        self.label.setText(_translate("MainWindow", "Awesome SMS"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.pushButton.setText(_translate("MainWindow", "Login"))

    def quit(self):
        sys.exit(app.exec_())

    def init_root(self):
        user = 'rick'
        pas = 'pas'
        if True:
            MainWindow.destroy()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Root()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            print("ERROR")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        