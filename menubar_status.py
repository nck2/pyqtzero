import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication
class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar() #상태창 생성
        self.statusBar().showMessage("안녕하세요") #상태표시줄 글자 쓰기

        menu = self.menuBar()               # 메뉴생성
        menu_file = menu.addMenu('File')    # 그릅생생
        menu_edif = menu.addMenu('Edit')    # 그룹생성

        file_exit = QAction('EXIT',self)    # 메뉴객체생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("누르면 꺼짐")
        new_txt = QAction("텍스트파일",self)
        new_py = QAction("python파일",self)

        file_exit.triggered.connect(QCoreApplication.instance().quit)

        file_new = QMenu("New", self) # 서브그룹 생성

        file_new.addAction(new_txt)     #서브메뉴 등록
        file_new.addAction(new_py)

        menu_file.addMenu(file_new) # 메뉴 등록
        menu_file.addAction(file_exit) # 메뉴 등록

        self.resize(450,450)
        self.show()

app = QApplication(sys.argv)
w =Exam()
sys.exit(app.exec_())
