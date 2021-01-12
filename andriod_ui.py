# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(374, 279)
        self.tabWidget = QtWidgets.QTabWidget(Frame)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 341, 161))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_log = QtWidgets.QWidget()
        self.tab_log.setObjectName("tab_log")
        self.row_trunk = QtWidgets.QPushButton(self.tab_log)
        self.row_trunk.setGeometry(QtCore.QRect(10, 10, 71, 31))
        self.row_trunk.setObjectName("row_trunk")
        self.row_release = QtWidgets.QPushButton(self.tab_log)
        self.row_release.setGeometry(QtCore.QRect(90, 10, 71, 31))
        self.row_release.setObjectName("row_release")
        self.cn = QtWidgets.QPushButton(self.tab_log)
        self.cn.setGeometry(QtCore.QRect(170, 10, 71, 31))
        self.cn.setObjectName("cn")
        self.pub = QtWidgets.QPushButton(self.tab_log)
        self.pub.setGeometry(QtCore.QRect(250, 10, 71, 31))
        self.pub.setObjectName("pub")
        self.tips1 = QtWidgets.QTextBrowser(self.tab_log)
        self.tips1.setGeometry(QtCore.QRect(10, 50, 311, 81))
        self.tips1.setObjectName("tips1")
        self.tabWidget.addTab(self.tab_log, "")
        self.tab_pic = QtWidgets.QWidget()
        self.tab_pic.setObjectName("tab_pic")
        self.dcim_pic = QtWidgets.QPushButton(self.tab_pic)
        self.dcim_pic.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.dcim_pic.setObjectName("dcim_pic")
        self.default_pic = QtWidgets.QPushButton(self.tab_pic)
        self.default_pic.setGeometry(QtCore.QRect(10, 60, 101, 41))
        self.default_pic.setObjectName("default_pic")
        self.xup_record = QtWidgets.QPushButton(self.tab_pic)
        self.xup_record.setGeometry(QtCore.QRect(130, 10, 101, 41))
        self.xup_record.setObjectName("xup_record")
        self.dcim_record = QtWidgets.QPushButton(self.tab_pic)
        self.dcim_record.setGeometry(QtCore.QRect(130, 60, 101, 41))
        self.dcim_record.setObjectName("dcim_record")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_pic)
        self.lineEdit.setGeometry(QtCore.QRect(240, 100, 91, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.tab_pic)
        self.label.setGeometry(QtCore.QRect(10, 100, 181, 31))
        self.label.setObjectName("label")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_pic)
        self.textBrowser_3.setGeometry(QtCore.QRect(240, 10, 91, 81))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.tab_pic, "")
        self.textBrowser = QtWidgets.QTextBrowser(Frame)
        self.textBrowser.setGeometry(QtCore.QRect(20, 190, 341, 81))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Frame)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "日志截图提取工具"))
        self.row_trunk.setText(_translate("Frame", "row主干"))
        self.row_release.setText(_translate("Frame", "row分支"))
        self.cn.setText(_translate("Frame", "CN"))
        self.pub.setText(_translate("Frame", "正式环境"))
        self.tips1.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">点击按钮确认要提取的日志。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">会自动压缩，会自动删除电脑上旧的日志文件。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">正式环境为pre、pub包</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_log), _translate("Frame", "日志文件"))
        self.dcim_pic.setText(_translate("Frame", "DCIM路径图片"))
        self.default_pic.setText(_translate("Frame", "picture路径图片"))
        self.xup_record.setText(_translate("Frame", "XUP视频"))
        self.dcim_record.setText(_translate("Frame", "手机默认视频"))
        self.label.setText(_translate("Frame", "            请输入数字"))
        self.textBrowser_3.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">输入想提取的</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">最近生成的截</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">图或录屏数量</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pic), _translate("Frame", "截图视频"))
