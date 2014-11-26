from PyQt4 import QtGui

class ResultWindow(QtGui.QMainWindow):
    '''
    cria uma tela com os resultados da busca
    '''
    
    def __init__(self, res):
        
        super(ResultWindow, self).__init__()
        
        #cria um text edit na janela toda
        self.resultado = QtGui.QTextEdit()
        self.setCentralWidget(self.resultado)
        
        #joga os resultados na janela
        self.resultado.setText(self.res2str(res))
        
        #cria a janela
        self.setWindowTitle('Resultados da Busca')
        self.show()
        
        
    def res2str(self, res):
        
        strRes = ""
        
        if isinstance(res, list):
            for i in res:
                for j in i:
                    strRes += str(j) + "\t\t\t"
                strRes += "\n"    
                        
        elif isinstance(res, tuple):
            for j in i:
                strRes += str(j) + "\t"
            
        else:
            strRes = str(res)
        
        return strRes
    
class ResultWindow2(QtGui.QDialog):
    '''
    cria uma tela com os resultados da busca
    '''
    
    def __init__(self, res):
        
        super(ResultWindow2, self).__init__()
        
        #cria um text edit na janela toda
        self.resultado = QtGui.QGridLayout()
        
        #joga os resultados na janela
        self.res2grid(res)
        
        #cria a janela
        self.setLayout(self.resultado)
        self.setWindowTitle('Resultados da Busca')
        
        
    def res2grid(self, res):
        
        if isinstance(res, (list,tuple)):
            for i in range(len(res)):
                try:
                    #caso seja uma lista de tuplas
                    for j in range(len(res[i])):
                        label = QtGui.QLabel(str(res[i][j]))
                        self.resultado.addWidget(label, i, j)
                        
                except:
                    #caso seja uma lista ou tupla simples
                    label = QtGui.QLabel(str(res[i]))
                    self.resultado.addWidget(label, i, 0)
            
        else:
            #caso seja somente um valor
            label = QtGui.QLabel(str(res))
            self.resultado.addWidget(label, i, j)