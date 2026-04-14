import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from frontend.calculator_ui import Calculator_ui

current_number = []

class Actions(Calculator_ui, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listing()

    def listing(self):    
        number_button = {
            1:self.one_button,
            2:self.two_button,
            3:self.three_button,
            4:self.four_button,
            5:self.five_button,
            6:self.six_button,
            7:self.seven_button,
            8:self.eight_button,
            9:self.nine_button,
            0:self.zero_button,
            '+':self.addition_button,
            '-':self.subraction_button,
            '/':self.division_button,
            '*':self.multiplication_button,
            '%':self.percent_button
        }

        disable_operator = ['+', '*', '/', '%']

        if current_number == 0:
            for i in disable_operator:
                number_button[i].setEnabled(False)

        for values in number_button.values():
            values.clicked.connect(self.handle_digit)

    def handle_digit(self):

        
        clicked_button = self.sender()
        
        print(type(clicked_button))
        new_digit = clicked_button.text()

        

        # current_number.append(int(new_digit))
        current_number.append(new_digit)
        current_text = self.display_label.text()
        if not len(current_text) == 13:
            self.display_label.setText(current_text + new_digit)
        print(current_number)

    def handle_operator(self):
        operations = ['+', '-', '*', '/', '%']


        