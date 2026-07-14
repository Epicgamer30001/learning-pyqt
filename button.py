import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.button_is_checked = True   #initial state

        self.setWindowTitle("My App")
        
        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)        #light switch = True 
        self.button.clicked.connect(self.button_cb)  #define callback
 
        self.button.setChecked(self.button_is_checked)   #set inital state 

        self.setCentralWidget(self.button)        

    def button_cb(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)
"""
    def button_cb(self,checked):
        self.button_is_checked = checked

        print(self.button_is_checked)"""
    
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()