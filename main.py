# from pathlib import Path 
import sys
from frontend.calculator_ui import Calculator_ui
from PySide6.QtWidgets import QApplication, QWidget
# from PySide6 import QtWidgets
import backend

class Calculator(QWidget, Calculator_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        backend.Actions()
        self.setWindowTitle("Calculator ni Vougeart")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
