import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('노창균',self)
        btn.resize(btn.sizeHint()) # 글씨를 기준으로 적당하게 크기 조정
        btn.setToolTip('툴팁입니다.<b>안녕하세요<b/>') #태그도 가능함
        btn.move(20,30) #버튼 위치

        self.setGeometry(300,300,400,500) #전체창 크기
        self.setWindowTitle('첫번째 학습') # 윈도우 타이틀
        self.show()


app = QApplication(sys.argv)

W = Exam()
sys.exit(app.exec_())
