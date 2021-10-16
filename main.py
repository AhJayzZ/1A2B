
import Game_1A2B
from GUI.GUI import *
import sys

if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())