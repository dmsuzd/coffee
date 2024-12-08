import sys
import sqlite3
from PyQt6 import QtWidgets
from PyQt6 import uic


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.load_data()

    def load_data(self):
        conn = sqlite3.connect("database.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee")
        coffees = cursor.fetchall()
        for coffee in coffees:
            self.listWidget.addItem(f"ID: {coffee[0]}, Name: {coffee[1]}, Roast: {coffee[2]}, Type: "
                                    f"{coffee[3]}, Flavor: {coffee[4]}, Price: {coffee[5]}, Volume: {coffee[6]}")
        conn.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
