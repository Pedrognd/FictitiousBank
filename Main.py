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
        # Form.setWindowFlag(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)

        #### FRAMES ####
        self.MainFrame = QFrame(Form)
        self.MainFrame.setObjectName('MainFrame')
        self.MainFrame.setStyleSheet('border-radius:25px;')

        self.AccountDataFrame = QFrame(self.MainFrame)
        self.AccountDataFrame.setObjectName('AccountDataFrame')
        self.AccountDataFrame.setMaximumHeight(200)
        self.AccountDataFrame.setMinimumHeight(200)
        # Back = QPixmap("Icons\Recortada.jpg")
        # self.AccountDataFrame.setStyleSheet(f'background-image: url({Back});')

        self.FuncFrame = QFrame(self.MainFrame)
        self.FuncFrame.setObjectName('FuncFrame')
        self.FuncFrame.setStyleSheet(self.Color03)

        #### ACCOUNTDATAFRAME ####
        self.HeaderFrame = QFrame(self.AccountDataFrame)
        self.HeaderFrame.setObjectName('HeaderFrame')
        self.HeaderFrame.setMaximumHeight(50)
        self.HeaderFrame.setStyleSheet('background-color: #1142a1; ')

        self.HeaderLabel = QLabel(self.HeaderFrame)
        self.HeaderLabel.setObjectName('HeaderLabel')
        self.HeaderLabel.setStyleSheet(f"font: 25pt \"Agency FB\" ;color: #ccc4cf")
        self.HeaderLabel.setText('Central Bank')
        self.HeaderLabel.setAlignment(Qt.AlignCenter)

        self.TitleFrame = QFrame(self.AccountDataFrame)
        self.TitleFrame.setObjectName('TitleFrame')
        self.TitleFrame.setMaximumHeight(50)

        # self.opacity_effect = QGraphicsOpacityEffect()
        # self.opacity_effect.setOpacity(0.3)
        # self.TitleFrame.setGraphicsEffect(self.opacity_effect)

        self.TitleLabelFrame = QFrame(self.TitleFrame)
        self.TitleLabelFrame.setObjectName('TitleLabelFrame')
        self.TitleLabelFrame.setMaximumHeight(50)
        
        self.TitleLabel = QLabel(self.TitleLabelFrame)
        self.TitleLabel.setObjectName('TitleLabel')
        self.TitleLabel.setStyleSheet(f'font: 15pt \'Agency FB\'; color: #ccc4cf;')
        self.TitleLabel.setText('Olá, João Victor')
        self.TitleLabel.setAlignment(Qt.AlignCenter)

        self.BtnFrame = QFrame(self.TitleFrame)
        self.BtnFrame.setObjectName('BtnFrame')
        self.BtnFrame.setMinimumSize(110,50)
        self.BtnFrame.setMaximumSize(110,50)

        self.BtnReturn = QPushButton(self.BtnFrame)
        self.BtnReturn.setObjectName("BtnReturn")
        self.BtnReturn.setMinimumSize(QSize(50, 50))
        self.BtnReturn.setMaximumSize(QSize(50, 50))
        self.BtnReturn.setCursor(QCursor(Qt.PointingHandCursor))
        self.BtnReturn.setText("")
        self.BtnReturn.setStyleSheet('border-radius:25px;')
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons\Btt_Return.png"), QIcon.Normal, QIcon.Off)
        self.BtnReturn.setIcon(icon)
        self.BtnReturn.setIconSize(QSize(50, 50))
        self.BtnReturn.setShortcut("")
        self.BtnReturn.setCheckable(True)
        self.BtnReturn.setFlat(True)
        # self.BtnReturn.clicked.connect(self.ExitFunc)

        self.BtnExit = QPushButton(self.BtnFrame)
        self.BtnExit.setObjectName("BtnExit")
        self.BtnExit.setMinimumSize(QSize(50, 50))
        self.BtnExit.setMaximumSize(QSize(50, 50))
        self.BtnExit.setCursor(QCursor(Qt.PointingHandCursor))
        self.BtnExit.setText("")
        self.BtnExit.setStyleSheet('border-radius:25px;')
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons\Btt_Exit.png"), QIcon.Normal, QIcon.Off)
        self.BtnExit.setIcon(icon)
        self.BtnExit.setIconSize(QSize(50, 50))
        self.BtnExit.setShortcut("")
        self.BtnExit.setCheckable(True)
        self.BtnExit.setFlat(True)
        # self.BtnExit.clicked.connect(self.ExitFunc)

        self.AccountFrame = QFrame(self.AccountDataFrame)
        self.AccountFrame.setObjectName('AccountFrame')

        self.BalanceFrame = QFrame(self.AccountFrame)
        self.BalanceFrame.setObjectName('BalanceFrame')
        self.BalanceFrame.setMaximumHeight(50)

        self.BalanceLabel01 = QLabel(self.AccountFrame)
        self.BalanceLabel01.setObjectName('BalanceLabel01')
        self.BalanceLabel01.setStyleSheet(f'font: 15pt \'Agency FB\'; color: #ccc4cf;')
        self.BalanceLabel01.setText('Saldo da Conta')
        self.BalanceLabel01.setAlignment(Qt.AlignCenter)

        self.BalanceLabel02 = QLabel(self.BalanceFrame)
        self.BalanceLabel02.setObjectName('BalanceLabel02')
        self.BalanceLabel02.setMaximumWidth(100)
        self.BalanceLabel02.setStyleSheet(f'font: 15pt \'Agency FB\'; color: #ccc4cf; background-color:#7c96c7; border-radius:10px;')
        self.BalanceLabel02.setText('R$ 1.999,99')
        self.BalanceLabel02.setAlignment(Qt.AlignCenter)

        self.AccountIdFrame = QFrame(self.AccountFrame)
        self.AccountIdFrame.setObjectName('AccountIdFrame')
        self.AccountIdFrame.setMaximumHeight(50)

        self.AccountIdLabel = QLabel(self.AccountIdFrame)
        self.AccountIdLabel.setObjectName('AccountIdLabel')
        self.AccountIdLabel.setStyleSheet(f'font: 15pt \'Agency FB\'; color: #ccc4cf;')
        self.AccountIdLabel.setText('6730806')
        self.AccountIdLabel.setAlignment(Qt.AlignCenter)

        #### FUNCFRAME ####
        self.BtnFuncFrame = QFrame(self.FuncFrame)

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

        self.VerticalLayout04 = QVBoxLayout(self.AccountFrame)
        self.VerticalLayout04.setObjectName('VerticalLayout04')
        self.VerticalLayout04.setContentsMargins(0,0,0,0)
        self.VerticalLayout04.setSpacing(0)
        
        self.VerticalLayout06 = QVBoxLayout(self.AccountIdFrame)
        self.VerticalLayout06.setObjectName('VerticalLayout06')
        self.VerticalLayout06.setContentsMargins(0,0,0,0)
        self.VerticalLayout06.setSpacing(0)

        self.HorizontalLayout = QHBoxLayout(self.HeaderFrame)
        self.HorizontalLayout.setObjectName('HorizontalLayout')
        self.HorizontalLayout.setContentsMargins(0,0,0,0)
        self.HorizontalLayout.setSpacing(0)
        
        self.HorizontalLayout01 = QHBoxLayout(self.TitleFrame)
        self.HorizontalLayout01.setObjectName('HorizontalLayout01')
        self.HorizontalLayout01.setContentsMargins(0,0,0,0)
        self.HorizontalLayout01.setSpacing(0)

        self.HorizontalLayout02 = QHBoxLayout(self.TitleLabelFrame)
        self.HorizontalLayout02.setObjectName('HorizontalLayout02')
        self.HorizontalLayout02.setContentsMargins(25,0,0,0)
        self.HorizontalLayout02.setSpacing(0)

        self.HorizontalLayout03 = QHBoxLayout(self.BtnFrame)
        self.HorizontalLayout03.setObjectName('HorizontalLayout03')
        self.HorizontalLayout03.setContentsMargins(0,0,0,0)
        self.HorizontalLayout03.setSpacing(0)
        
        self.HorizontalLayout04 = QHBoxLayout(self.BalanceFrame)
        self.HorizontalLayout04.setObjectName('VerticalLayout05')
        self.HorizontalLayout04.setContentsMargins(0,0,0,0)
        self.HorizontalLayout04.setSpacing(0)

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
        self.VerticalLayout04.addWidget(self.BalanceLabel01)
        self.VerticalLayout04.addWidget(self.BalanceFrame)
        self.VerticalLayout04.addWidget(self.AccountIdFrame)
        self.VerticalLayout06.addWidget(self.AccountIdLabel)
        self.HorizontalLayout.addWidget(self.HeaderLabel)
        self.HorizontalLayout01.addWidget(self.TitleLabelFrame)
        self.HorizontalLayout01.addItem(self.SeparatorHorizontal)
        self.HorizontalLayout01.addWidget(self.BtnFrame)
        self.HorizontalLayout02.addWidget(self.TitleLabel)
        self.HorizontalLayout03.addWidget(self.BtnReturn)
        self.HorizontalLayout03.addWidget(self.BtnExit)
        self.HorizontalLayout04.addWidget(self.BalanceLabel02)

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