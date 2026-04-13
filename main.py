# from pathlib import Path 
import sys
from frontend.calculator_ui import Calculator_ui
from PySide6.QtWidgets import QApplication, QWidget
# from PySide6 import QtWidgets
from backend import Actions


app = QApplication(sys.argv)
window = Actions()
window.show()
sys.exit(app.exec())
