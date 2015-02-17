#-*- coding: latin -*-
from PyQt4 import QtGui, QtCore
from database import db


class InputWindow(QtGui.QMainWindow):
    def __init__(self, schema):
        super(InputWindow, self).__init__()
        
        #widget = QtGui.QWidget()
        #self.setCentralWidget(widget)
        
        self.schema = schema
        self.setWindowTitle(schema.upper())
        
        self.criaMenu()
        
        self.statusBar()
        
        self.setCentralWidget(self.criaLayout())
        
        
    #LAYOUT DA CLASSE
    def criaMenu(self):
        #acao de inserir sql diretamente
        sqlAction = QtGui.QAction('&Inserir SQL', self)        
        sqlAction.setShortcut('Ctrl+S')
        sqlAction.setStatusTip('Insira comandos SQL diretamente no banco')
        sqlAction.triggered.connect(self.sqlCall)
        
        #acao de carregar base de dados
        loadAction = QtGui.QAction('&Carregar', self)        
        loadAction.setShortcut('Ctrl+L')
        loadAction.setStatusTip('Carregar base de dados INEP 2012')
        loadAction.triggered.connect(self.loadCall)
        
        #encerrar a aplicacao
        quitAction = QtGui.QAction('&Sair', self)        
        quitAction.setShortcut('Ctrl+Q')
        quitAction.setStatusTip('Encerra o programa')
        quitAction.triggered.connect(QtCore.QCoreApplication.instance().quit)

        #criacao da barra de menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Banco')
        fileMenu.addAction(loadAction)
        fileMenu.addAction(sqlAction)
        fileMenu.addAction(quitAction)
    
    
    def criaLayout(self):
        scroll = QtGui.QScrollArea()
        w = QtGui.QWidget()
        
        vbox = QtGui.QVBoxLayout()
        
                
        self.tabelas = {}
        
        tabelas = [i[2] for i in db.query('''
        SELECT * FROM information_schema.tables 
        WHERE table_schema = ''' + "'" + self.schema + "'" + '''
        ''')]
        
        #grid.addLayout(self.cabecalhoLayout(), 0, 0)
        for i in tabelas:
            vbox.addLayout(self.tabelaLayout(i))
        
        w.setLayout(vbox)
        scroll.setWidget(w)
        return scroll
    
    def cabecalhoLayout(self):
        #FICA DESALINHADO - REPENSARR
        
        grid = QtGui.QGridLayout()
        
        self.campo = QtGui.QLabel('Campo')
        self.retorno = QtGui.QLabel('Retornar')
        self.igual = QtGui.QLabel('Igual a')
        self.like = QtGui.QLabel('Like')
        grid.addWidget(self.campo, 0, 0)
        grid.addWidget(self.retorno, 0, 1)
        grid.addWidget(self.igual, 0, 2)
        grid.addWidget(self.like, 0, 3)
        
        return grid
        
    def tabelaLayout(self, tabela):
        '''
        tabela = string contendo o nome da tabela
        retorna um grid contendo os campos para cada coluna de uma tabela
        '''
        #TRANSFORMAR EM GRID
        vbox = QtGui.QVBoxLayout()
        
        #titulo
        titulo = QtGui.QLabel(tabela.upper())
        vbox.addWidget(titulo)
        
        colunas = [i[3] for i in db.query('''
            SELECT *
            FROM information_schema.columns
            WHERE table_schema = ''' + "'" + self.schema + ''''
            AND table_name   = ''' + "'" + tabela + "'")]
        
        self.tabelas[tabela] = []
        for i in colunas:
            aux = []
            aux.append(i)
            aux.append(QtGui.QLabel(i))
            aux.append(QtGui.QCheckBox(''))
            aux.append(QtGui.QLineEdit())
            aux.append(QtGui.QCheckBox(''))
            self.tabelas[tabela].append(aux)
            
        for i in range(len(self.tabelas[tabela])):
            aux = QtGui.QHBoxLayout()
            for j in range(1, len(self.tabelas[tabela][0])):
                aux.addWidget(self.tabelas[tabela][i][j])
            aux.addStretch(1)
            vbox.addLayout(aux)
        
        return vbox
        
        
    #ACOES DA CLASSE
    def sqlCall(self):
        from gui.dataGridView import DataGridView
        from database import db
        
        #abre janela de dialogo
        sql, ok = QtGui.QInputDialog.getText(self, 'Inserir SQL', 
            'Insira o comando SQL:')
        #executa sql e abre janela com resultado
        if ok:
            sql = str(sql)
            campos = db.camposRetornoSql(sql) 
            if campos[0] == '*':
                campos = None
            res = DataGridView(db.query(sql), campos)
            res.show()
        #aux = Inep2012Window()
        #aux.show()
        
        
    def loadCall(self):
        from gui import fileDialog
        from database import inep2012
        
        inep2012.carrega(fileDialog.pickDirectory())
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    w = InputWindow('inep2012')
    w.show()
    w.raise_()
    sys.exit(app.exec_())