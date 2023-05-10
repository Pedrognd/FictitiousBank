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
        self.AccountDataFrame.setMaximumHeight(250)
        self.AccountDataFrame.setMinimumHeight(250)
        # Back = QPixmap("Icons\Recortada.jpg")
        # self.AccountDataFrame.setStyleSheet(f'background-image: url({Back});')

        self.FuncFrame = QFrame(self.MainFrame)
        self.FuncFrame.setObjectName('FuncFrame')
        self.FuncFrame.setStyleSheet(self.Color03)
        # self.opacity_effect = QGraphicsOpacityEffect()
        # self.opacity_effect.setOpacity(0.3)
        # self.FuncFrame.setGraphicsEffect(self.opacity_effect)

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
        self.BtnExit.clicked.connect(self.ExitFunc)

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
        self.BalanceLabel02.setMaximumHeight(35)
        self.BalanceLabel02.setStyleSheet(f'font: 15pt \'Agency FB\'; color: #ccc4cf; background-color:#7c96c7; border-radius:10px;')
        self.BalanceLabel02.setText('R$ 1.999,99')
        self.BalanceLabel02.setAlignment(Qt.AlignCenter)

        self.AccountIdFrame = QFrame(self.AccountFrame)
        self.AccountIdFrame.setObjectName('AccountIdFrame')
        self.AccountIdFrame.setMaximumHeight(50)

        self.AccountIdLabel = QLabel(self.AccountIdFrame)
        self.AccountIdLabel.setObjectName('AccountIdLabel')
        self.AccountIdLabel.setStyleSheet(f'font: 15pt \'Agency FB\'; color: #ccc4cf;')
        self.AccountIdLabel.setText('67308067894564')
        self.AccountIdLabel.setAlignment(Qt.AlignCenter)

        #### FUNCFRAME ####
        self.BtnFuncFrame = QFrame(self.FuncFrame)
        self.BtnFuncFrame.setObjectName('BtnFuncFrame')

        self.BtnInvestment = QPushButton(self.BtnFuncFrame)
        self.BtnInvestment.setObjectName("BtnInvestment")
        self.BtnInvestment.setMinimumSize(QSize(150, 150))
        self.BtnInvestment.setMaximumSize(QSize(150, 150))
        self.BtnInvestment.setCursor(QCursor(Qt.PointingHandCursor))
        self.BtnInvestment.setText("")
        self.BtnInvestment.setStyleSheet('border-radius:25px;')
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons\Account_App.png"), QIcon.Normal, QIcon.Off)
        self.BtnInvestment.setIcon(icon)
        self.BtnInvestment.setIconSize(QSize(150, 150))
        self.BtnInvestment.setShortcut("")
        self.BtnInvestment.setCheckable(True)
        self.BtnInvestment.setFlat(True)

        self.BtnActivities = QPushButton(self.BtnFuncFrame)
        self.BtnActivities.setObjectName("BtnActivities")
        self.BtnActivities.setMinimumSize(QSize(150, 150))
        self.BtnActivities.setMaximumSize(QSize(150, 150))
        self.BtnActivities.setCursor(QCursor(Qt.PointingHandCursor))
        self.BtnActivities.setText("")
        self.BtnActivities.setStyleSheet('border-radius:25px;')
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons\Account_App.png"), QIcon.Normal, QIcon.Off)
        self.BtnActivities.setIcon(icon)
        self.BtnActivities.setIconSize(QSize(150, 150))
        self.BtnActivities.setShortcut("")
        self.BtnActivities.setCheckable(True)
        self.BtnActivities.setFlat(True)

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
        self.VerticalLayout03.setSpacing(10)

        self.VerticalLayout04 = QVBoxLayout(self.AccountFrame)
        self.VerticalLayout04.setObjectName('VerticalLayout04')
        self.VerticalLayout04.setContentsMargins(0,0,0,0)
        self.VerticalLayout04.setSpacing(0)
        
        self.VerticalLayout06 = QVBoxLayout(self.AccountIdFrame)
        self.VerticalLayout06.setObjectName('VerticalLayout06')
        self.VerticalLayout06.setContentsMargins(0,0,0,0)
        self.VerticalLayout06.setSpacing(0)

        self.VerticalLayout07 = QVBoxLayout(self.FuncFrame)
        self.VerticalLayout07.setObjectName('VerticalLayout07')
        self.VerticalLayout07.setContentsMargins(0,0,0,0)
        self.VerticalLayout07.setSpacing(0)

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

        self.GridLayout = QGridLayout(self.BtnFuncFrame)
        self.GridLayout.setObjectName('GridLayout')
        self.GridLayout.setContentsMargins(5,5,5,5)
        self.GridLayout.setSpacing(5)

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
        self.VerticalLayout07.addWidget(self.BtnFuncFrame)
        self.HorizontalLayout.addWidget(self.HeaderLabel)
        self.HorizontalLayout01.addWidget(self.TitleLabelFrame)
        self.HorizontalLayout01.addItem(self.SeparatorHorizontal)
        self.HorizontalLayout01.addWidget(self.BtnFrame)
        self.HorizontalLayout02.addWidget(self.TitleLabel)
        self.HorizontalLayout03.addWidget(self.BtnReturn)
        self.HorizontalLayout03.addWidget(self.BtnExit)
        self.HorizontalLayout04.addWidget(self.BalanceLabel02)
        self.GridLayout.addWidget(self.BtnInvestment,0,0,1,1)
        self.GridLayout.addWidget(self.BtnActivities,0,1,1,1)

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