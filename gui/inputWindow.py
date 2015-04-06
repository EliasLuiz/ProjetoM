#-*- coding: latin -*-
from PyQt4 import QtGui, QtCore
from database import db
from gui.dataGridView import DataGridView


class InputWindow(QtGui.QMainWindow):
    def __init__(self, schema, parent = None):
        super(InputWindow, self).__init__(parent)
        
        self.schema = schema
        self.setWindowTitle(schema.upper())
        
        #self.criaMenu()
        
        self.statusBar()
        
        self.setCentralWidget(self.criaLayout())
        
        self.resize(500, 1000)
        
        
    #LAYOUT DA CLASSE
    '''
    def criaMenu(self):
        
        #encerrar a aplicacao
        quitAction = QtGui.QAction('Sair', self)        
        quitAction.setShortcut('Ctrl+Q')
        quitAction.setStatusTip('Encerra o programa')
        quitAction.triggered.connect(QtCore.QCoreApplication.instance().quit)

        #criacao da barra de menu
        menubar = QtGui.QMenuBar()
        fileMenu = menubar.addMenu('Banco')
        fileMenu.addAction(quitAction)
    '''
    
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
    def submitCall(self):
        
        tabelas = []
        camposDeRetorno = {}
        camposDeBusca = {}
        camposDeFiltro = {}
        
        #leitura do input do usuario
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
                    valor = (coluna[3].text()).toUtf8()
                    try:
                        valor = float(valor)
                    except:
                        valor = str(valor)
                    if tabela not in tabelas:
                        tabelas.append(tabela)
                    if coluna[4].isChecked():
                        camposDeFiltro[tabela].append((coluna[0], valor))
                    else:
                        camposDeBusca[tabela].append((coluna[0], valor))
        
        if self.count.isChecked():
            camposDeRetorno = 'count(*)'
        
        sql = db.sqlSelectGeneratorSearchFilter(self.schema, tabelas, camposDeRetorno,
                camposDeBusca, camposDeFiltro)
        
        DataGridView(db.query(sql), db.camposRetornoCabecalho(camposDeRetorno), sql.upper())
        db.commit()
        