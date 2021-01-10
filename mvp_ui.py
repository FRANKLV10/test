import sys

from PyQt5 import QtCore, QtWidgets
class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        # 主窗口参数设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 设置按键参数
        self.file = QtWidgets.QPushButton(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(10, 270, 120, 30))
        self.file.setObjectName("file")
        self.file.setStyleSheet(" margin: 0px; padding: 0px;" )
        self.file.setStyleSheet(
            "QPushButton{ margin: 0px; padding: 0px;"  "QPushButton:hover{color:green}"  # 光标移动到上面后的前景色
                                                        "QPushButton{border-radius:6px}"  # 圆角半径
                                                        "QPushButton:pressed{border: None;}"  # 按下时的样式
        )
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(10, 30, 120,220))
        self.start.setObjectName("file")
        self.start.setStyleSheet(" margin: 0px; padding: 0px;")
        self.start.setStyleSheet(
            "QPushButton{ margin: 0px; padding: 0px;"  "QPushButton:hover{color:green}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{border: None;}"  # 按下时的样式
        )
        # 设置显示窗口参数
        self.output = QtWidgets.QTextBrowser(self.centralwidget)

        self.output.setGeometry(QtCore.QRect(150, 30, 340, 220))
        self.output.setObjectName("output")

        # 设置文件窗口参数
        self.fileT = QtWidgets.QPushButton(self.centralwidget)
        self.fileT.setGeometry(QtCore.QRect(150, 270, 340, 30))
        self.fileT.setObjectName("file")
        self.fileT.setStyleSheet(" margin: 0px; padding: 0px;" )
        self.fileT.setStyleSheet(
            "QPushButton{ margin: 0px; padding: 0px;"  "QPushButton:hover{color:white}"  # 光标移动到上面后的前景色
                                                        "QPushButton{border-radius:6px}"  # 圆角半径
                                                        "QPushButton:pressed{border: None;}"  # 按下时的样式
        )

        # 主窗口及菜单栏标题栏设置
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass
