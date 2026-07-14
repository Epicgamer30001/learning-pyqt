from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow

import sys

di = 5


#one Qapplication instance per app
app = QApplication(sys.argv)

window = QWidget()   #Qt widget
window.show()   #widgets are hidden by defult

window2 = QPushButton("Push Me")
window2.show()

window3 = QMainWindow()
window3.show()

app.exec()


