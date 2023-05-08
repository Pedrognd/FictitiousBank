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
        
        self.ToolsFrame = QFrame(self.MainFrame)
        self.ToolsFrame.setObjectName('ToolsFrame')
        self.ToolsFrame.setMinimumHeight(115)
        self.ToolsFrame.setMaximumHeight(115)

        self.ContFrame = QFrame(self.MainFrame)
        self.ContFrame.setObjectName('ContFrame')

        #### BLOCK TOOLSFRAME ####
        self.ToolBar = QFrame(self.ToolsFrame)
        self.ToolBar.setObjectName('ToolBar')
        self.ToolBar.setMinimumHeight(50)
        self.ToolBar.setMaximumHeight(50)

        self.ExitFrame = QFrame(self.ToolBar)
        self.ExitFrame.setObjectName('ExitFrame')
        self.ExitFrame.setMinimumSize(QSize(50,50))
        self.ExitFrame.setMaximumSize(QSize(50,50))

        self.Exit = QPushButton(self.ExitFrame)
        self.Exit.setObjectName("Exit")
        self.Exit.setMinimumSize(QSize(50, 50))
        self.Exit.setMaximumSize(QSize(50, 50))
        self.Exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.Exit.setText("")
        self.Exit.setStyleSheet('border-radius:25px;')
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons\Btt_Exit.png"), QIcon.Normal, QIcon.Off)
        self.Exit.setIcon(icon)
        self.Exit.setIconSize(QSize(50, 50))
        self.Exit.setShortcut("")
        self.Exit.setCheckable(True)
        self.Exit.setFlat(True)
        self.Exit.clicked.connect(self.ExitFunc)

        self.LabelFrame = QFrame(self.ContFrame)
        self.LabelFrame.setObjectName('LabelFrame')

        self.Label = QLabel(self.LabelFrame)
        self.Label.setObjectName('Label')
        self.Label.setStyleSheet(f"font: 48pt \"Agency FB\";color: #E5E5E5")
        self.Label.setText("Central Bank")
        self.Label.setAlignment(Qt.AlignCenter)

        self.LoginFrame = QFrame(self.ContFrame)
        self.LoginFrame.setObjectName('LoginFrame')
        self.LoginFrame.setMinimumHeight(50)
        self.LoginFrame.setMaximumHeight(50)

        self.Login = QPushButton(self.LoginFrame)
        self.Login.setObjectName("Login")
        self.Login.setMinimumHeight(50)
        self.Login.setMaximumHeight(50)
        self.Login.setCursor(QCursor(Qt.PointingHandCursor))
        self.Login.setText("")
        self.Login.setStyleSheet('border-radius:10px;')
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons\Btt_Login.png"), QIcon.Normal, QIcon.Off)
        self.Login.setIcon(icon)
        self.Login.setIconSize(QSize(250, 50))
        self.Login.setShortcut("")
        self.Login.setCheckable(True)
        self.Login.setFlat(True)
        self.Login.clicked.connect(self.ExitFunc)

        #### LAYOUT'S ####
        self.VerticalLayout = QVBoxLayout(Form)
        self.VerticalLayout.setContentsMargins(0,0,0,0)
        self.VerticalLayout.setSpacing(0)
        self.VerticalLayout.setObjectName("VerticalLayout")

        self.VerticalLayout02 = QVBoxLayout(self.MainFrame)
        self.VerticalLayout02.setObjectName('VerticalLayout02')
        self.VerticalLayout02.setContentsMargins(0,0,0,0)
        self.VerticalLayout02.setSpacing(0)

        self.VerticalLayout03 = QVBoxLayout(self.ContFrame)
        self.VerticalLayout03.setObjectName('VerticalLayout03')
        self.VerticalLayout03.setContentsMargins(30,0,30,30)
        self.VerticalLayout03.setSpacing(0)

        self.HorizontalLayout = QHBoxLayout(self.ToolsFrame)
        self.HorizontalLayout.setObjectName('HorizontalLayout')
        self.HorizontalLayout.setContentsMargins(30,30,30,0)
        self.HorizontalLayout.setSpacing(0)

        self.HorizontalLayout02 = QHBoxLayout(self.ToolBar)
        self.HorizontalLayout02.setObjectName('HorizontalLayout02')
        self.HorizontalLayout02.setContentsMargins(0,0,0,0)
        self.HorizontalLayout02.setSpacing(0)

        self.HorizontalLayout03 = QHBoxLayout(self.LoginFrame)
        self.HorizontalLayout03.setObjectName('HorizontalLayout03')
        self.HorizontalLayout03.setContentsMargins(0,0,0,0)
        self.HorizontalLayout03.setSpacing(0)

        self.HorizontalLayout04 = QHBoxLayout(self.LabelFrame)
        self.HorizontalLayout04.setObjectName('HorizontalLayout04')
        self.HorizontalLayout04.setContentsMargins(0,0,0,0)
        self.HorizontalLayout04.setSpacing(0)
        
        #### SEPARATOR'S ####
        self.SeparatorHorizontal = QSpacerItem(40,50,QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.SeparatorVertical = QSpacerItem(40,50, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        #### ADD ITENS TO LAYOUT'S ####
        self.VerticalLayout.addWidget(self.MainFrame)
        self.VerticalLayout02.addWidget(self.ToolsFrame)
        self.VerticalLayout02.addWidget(self.ContFrame)
        self.VerticalLayout03.addWidget(self.LabelFrame)
        self.VerticalLayout03.addItem(self.SeparatorVertical)
        self.VerticalLayout03.addWidget(self.LoginFrame)
        self.HorizontalLayout.addWidget(self.ToolBar)
        self.HorizontalLayout02.addItem(self.SeparatorHorizontal)
        self.HorizontalLayout02.addWidget(self.ExitFrame) 
        self.HorizontalLayout03.addWidget(self.Login)
        self.HorizontalLayout04.addWidget(self.Label)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate('LoginScreen', 'LoginScreen'))

    def ExitFunc(self):
        Form.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())