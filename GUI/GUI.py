import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from GUI.Ui_1A2B_GUI import *
import Game_1A2B

class MainWindow(QtWidgets.QMainWindow,Ui_GameGUI):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('1A2B Game v1.0')
        self.MsgBox = QtWidgets.QMessageBox()
        self.MsgBox.setWindowTitle('訊息')

        # Checkbox setting
        self.answer_label.setStyleSheet("Color:Red")
        self.answer_label.setHidden(True)
        self.input_textbox.setMaxLength(4)
        self.input_textbox.setFocus()

        # button trigger
        self.exit_btn.clicked.connect(sys.exit)
        self.confirm_btn.clicked.connect(self.confirm_btn_click)
        self.reset_btn.clicked.connect(self.reset_btn_click)
        self.answer_checkbox.clicked.connect(self.show_answer_checkbox_click)
    
    def confirm_btn_click(self):
        self.guessNum = self.input_textbox.text()
        self.input_textbox.clear()
        self.A,self.B,self.statusCode = Game_1A2B.Game(self.guessNum)
        if self.statusCode == -1:
            self.MsgBox.setText('請輸入四位數字')
            self.MsgBox.exec()
        elif self.statusCode == 1:
            self.MsgBox.setText('恭喜你猜對了!')
            self.result_label.setText('4A0B')
            self.MsgBox.exec()
            self.reset_btn_click()
        else :
            self.result_label.setText(str(self.A)+'A'+str(self.B)+'B')

    def show_answer_checkbox_click(self):
        if self.answer_checkbox.isChecked():
            self.answer_label.setHidden(False)
            self.answer_label.setText(Game_1A2B.returnAnswer())
        else :
            self.answer_label.setHidden(True)

    def reset_btn_click(self):
        Game_1A2B.reset()
        self.result_label.setText('0A0B')
        self.input_textbox.clear()
        self.input_textbox.setFocus()
        self.log_list.clear()

    
        



