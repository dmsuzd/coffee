import sys
import random
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor


class CircleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 362, 494)
        self.setWindowTitle("Circle Drawer")
        self.pushButton = QtWidgets.QPushButton("Add Circle", self)
        self.pushButton.setGeometry(40, 390, 271, 41)
        self.pushButton.clicked.connect(self.add_circle)

        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(circle[3])
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleApp()
    window.show()
    sys.exit(app.exec())
