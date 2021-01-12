from andriod_ui import Ui_Frame
from PyQt5 import QtWidgets, QtGui,QtCore

import sys
class Stream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))

class mywindow(QtWidgets.QWidget,Ui_Frame):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

    def outputWritten(self, text):
        cursor = self.output.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()
    def
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = mywindow()
    win.show()
    sys.exit(app.exec_())