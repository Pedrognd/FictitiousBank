from PyQt5 import uic,QtWidgets,QtCore
import ImageAndIcons
import os


#### Classe para Ajustar Background do Label ####
class Func():
    def __init__(self):
        self.BalanceAccount = 2
        self.LenBalance = len(f'R$ {self.BalanceAccount:.2f}')

    #### Troca de pontuações, '_' para '.' e '.' para ',' ####
    def BalanceFormat(self):
        Balance = f'R$ {self.BalanceAccount:_.2f}'
        Balance = Balance.replace('.',',').replace('_','.')
        return Balance
    
    #### Troca de Largura do Background ####
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
    
    # def ReturnBtn(self,active,request):
    #     if active == 0:
    #         active = ListScreen[0]
    #     if active.close() == True:
    #         request.show()

#### Função para Chamar Tela de MainScreen (A Segunda Tela) ####
def SegundaTela():
    # Tirar Barra de Tarefas e Deixa o Form Principal 'Invisivel' 
    MainScreen.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    MainScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # Troca de Largura do Background do Balance Label
    MainScreen.BalanceLabel.setText(Func().BalanceFormat())
    NewWidthSize = Func().WidthSizeChange()
    MainScreen.BalanceLabel.setMaximumWidth(NewWidthSize)

    # Funções dos Botões, de Fechar Tela e Abrir a Proxima Tela
    MainScreen.ExitBtn.clicked.connect(MainScreen.close)
    MainScreen.InvestmentBtn.clicked.connect(TerceiraTela)

    # Iniciar o Form e Fechar Tela Anterior
    MainScreen.show()
    LoginScreen.close()

#### Função para Chamar Tela de InvestmentScreen (A Terceira Tela) ####
def TerceiraTela():
    # Tirar Barra de Tarefas e Deixa o Form Principal 'Invisivel' 
    InvestmentScreen.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    InvestmentScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # Função do Botão, Fechar a Tela 
    InvestmentScreen.ReturnBtn.clicked.connect(ReturnBtn)

    # Iniciar o Form e Fechar Tela Anterior
    InvestmentScreen.show()
    MainScreen.hide()
    
#### Função para Quando fechar a Tela de Investimento, Voltar para a Tela Principal #### 
def ReturnBtn():
    # Verifica se a Tela foi Fechada, se 'Sim' Chama a Tela Principal 
    if InvestmentScreen.close() == True:
        MainScreen.show()

#### Carregando os Forms que Foram Feitos no QtDesigner ####
app = QtWidgets.QApplication([])
LoginScreen=uic.loadUi('FictitiousBank01.ui')
MainScreen=uic.loadUi('FictitiousBank02.ui')
InvestmentScreen=uic.loadUi('FictitiousBank03.ui')

def PrimeiraTela():
    # Tirar Barra de Tarefas e Deixa o Form Principal 'Invisivel' 
    LoginScreen.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    LoginScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # Funções dos Botões, de Fechar Tela e Abrir a Proxima Tela
    LoginScreen.ExitBtn.clicked.connect(LoginScreen.close)
    LoginScreen.LoginBtn.clicked.connect(SegundaTela)

    # Iniciar o Form
    LoginScreen.show()

PrimeiraTela()
app.exec()