from PyQt5 import uic,QtWidgets,QtCore
import ImageAndIcons
import os

def SegundaTela():
    MainScreen.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    MainScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    MainScreen.ExitBtn.clicked.connect(MainScreen.close)
    MainScreen.show()
    LoginScreen.close()


app = QtWidgets.QApplication([])
LoginScreen=uic.loadUi('FictitiousBank01.ui')
MainScreen=uic.loadUi('FictitiousBank02.ui')
LoginScreen.setWindowFlag(QtCore.Qt.FramelessWindowHint)
LoginScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)
LoginScreen.ExitBtn.clicked.connect(LoginScreen.close)
LoginScreen.LoginBtn.clicked.connect(SegundaTela)

LoginScreen.show()
app.exec()