#-*- coding: latin -*-
from PyQt4 import QtGui, QtCore
from database import db
from gui.dataGridView import DataGridView


class InputWindow(QtGui.QMainWindow):
    def __init__(self, schema):
        super(InputWindow, self).__init__()
        
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
        
        for i in tabelas:
            vbox.addLayout(self.tabelaLayout(i))
            
        self.count = QtGui.QCheckBox('Contar')
        vbox.addWidget(self.count)
            
        self.submit = QtGui.QPushButton('Pesquisar')
        self.submit.clicked.connect(self.submitCall)
        #QtCore.QObject.connect(self.submit, QtCore.SIGNAL('clicked()'), self.submitCall)
        
        vbox.addWidget(self.submit)
        
        w.setLayout(vbox)
        scroll.setWidget(w)
        return scroll
        
    def tabelaLayout(self, tabela):
        '''
        tabela = string contendo o nome da tabela
        retorna um grid contendo os campos para cada coluna de uma tabela
        '''
        grid = QtGui.QGridLayout()
        
        #titulo
        titulo = QtGui.QLabel("\n\n\n" + tabela.upper() + "\n\n")
        grid.addWidget(titulo, 0, 0)
        
        campo = QtGui.QLabel('Campo')
        retorno = QtGui.QLabel('Retornar')
        igual = QtGui.QLabel('Igual a')
        like = QtGui.QLabel('Like')
        grid.addWidget(campo, 1, 0)
        grid.addWidget(retorno, 1, 1)
        grid.addWidget(igual, 1, 2)
        grid.addWidget(like, 1, 3)
        
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
            for j in range(1, len(self.tabelas[tabela][0])):
                grid.addWidget(self.tabelas[tabela][i][j], i+2, j-1)
        
        return grid
        
        
    #ACOES DA CLASSE
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
            DataGridView(db.query(sql), campos)
            db.commit()
        #aux = Inep2012Window()
        #aux.show()
        
        
    def loadCall(self):
        from gui import fileDialog
        
        if self.schema == "inep2012":
            from database import inep2012
            inep2012.carrega(fileDialog.pickDirectory())
            
        QtCore.QCoreApplication.instance().quit()
        
    def submitCall(self):
        
        tabelas = []
        camposDeRetorno = {}
        camposDeBusca = {}
        camposDeFiltro = {}
        
        for tabela, matriz in self.tabelas.iteritems():
            camposDeRetorno[tabela] = []
            camposDeBusca[tabela] = []
            camposDeFiltro[tabela] = []
            for coluna in matriz:
                if coluna[2].isChecked():
                    camposDeRetorno[tabela].append(coluna[0])
                    if tabela not in tabelas:
                        tabelas.append(tabela)
                if str((coluna[3].text()).toUtf8()) != "":
                    if tabela not in tabelas:
                        tabelas.append(tabela)
                    if coluna[4].isChecked():
                        camposDeFiltro[tabela].append((coluna[0], str((coluna[3].text()).toUtf8())))
                    else:
                        camposDeBusca[tabela].append((coluna[0], str((coluna[3].text()).toUtf8())))
        
        if self.count.isChecked():
            camposDeRetorno = 'count(*)'
        
        DataGridView(db.sqlSelectGeneratorSearchFilter(self.schema, tabelas, camposDeRetorno,
                camposDeBusca, camposDeFiltro), db.camposRetornoCabecalho(camposDeRetorno))
        db.commit()
        
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    w = InputWindow('inep2012')
    w.show()
    w.raise_()
    sys.exit(app.exec_())