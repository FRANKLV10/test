

from testtools.mvp_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui,QtWidgets
import sys
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
import os

class Stream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))
class ControlBoard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ControlBoard, self).__init__()
        self.setupUi(self)
        # 下面将输出重定向到textBrowser中
        sys.stdout = Stream(textWritten=self.outputWritten)
        sys.stderr = Stream(textWritten=self.outputWritten)

        # 有按钮的话，下面的就不要注释掉
        # self.pushButton.clicked.connect(self.bClicked)

        self.file.clicked.connect(self.msg)
        self.start.clicked.connect(self.mvp)


    def retranslateUi(self, MainWindow):
         _translate = QtCore.QCoreApplication.translate
         MainWindow.setWindowTitle(_translate("MainWindow", "MVP分数计算器"))
         self.start.setText(_translate("MainWindow", "开始计算"))
         self.file.setText(_translate("MainWindow", "选择文件"))
         self.fileT.setText(_translate("MainWindow", ''))



    def outputWritten(self, text):
        cursor = self.output.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.output.setTextCursor(cursor)
        self.output.ensureCursorVisible()


    def msg(self):
        path = os.getcwd()

        file_path =  QtWidgets.QFileDialog.getOpenFileName(None, "请选择要添加的文件", path, "Text Files (*.xls)")# 起始路径

        self.fileT.setText(file_path[0])

    def mvp(self):
            print("计算中")
            print("-------------------")
            print("计算完成")

if __name__ == '__main__':
    app = QApplication(sys.argv)





    win = ControlBoard()
    win.show()
    sys.exit(app.exec_())