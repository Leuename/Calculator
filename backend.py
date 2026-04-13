import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from frontend.calculator_ui import Calculator_ui
from main import Calculator
class Actions(Calculator.window):
    def __init__(self):
        super().__init__()
        self.one_button.clicked.connect(self.one_button_action)
    
    def label(self):
        pass
    
    def one_button_action(self):
        label = self.display_label.setText("1")
    
    def two_button_action(self):
        pass
    
    def three_button_action(self):
        pass
    
    def four_button_action(self):
        pass
    
    def five_button_action(self):
        pass
    
    def six_button_action(self):
        pass
    
    def seven_button_action(self):
        pass
    
    def eight_button_action(self):
        pass
    
    def nine_button_action(self):
        pass
    
    def zero_button_action(self):
        pass
    
    def plus(self):
        pass
    
    def minus(self):
        pass
    
    def multiply(self):
        pass
    
    def divide(self):
        pass
    
    def percent(self):
        pass