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

        # Checkbox setting
        self.answer_label.setHidden(True)
        self.input_textbox.setFocus()

        # button trigger
        self.exit_btn.clicked.connect(sys.exit)
        self.reset_btn.clicked.connect(self.reset_btn_click)
        self.answer_checkbox.clicked.connect(self.show_answer_checkbox_click)
    
    def show_answer_checkbox_click(self):
        if self.answer_checkbox.isChecked():
            self.answer_label.setHidden(False)
            self.answer_label.setText('答案:')
        else :
            self.answer_label.setHidden(True)

    def reset_btn_click(self):
        self.result_label.setText('0A0B')
        self.input_textbox.clear()
        self.input_textbox.setFocus()
        self.log_list.clear()

    
        



