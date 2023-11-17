import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect, QPoint, QSize
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from UI import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        self.pushButton.move(70, 150)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        for i in range(25):
            r, g, b = random.randrange(256), random.randrange(256), random.randrange(256)
            qp.setBrush(QColor(r, g, b))
            x, y = random.randrange(300), random.randrange(300)
            dx = dy = random.randint(20, 50)
            qp.drawEllipse(QRect(QPoint(x, y), QSize(dx, dy)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
