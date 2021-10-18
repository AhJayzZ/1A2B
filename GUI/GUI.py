
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from GUI.Ui_1A2B_GUI import *
import sys,pygame
import Game_1A2B

class MainWindow(QtWidgets.QMainWindow,Ui_GameGUI):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('1A2B Game v1.0')
        self.setWindowIcon(QtGui.QIcon('GUI/image/app_icon.png'))
        self.MsgBox = QtWidgets.QMessageBox()
        self.MsgBox.setWindowTitle('訊息')

        # Global setting
        self.answer_label.setStyleSheet("Color:Red")
        self.confirm_btn.setDefault(True)
        self.answer_label.setHidden(True)
        self.bgm_checkbox.setChecked(True)
        self.input_textbox.setMaxLength(4)
        self.get_focus()
        self.playBGM()

        # button trigger
        self.exit_btn.clicked.connect(sys.exit)
        self.confirm_btn.clicked.connect(self.confirm_btn_click)
        self.reset_btn.clicked.connect(self.reset_btn_click)
        self.answer_checkbox.clicked.connect(self.show_answer_checkbox_click)
        self.bgm_checkbox.clicked.connect(self.playBGM)

        # BGM setting
        pygame.mixer.init()
        pygame.mixer.music.load('GUI/bgm/bgm_1A2B.mp3')
        pygame.mixer.music.play(-1,0,0)
        pygame.mixer.music.set_volume(0.5)

        #Game object
        self.Game = Game_1A2B.Game()
        self.guessCount = 0
      
    
    def confirm_btn_click(self):
        self.guessNum = self.input_textbox.text()
        self.input_textbox.clear()
        self.get_focus()
        self.statusCode = self.Game.start(self.guessNum)
        self.A , self.B = str(self.Game.A) , str(self.Game.B)

        if self.statusCode == -1:
            self.MsgBox.setWindowIcon(QtGui.QIcon('GUI/image/error_icon.png'))
            self.MsgBox.setText('請輸入四位數字!')
            self.MsgBox.exec()
        else :
            self.guessCount = self.guessCount + 1
            self.result_label.setText(self.A + 'A' + self.B + 'B')
            self.log_list.addItem(str(self.guessCount) + ',' + self.guessNum + ',' + self.A + 'A' + self.B + 'B')
            if self.statusCode == 1:
                self.MsgBox.setWindowIcon(QtGui.QIcon('GUI/image/correct_icon.png'))
                self.MsgBox.setText('恭喜你猜對了!')
                self.result_label.setText('4A0B')
                self.MsgBox.exec()


    def show_answer_checkbox_click(self):
        if self.answer_checkbox.isChecked():
            self.answer_label.setHidden(False)
            self.answer_label.setText(self.Game.returnAnswer())
        else :
            self.answer_label.setHidden(True)

    def reset_btn_click(self):
        self.Game.reset()
        self.Game.returnAnswer()
        self.get_focus()
        self.guessCount = 0
        self.result_label.setText('0A0B')
        self.answer_label.setHidden(True)
        self.answer_checkbox.setChecked(False)
        self.input_textbox.clear()
        self.log_list.clear()
        
    def get_focus(self):
        self.input_textbox.setFocus()
        self.confirm_btn.setFocus()

    def playBGM(self):
        pygame.mixer.init()
        if self.bgm_checkbox.isChecked():
            pygame.mixer.music.unpause()
        else :
            pygame.mixer.music.pause()
        
