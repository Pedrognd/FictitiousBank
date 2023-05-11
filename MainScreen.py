# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Screens\FictitiousBank02.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import ImageAndIcons


class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(360, 450)
        MainScreen.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainScreen.setStyleSheet("#BackgroundFrame{\n"
"    background-image: url(:/newPrefix/BackGroundMain.png);\n"
"    border-radius:25px;\n"
"    background-position: center;\n"
"}\n"
"\n"
"#MainFrame{\n"
"    background-color: rgba(26, 84, 191,0.7);\n"
"    border-radius:25px;\n"
"}\n"
"\n"
"#HeaderFrame{\n"
"    background-color: rgba(26, 84, 191,1);\n"
"    border-radius:25px;\n"
"}\n"
"\n"
"#TitleLabel{\n"
"    color: rgb(229, 229, 229);\n"
"    font: 30pt Agency FB;\n"
"}\n"
"\n"
"#UserLabel{\n"
"    color: rgb(229, 229, 229);\n"
"    font: 15pt Agency FB;\n"
"}\n"
"\n"
"#ExitBtn{\n"
"    image: url(:/newPrefix/Btt_Exit.png);\n"
"    border-radius:25px;\n"
"}\n"
"\n"
"#ExitBtn:hover{\n"
"    image: url(:/newPrefix/Btt_Exit_Hover.png);\n"
"    border-radius:25px;\n"
"}\n"
"\n"
"#Label00{\n"
"    color: rgb(229, 229, 229);\n"
"    font: 15pt Agency FB;\n"
"}\n"
"\n"
"#BalanceLabel{\n"
"    background-color: rgba(229,229, 229,0.3);\n"
"    border-radius:15px;\n"
"    color: rgb(229, 229, 229);\n"
"    font: 15pt Agency FB;\n"
"}\n"
"\n"
"#IdAccount{\n"
"    color: rgb(229, 229, 229);\n"
"    font: 15pt Agency FB;\n"
"}\n"
"\n"
"#InvestmentBtn{\n"
"    \n"
"    image: url(:/newPrefix/Btn_Investment.png);\n"
"    border-radius:25px;\n"
"}\n"
"\n"
"#InvestmentBtn:hover{\n"
"    image: url(:/newPrefix/Btn_Investment_Hover.png);\n"
"    border-radius:25px;\n"
"}\n"
"\n"
"#ActivitiesBtn{\n"
"    image: url(:/newPrefix/Btn_Activities.png);\n"
"    border-radius:25px;\n"
"}\n"
"\n"
"#ActivitiesBtn:hover{\n"
"    image: url(:/newPrefix/Btn_Activities_Hover.png);\n"
"    border-radius:25px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(MainScreen)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BackgroundFrame = QtWidgets.QFrame(MainScreen)
        self.BackgroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackgroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackgroundFrame.setObjectName("BackgroundFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.BackgroundFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MainFrame = QtWidgets.QFrame(self.BackgroundFrame)
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.MainFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.HeaderFrame = QtWidgets.QFrame(self.MainFrame)
        self.HeaderFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.HeaderFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.HeaderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HeaderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HeaderFrame.setObjectName("HeaderFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.HeaderFrame)
        self.horizontalLayout.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TitleLabel = QtWidgets.QLabel(self.HeaderFrame)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.horizontalLayout.addWidget(self.TitleLabel)
        self.verticalLayout_3.addWidget(self.HeaderFrame)
        self.BodyFrame = QtWidgets.QFrame(self.MainFrame)
        self.BodyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BodyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BodyFrame.setObjectName("BodyFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.BodyFrame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ToolBar = QtWidgets.QFrame(self.BodyFrame)
        self.ToolBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ToolBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ToolBar.setObjectName("ToolBar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ToolBar)
        self.horizontalLayout_4.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.UserLabel = QtWidgets.QLabel(self.ToolBar)
        self.UserLabel.setObjectName("UserLabel")
        self.horizontalLayout_4.addWidget(self.UserLabel)
        spacerItem = QtWidgets.QSpacerItem(142, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.ExitBtn = QtWidgets.QPushButton(self.ToolBar)
        self.ExitBtn.setMinimumSize(QtCore.QSize(50, 50))
        self.ExitBtn.setMaximumSize(QtCore.QSize(50, 50))
        self.ExitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitBtn.setText("")
        self.ExitBtn.setFlat(True)
        self.ExitBtn.setObjectName("ExitBtn")
        self.ExitBtn.clicked.connect(self.ExitFunc)
        self.horizontalLayout_4.addWidget(self.ExitBtn)
        self.verticalLayout_4.addWidget(self.ToolBar)
        self.Label00 = QtWidgets.QLabel(self.BodyFrame)
        self.Label00.setAlignment(QtCore.Qt.AlignCenter)
        self.Label00.setObjectName("Label00")
        self.verticalLayout_4.addWidget(self.Label00)
        self.BalanceFrame = QtWidgets.QFrame(self.BodyFrame)
        self.BalanceFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BalanceFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BalanceFrame.setObjectName("BalanceFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.BalanceFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BalanceLabel = QtWidgets.QLabel(self.BalanceFrame)
        self.BalanceLabel.setMaximumSize(QtCore.QSize(100, 35))
        self.BalanceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BalanceLabel.setObjectName("BalanceLabel")
        self.horizontalLayout_3.addWidget(self.BalanceLabel)
        self.verticalLayout_4.addWidget(self.BalanceFrame)
        self.IdAccount = QtWidgets.QLabel(self.BodyFrame)
        self.IdAccount.setAlignment(QtCore.Qt.AlignCenter)
        self.IdAccount.setObjectName("IdAccount")
        self.verticalLayout_4.addWidget(self.IdAccount)
        self.verticalLayout_3.addWidget(self.BodyFrame)
        self.FooterFrame = QtWidgets.QFrame(self.MainFrame)
        self.FooterFrame.setStyleSheet("")
        self.FooterFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FooterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FooterFrame.setObjectName("FooterFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.FooterFrame)
        self.horizontalLayout_2.setContentsMargins(30, 0, 30, 30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.InvestmentBtn = QtWidgets.QPushButton(self.FooterFrame)
        self.InvestmentBtn.setMinimumSize(QtCore.QSize(140, 140))
        self.InvestmentBtn.setMaximumSize(QtCore.QSize(140, 140))
        self.InvestmentBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.InvestmentBtn.setText("")
        self.InvestmentBtn.setFlat(True)
        self.InvestmentBtn.setObjectName("InvestmentBtn")
        self.horizontalLayout_2.addWidget(self.InvestmentBtn)
        self.ActivitiesBtn = QtWidgets.QPushButton(self.FooterFrame)
        self.ActivitiesBtn.setMinimumSize(QtCore.QSize(140, 140))
        self.ActivitiesBtn.setMaximumSize(QtCore.QSize(140, 140))
        self.ActivitiesBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ActivitiesBtn.setText("")
        self.ActivitiesBtn.setFlat(True)
        self.ActivitiesBtn.setObjectName("ActivitiesBtn")
        self.horizontalLayout_2.addWidget(self.ActivitiesBtn)
        self.verticalLayout_3.addWidget(self.FooterFrame)
        self.verticalLayout_2.addWidget(self.MainFrame)
        self.verticalLayout.addWidget(self.BackgroundFrame)

        self.retranslateUi(MainScreen)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "Form"))
        self.TitleLabel.setText(_translate("MainScreen", "Central Bank"))
        self.UserLabel.setText(_translate("MainScreen", "Olá, João Nobre..."))
        self.Label00.setText(_translate("MainScreen", "Saldo da Conta"))
        self.BalanceLabel.setText(_translate("MainScreen", "R$ 2000,00"))
        self.IdAccount.setText(_translate("MainScreen", "97816465416617687674"))

    def ExitFunc(self):
        MainScreen.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainScreen = QtWidgets.QWidget()
    ui = Ui_MainScreen()
    ui.setupUi(MainScreen)
    MainScreen.show()
    sys.exit(app.exec_())
