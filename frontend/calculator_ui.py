# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Calculator_ui(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(398, 688)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(380, 670))
        self.frame.setMaximumSize(QSize(380, 670))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.display_label = QLabel(self.frame)
        self.display_label.setObjectName(u"display_label")
        self.display_label.setMinimumSize(QSize(271, 121))
        self.display_label.setMaximumSize(QSize(16777215, 121))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(36)
        font.setBold(True)
        self.display_label.setFont(font)
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.display_label, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(360, 520))
        self.widget_2.setMaximumSize(QSize(360, 520))
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.equal_button = QPushButton(self.widget_2)
        self.equal_button.setObjectName(u"equal_button")
        self.equal_button.setMinimumSize(QSize(81, 70))
        self.equal_button.setMaximumSize(QSize(81, 70))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.equal_button.setFont(font1)

        self.gridLayout.addWidget(self.equal_button, 5, 3, 1, 1)

        self.point_button = QPushButton(self.widget_2)
        self.point_button.setObjectName(u"point_button")
        self.point_button.setMinimumSize(QSize(81, 70))
        self.point_button.setMaximumSize(QSize(81, 70))
        self.point_button.setFont(font1)

        self.gridLayout.addWidget(self.point_button, 5, 2, 1, 1)

        self.one_button = QPushButton(self.widget_2)
        self.one_button.setObjectName(u"one_button")
        self.one_button.setMinimumSize(QSize(81, 70))
        self.one_button.setMaximumSize(QSize(81, 70))
        self.one_button.setFont(font1)

        self.gridLayout.addWidget(self.one_button, 4, 0, 1, 1)

        self.backspace_button = QPushButton(self.widget_2)
        self.backspace_button.setObjectName(u"backspace_button")
        self.backspace_button.setMinimumSize(QSize(81, 70))
        self.backspace_button.setMaximumSize(QSize(81, 70))
        self.backspace_button.setFont(font1)

        self.gridLayout.addWidget(self.backspace_button, 0, 3, 1, 1)

        self.five_button = QPushButton(self.widget_2)
        self.five_button.setObjectName(u"five_button")
        self.five_button.setMinimumSize(QSize(81, 70))
        self.five_button.setMaximumSize(QSize(81, 70))
        self.five_button.setFont(font1)

        self.gridLayout.addWidget(self.five_button, 3, 1, 1, 1)

        self.pushButton_21 = QPushButton(self.widget_2)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(81, 70))
        self.pushButton_21.setMaximumSize(QSize(81, 70))
        self.pushButton_21.setFont(font1)

        self.gridLayout.addWidget(self.pushButton_21, 5, 0, 1, 1)

        self.two_button = QPushButton(self.widget_2)
        self.two_button.setObjectName(u"two_button")
        self.two_button.setMinimumSize(QSize(81, 70))
        self.two_button.setMaximumSize(QSize(81, 70))
        self.two_button.setFont(font1)

        self.gridLayout.addWidget(self.two_button, 4, 1, 1, 1)

        self.percent_button = QPushButton(self.widget_2)
        self.percent_button.setObjectName(u"percent_button")
        self.percent_button.setMinimumSize(QSize(81, 70))
        self.percent_button.setMaximumSize(QSize(81, 70))
        self.percent_button.setFont(font1)

        self.gridLayout.addWidget(self.percent_button, 0, 0, 1, 1)

        self.zero_button = QPushButton(self.widget_2)
        self.zero_button.setObjectName(u"zero_button")
        self.zero_button.setMinimumSize(QSize(81, 70))
        self.zero_button.setMaximumSize(QSize(81, 70))
        self.zero_button.setFont(font1)

        self.gridLayout.addWidget(self.zero_button, 5, 1, 1, 1)

        self.seven_button = QPushButton(self.widget_2)
        self.seven_button.setObjectName(u"seven_button")
        self.seven_button.setMinimumSize(QSize(81, 70))
        self.seven_button.setMaximumSize(QSize(81, 70))
        self.seven_button.setFont(font1)

        self.gridLayout.addWidget(self.seven_button, 2, 0, 1, 1)

        self.clear_button = QPushButton(self.widget_2)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setMinimumSize(QSize(81, 70))
        self.clear_button.setMaximumSize(QSize(81, 70))
        self.clear_button.setFont(font1)

        self.gridLayout.addWidget(self.clear_button, 0, 2, 1, 1)

        self.addition_button = QPushButton(self.widget_2)
        self.addition_button.setObjectName(u"addition_button")
        self.addition_button.setMinimumSize(QSize(81, 70))
        self.addition_button.setMaximumSize(QSize(81, 70))
        self.addition_button.setFont(font1)

        self.gridLayout.addWidget(self.addition_button, 4, 3, 1, 1)

        self.eight_button = QPushButton(self.widget_2)
        self.eight_button.setObjectName(u"eight_button")
        self.eight_button.setMinimumSize(QSize(81, 70))
        self.eight_button.setMaximumSize(QSize(81, 70))
        self.eight_button.setFont(font1)

        self.gridLayout.addWidget(self.eight_button, 2, 1, 1, 1)

        self.subraction_button = QPushButton(self.widget_2)
        self.subraction_button.setObjectName(u"subraction_button")
        self.subraction_button.setMinimumSize(QSize(81, 70))
        self.subraction_button.setMaximumSize(QSize(81, 70))
        self.subraction_button.setFont(font1)

        self.gridLayout.addWidget(self.subraction_button, 3, 3, 1, 1)

        self.three_button = QPushButton(self.widget_2)
        self.three_button.setObjectName(u"three_button")
        self.three_button.setMinimumSize(QSize(81, 70))
        self.three_button.setMaximumSize(QSize(81, 70))
        self.three_button.setFont(font1)

        self.gridLayout.addWidget(self.three_button, 4, 2, 1, 1)

        self.nine_button = QPushButton(self.widget_2)
        self.nine_button.setObjectName(u"nine_button")
        self.nine_button.setMinimumSize(QSize(81, 70))
        self.nine_button.setMaximumSize(QSize(81, 70))
        self.nine_button.setFont(font1)

        self.gridLayout.addWidget(self.nine_button, 2, 2, 1, 1)

        self.four_button = QPushButton(self.widget_2)
        self.four_button.setObjectName(u"four_button")
        self.four_button.setMinimumSize(QSize(81, 70))
        self.four_button.setMaximumSize(QSize(81, 70))
        self.four_button.setFont(font1)

        self.gridLayout.addWidget(self.four_button, 3, 0, 1, 1)

        self.multiplication_button = QPushButton(self.widget_2)
        self.multiplication_button.setObjectName(u"multiplication_button")
        self.multiplication_button.setMinimumSize(QSize(81, 70))
        self.multiplication_button.setMaximumSize(QSize(81, 70))
        self.multiplication_button.setFont(font1)

        self.gridLayout.addWidget(self.multiplication_button, 2, 3, 1, 1)

        self.clearEntry_button = QPushButton(self.widget_2)
        self.clearEntry_button.setObjectName(u"clearEntry_button")
        self.clearEntry_button.setMinimumSize(QSize(81, 70))
        self.clearEntry_button.setMaximumSize(QSize(81, 70))
        self.clearEntry_button.setFont(font1)

        self.gridLayout.addWidget(self.clearEntry_button, 0, 1, 1, 1)

        self.six_button = QPushButton(self.widget_2)
        self.six_button.setObjectName(u"six_button")
        self.six_button.setMinimumSize(QSize(81, 70))
        self.six_button.setMaximumSize(QSize(81, 70))
        self.six_button.setFont(font1)

        self.gridLayout.addWidget(self.six_button, 3, 2, 1, 1)

        self.reciprocal_button = QPushButton(self.widget_2)
        self.reciprocal_button.setObjectName(u"reciprocal_button")
        self.reciprocal_button.setMinimumSize(QSize(81, 70))
        self.reciprocal_button.setMaximumSize(QSize(81, 70))
        self.reciprocal_button.setFont(font1)

        self.gridLayout.addWidget(self.reciprocal_button, 1, 0, 1, 1)

        self.exponential_button = QPushButton(self.widget_2)
        self.exponential_button.setObjectName(u"exponential_button")
        self.exponential_button.setMinimumSize(QSize(81, 70))
        self.exponential_button.setMaximumSize(QSize(81, 70))
        self.exponential_button.setFont(font1)

        self.gridLayout.addWidget(self.exponential_button, 1, 1, 1, 1)

        self.squareRoot_button = QPushButton(self.widget_2)
        self.squareRoot_button.setObjectName(u"squareRoot_button")
        self.squareRoot_button.setMinimumSize(QSize(81, 70))
        self.squareRoot_button.setMaximumSize(QSize(81, 70))
        self.squareRoot_button.setFont(font1)

        self.gridLayout.addWidget(self.squareRoot_button, 1, 2, 1, 1)

        self.division_button = QPushButton(self.widget_2)
        self.division_button.setObjectName(u"division_button")
        self.division_button.setMinimumSize(QSize(81, 70))
        self.division_button.setMaximumSize(QSize(81, 70))
        self.division_button.setFont(font1)

        self.gridLayout.addWidget(self.division_button, 1, 3, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.display_label.setText("")
        self.equal_button.setText(QCoreApplication.translate("Form", u"=", None))
        self.point_button.setText(QCoreApplication.translate("Form", u".", None))
        self.one_button.setText(QCoreApplication.translate("Form", u"1", None))
        self.backspace_button.setText(QCoreApplication.translate("Form", u"<<", None))
        self.five_button.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_21.setText(QCoreApplication.translate("Form", u"+/-", None))
        self.two_button.setText(QCoreApplication.translate("Form", u"2", None))
        self.percent_button.setText(QCoreApplication.translate("Form", u"%", None))
        self.zero_button.setText(QCoreApplication.translate("Form", u"0", None))
        self.seven_button.setText(QCoreApplication.translate("Form", u"7", None))
        self.clear_button.setText(QCoreApplication.translate("Form", u"C", None))
        self.addition_button.setText(QCoreApplication.translate("Form", u"+", None))
        self.eight_button.setText(QCoreApplication.translate("Form", u"8", None))
        self.subraction_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.three_button.setText(QCoreApplication.translate("Form", u"3", None))
        self.nine_button.setText(QCoreApplication.translate("Form", u"9", None))
        self.four_button.setText(QCoreApplication.translate("Form", u"4", None))
        self.multiplication_button.setText(QCoreApplication.translate("Form", u"*", None))
        self.clearEntry_button.setText(QCoreApplication.translate("Form", u"CE", None))
        self.six_button.setText(QCoreApplication.translate("Form", u"6", None))
        self.reciprocal_button.setText(QCoreApplication.translate("Form", u"1/x", None))
        self.exponential_button.setText(QCoreApplication.translate("Form", u"x2", None))
        self.squareRoot_button.setText(QCoreApplication.translate("Form", u"2\u221ax", None))
        self.division_button.setText(QCoreApplication.translate("Form", u"/", None))
    # retranslateUi

