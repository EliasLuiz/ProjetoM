from PyQt4 import QtGui, QtCore
from database import db
from database import inep2012
from database import caged
from gui import inputWindow, fileDialog, dataGridView
from time import strftime


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
        self.setWindowTitle("PROJETO M")
        
        self.criaMenu()
        
        self.statusBar()
        
        self.setCentralWidget(self.criaLayout())
        
        self.resize(200, 300)

        
    def criaMenu(self):
        
        #submenu de carregar base de dados
        loadAction = QtGui.QMenu('Carregar', self)
        #acao de carregar base de dados inep2012
        inep2012 = QtGui.QAction('INEP2012', self)
        inep2012.setStatusTip('Carregar base de dados INEP 2012')
        inep2012.triggered.connect(self.loadCallInep2012)
        loadAction.addAction(inep2012)
        #acao de carregar base de dados inep2012
        caged = QtGui.QAction('CAGED', self)
        caged.setStatusTip('Carregar base de dados CAGED')
        caged.triggered.connect(self.loadCallCaged)
        loadAction.addAction(caged)
        
        #acao de inserir sql diretamente
        sqlAction = QtGui.QAction('Inserir &SQL', self)        
        sqlAction.setShortcut('Ctrl+S')
        sqlAction.setStatusTip('Insira comandos SQL diretamente no banco')
        sqlAction.triggered.connect(self.sqlCall)
        
        #encerrar a aplicacao
        quitAction = QtGui.QAction('Sair', self)        
        quitAction.setShortcut('Ctrl+Q')
        quitAction.setStatusTip('Encerra o programa')
        quitAction.triggered.connect(QtCore.QCoreApplication.instance().quit)
        
        #criacao da barra de menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Arquivo')
        fileMenu.addMenu(loadAction)
        fileMenu.addAction(sqlAction)
        fileMenu.addAction(quitAction)

    #LAYOUT DA CLASSE
    def criaLayout(self):
        
        scroll = QtGui.QScrollArea()
        w = QtGui.QWidget()
        vbox = QtGui.QVBoxLayout()
        
        
        #busca do banco os schemas
        #  sera gerada uma inputWindow para cada janela
        self.schemas = db.buscaSchemas()
        
        
        self.botoes = []
        for i in self.schemas:
            self.botoes.append(QtGui.QPushButton(i))
            
        for i in range(len(self.botoes)):
            self.botoes[i].setStatusTip('''Abre janela para pesquisa na base
de dados ''' + self.schemas[i].upper())
            self.botoes[i].clicked.connect(self.criaJanela)
            vbox.addWidget(self.botoes[i])
            
        w.setLayout(vbox)
        scroll.setWidget(w)
        return scroll
    
    #ACOES DA CLASSE
    def criaJanela(self):
        
        sender = self.sender()
        win = inputWindow.InputWindow(str(sender.text()), self)
        win.show()
        
        
    def loadCallInep2012(self):
	
        diretorio = fileDialog.pickDirectory()
		
        if diretorio != "":
            print strftime('%H:%M:%S')
            inep2012.carrega(diretorio)
            print strftime('%H:%M:%S')
            
        QtCore.QCoreApplication.instance().quit()
        
        
    def loadCallCaged(self):
        
        arquivo = fileDialog.pickFile("*.txt")
		
        if arquivo != "":
            print strftime('%H:%M:%S')
            caged.carrega(arquivo)
            print strftime('%H:%M:%S')
            
        QtCore.QCoreApplication.instance().quit()
        
        
    def sqlCall(self):
        
        #abre janela de dialogo
        sql, ok = QtGui.QInputDialog.getText(self, 'Inserir SQL', 
            'Insira o comando SQL:')
        #executa sql e abre janela com resultado
        if ok:
            sql = str(sql)
            campos = db.camposRetornoSql(sql) 
            if campos[0] == '*':
                campos = None
            db.insereSqlLog(sql)
            dataGridView.DataGridView(db.query(sql), campos, sql.upper())
            db.commit()
        