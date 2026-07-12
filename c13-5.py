import sys

from PyQt5.QtWidgets import (QMainWindow,QApplication,
                             QPushButton,QLabel)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.button=QPushButton("Click me!",self)
        self.label=QLabel("Hello",self)
        self.initUI()
       

    def initUI(self):
        self.button.setGeometry(165,200,200,100)
        self.button.setStyleSheet("font-size:25px;"
                            "background-color:gray;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(170,300,200,100)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size:40px;")
        
    def on_click(self):
        self.label.setText("Goodbye!")


def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()