import sys
import os

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog,QMessageBox
from PyQt5.QtCore import QCoreApplication

from tela_inicial import Tela_Inial
from tela_cadastro import Tela_Cadastro
from tela_busca import Tela_Buscar
from pessoa import Pessoa
from cadastro import Cadastro

class Ui_Main(QtWidgets.QWidget):

    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_busca = Tela_Buscar()
        self.tela_busca.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

class Main(QMainWindow, Ui_Main):

    def __init__ (self,parent = None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        self.tela_inicial.pushButton.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaBuscar)

        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastra)
        self.tela_busca.pushButton.clicked.connect(self.botaoBusca)
        self.tela_busca.pushButton_2.clicked.connect(self.botaoVotar)

    def botaoCadastra(self):
        nome = self.tela_cadastro.lineEdit.text()
        endereco = self.tela_cadastro.lineEdit_2.text()
        cpf = self.tela_cadastro.lineEdit_3.text()
        nascimento = self.tela_cadastro.lineEdit_4.text()

        if not(nome == '' or endereco == '' or cpf == '' or cpf == '' or nascimento == ''):
            p = Pessoa(nome,endereco,cpf,nascimento)
            if (self.cad.cadastra(p)):
                QMessageBox.information(None,'POOII',"Cadastro realizado com sucesso!")
                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
            else:
                QMessageBox.information(None,'POOII','O CPF iformado ja esta cadastrado na base de dados!')
        else:
            QMessageBox.information(None,'POOII','Todos os campos devem ser preenchidos!')

        self.QtStack.setCurrentIndex(0)

    def botaoBusca(self):
        cpf = self.tela_busca.lineEdit.text()
        pessoa = self.cad.busca(cpf)
        if(pessoa != None):
            self.tela_busca.lineEdit_2.setText(pessoa.nome)
            self.tela_busca.lineEdit_3.setText(pessoa.endereco)
            self.tela_busca.lineEdit_4.setText(pessoa.nascimento)
        else:
            QMessageBox.information(None,'POOII','CPF não encontrado!')
            self.tela_busca.lineEdit.setText('')

    def botaoVotar(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaBuscar(self):
        self.QtStack.setCurrentIndex(2)

if __name__=='__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())