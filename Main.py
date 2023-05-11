from PyQt5 import uic,QtWidgets,QtCore
import ImageAndIcons
import os

class Func():
    def __init__(self):
        self.BalanceAccount = 2
        self.LenBalance = len(f'R$ {self.BalanceAccount:.2f}')

    def BalanceFormat(self):
        Balance = f'R$ {self.BalanceAccount:_.2f}'
        Balance = Balance.replace('.',',').replace('_','.')
        return Balance
    
    def WidthSizeChange(self):
        if self.LenBalance <= 9:
            NewWd = 75
        elif self.LenBalance <= 12:
            NewWd = 105
        elif self.LenBalance <= 14:
            NewWd = 135
        else:
            NewWd = 150
        return NewWd

def SegundaTela():
    MainScreen.BalanceLabel.setText(Func().BalanceFormat())
    NewWidthSize = Func().WidthSizeChange()
    MainScreen.BalanceLabel.setMaximumWidth(NewWidthSize)
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