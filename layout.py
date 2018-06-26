import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMessageBox,
                             QHBoxLayout, QVBoxLayout)
# from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("ok")
        cancelButton = QPushButton("cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle("Button")
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex =Exam()
    sys.exit(app.exec_())
