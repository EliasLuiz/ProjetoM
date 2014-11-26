from PyQt4 import QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Projeto M")
        
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

        #criacao da barra de menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Banco')
        fileMenu.addAction(loadAction)
        fileMenu.addAction(sqlAction)
        
        
    def sqlCall(self):
        from gui import result
        from database import db
        
        #abre janela de dialogo
        sql, ok = QtGui.QInputDialog.getText(self, 'Inserir SQL', 
            'Insira o comando SQL:')
        #executa sql e abre janela com resultado
        if ok:
            print sql
            res = result.ResultWindow2(db.query(str(sql)))
            res.show()
        aux = MainWindow()
        aux.show()
        
        
    def loadCall(self):
        from gui import fileDialog
        from database import inep2012
        
        inep2012.carrega(fileDialog.pickDirectory())