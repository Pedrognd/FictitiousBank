import typing
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import sys

class Ui_Form(object):
    def __init__(self):
        self.Mode = 'off'
        self.Color01 = 'background-color: #1a52bf'
        self.Color02 = 'background-color: #f47f16'
        self.Color03 = 'background-color: #ccc4cf'

    def setupUi(self, Form):

        #### DEFAULT ####
        Form.setObjectName('LoginScreen')
        Form.resize(360, 450)
        Form.setStyleSheet(self.Color01)
        Form.setWindowFlag(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)

        #### FRAMES ####
        self.MainFrame = QFrame(Form)
        self.MainFrame.setObjectName('MainFrame')
        self.MainFrame.setStyleSheet('border-radius:25px;')

        self.AccountDataFrame = QFrame(self.MainFrame)
        self.AccountDataFrame.setObjectName('AccountDataFrame')
        self.AccountDataFrame.setMaximumHeight(200)
        self.AccountDataFrame.setMinimumHeight(200)

        self.FuncFrame = QFrame(self.MainFrame)
        self.FuncFrame.setObjectName('FuncFrame')
        self.FuncFrame.setStyleSheet(self.Color03)

        #### ACCOUNTDATAFRAME ####
        self.HeaderFrame = QFrame(self.AccountDataFrame)
        self.HeaderFrame.setObjectName('HeaderFrame')
        self.HeaderFrame.setMaximumHeight(50)

        self.HeaderLabel = QLabel(self.HeaderFrame)
        self.HeaderLabel.setObjectName('HeaderLabel')
        self.HeaderLabel.setStyleSheet(f"font: 15pt \"Agency FB\" ;color: #ccc4cf")
        self.HeaderLabel.setText('Central Bank')
        self.HeaderLabel.setAlignment(Qt.AlignCenter)

        self.TitleFrame = QFrame(self.AccountDataFrame)
        self.TitleFrame.setObjectName('TitleFrame')
        self.TitleFrame.setMaximumHeight(50)
        self.TitleFrame.setStyleSheet(self.Color03)

        self.TitleLabelFrame = QFrame(self.TitleFrame)
        self.TitleLabelFrame.setObjectName('TitleLabelFrame')
        self.TitleLabelFrame.setMaximumHeight(50)
        
        self.TitleLabel = QLabel(self.TitleLabelFrame)
        self.TitleLabel.setObjectName('TitleLabel')
        self.TitleLabel.setStyleSheet(f'font: 12pt \'Agency FB\'; color: #ccc4cf')
        self.TitleLabel.setText('Olá, Fulano de Tal')
        self.TitleLabel.setAlignment(Qt.AlignCenter)

        self.AccountFrame = QFrame(self.AccountDataFrame)
        self.AccountFrame.setObjectName('AccountFrame')
        self.AccountFrame.setStyleSheet(self.Color02)

        #### LAYOUT'S ####
        self.VerticalLayout = QVBoxLayout(Form)
        self.VerticalLayout.setObjectName("VerticalLayout")
        self.VerticalLayout.setContentsMargins(0,0,0,0)
        self.VerticalLayout.setSpacing(0)

        self.VerticalLayout02 = QVBoxLayout(self.MainFrame)
        self.VerticalLayout02.setObjectName('VerticalLayout02')
        self.VerticalLayout02.setContentsMargins(0,0,0,0)
        self.VerticalLayout02.setSpacing(0)

        self.VerticalLayout03 = QVBoxLayout(self.AccountDataFrame)
        self.VerticalLayout03.setObjectName('VerticalLayout03')
        self.VerticalLayout03.setContentsMargins(0,0,0,0)
        self.VerticalLayout03.setSpacing(0)

        self.HorizontalLayout = QHBoxLayout(self.HeaderFrame)
        self.HorizontalLayout.setObjectName('HorizontalLayout')
        self.HorizontalLayout.setContentsMargins(0,0,0,0)
        self.HorizontalLayout.setSpacing(0)
        
        #### SEPARATOR'S ####
        self.SeparatorHorizontal = QSpacerItem(40,50,QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.SeparatorVertical = QSpacerItem(40,50, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        #### ADD ITENS TO LAYOUT'S ####
        self.VerticalLayout.addWidget(self.MainFrame)
        self.VerticalLayout02.addWidget(self.AccountDataFrame)
        self.VerticalLayout02.addWidget(self.FuncFrame)
        self.VerticalLayout03.addWidget(self.HeaderFrame)
        self.VerticalLayout03.addWidget(self.TitleFrame)
        self.VerticalLayout03.addWidget(self.AccountFrame)
        self.HorizontalLayout.addWidget(self.HeaderLabel)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate('LoginScreen', 'LoginScreen'))

    def ExitFunc(self):
        Form.close()

    def ReturnFunc(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())