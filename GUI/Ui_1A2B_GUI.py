# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\AhJayzZ\Desktop\NTUST Assignment\Project\SideProject\1A2B\GUI\1A2B_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameGUI(object):
    def setupUi(self, GameGUI):
        GameGUI.setObjectName("GameGUI")
        GameGUI.resize(478, 291)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        GameGUI.setFont(font)
        self.result_label = QtWidgets.QLabel(GameGUI)
        self.result_label.setGeometry(QtCore.QRect(20, 20, 151, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.result_label.setFont(font)
        self.result_label.setObjectName("result_label")
        self.exit_btn = QtWidgets.QPushButton(GameGUI)
        self.exit_btn.setGeometry(QtCore.QRect(160, 240, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        self.confirm_btn = QtWidgets.QPushButton(GameGUI)
        self.confirm_btn.setGeometry(QtCore.QRect(10, 140, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_btn.setFont(font)
        self.confirm_btn.setObjectName("confirm_btn")
        self.log_list = QtWidgets.QListWidget(GameGUI)
        self.log_list.setGeometry(QtCore.QRect(300, 40, 171, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.log_list.setFont(font)
        self.log_list.setObjectName("log_list")
        self.answer_label = QtWidgets.QLabel(GameGUI)
        self.answer_label.setEnabled(True)
        self.answer_label.setGeometry(QtCore.QRect(20, 190, 221, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.answer_label.setFont(font)
        self.answer_label.setObjectName("answer_label")
        self.reset_btn = QtWidgets.QPushButton(GameGUI)
        self.reset_btn.setGeometry(QtCore.QRect(10, 240, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.answer_checkbox = QtWidgets.QCheckBox(GameGUI)
        self.answer_checkbox.setGeometry(QtCore.QRect(180, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.answer_checkbox.setFont(font)
        self.answer_checkbox.setObjectName("answer_checkbox")
        self.log_label = QtWidgets.QLabel(GameGUI)
        self.log_label.setGeometry(QtCore.QRect(290, 0, 61, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.log_label.setFont(font)
        self.log_label.setObjectName("log_label")
        self.input_textbox = QtWidgets.QLineEdit(GameGUI)
        self.input_textbox.setGeometry(QtCore.QRect(10, 90, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_textbox.setFont(font)
        self.input_textbox.setObjectName("input_textbox")

        self.retranslateUi(GameGUI)
        QtCore.QMetaObject.connectSlotsByName(GameGUI)

    def retranslateUi(self, GameGUI):
        _translate = QtCore.QCoreApplication.translate
        GameGUI.setWindowTitle(_translate("GameGUI", "Dialog"))
        self.result_label.setText(_translate("GameGUI", "0A0B"))
        self.exit_btn.setText(_translate("GameGUI", "離開"))
        self.confirm_btn.setText(_translate("GameGUI", "確定"))
        self.answer_label.setText(_translate("GameGUI", "答案:"))
        self.reset_btn.setText(_translate("GameGUI", "重置"))
        self.answer_checkbox.setText(_translate("GameGUI", "顯示答案"))
        self.log_label.setText(_translate("GameGUI", "紀錄:"))
