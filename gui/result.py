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
            
            
            
'''
    import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MyWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        # create table
        self.get_table_data()
        self.table = self.createTable()

        # layout
        self.layout = QVBoxLayout()

        self.testButton = QPushButton("test")
        self.connect(self.testButton, SIGNAL("released()"), self.test)        

        self.layout.addWidget(self.testButton)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def get_table_data(self):
        self.tabledata = [[1234567890,2,3,4,5],
                          [6,7,8,9,10],
                          [11,12,13,14,15],
                          [16,17,18,19,20]]

    def createTable(self):
        # create the view
        tv = QTableView()

        # set the table model
        header = ['col_0', 'col_1', 'col_2', 'col_3', 'col_4']
        tablemodel = MyTableModel(self.tabledata, header, self)
        tv.setModel(tablemodel)

        # set the minimum size
        tv.setMinimumSize(400, 300)

        # hide grid
        tv.setShowGrid(False)

        # hide vertical header
        vh = tv.verticalHeader()
        vh.setVisible(False)

        # set horizontal header properties
        hh = tv.horizontalHeader()
        hh.setStretchLastSection(True)

        # set column width to fit contents
        tv.resizeColumnsToContents()

        # set row height
        tv.resizeRowsToContents()

        # enable sorting
        tv.setSortingEnabled(False)

        return tv

    def test(self):
        self.tabledata.append([1,1,1,1,1])
        self.table.model().layoutChanged.emit()
        print 'success'

class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None):
        """
        Args:
            datain: a list of lists\n
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        if len(self.arraydata) > 0: 
            return len(self.arraydata[0]) 
        return 0

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def setData(self, index, value, role):
        pass         # not sure what to put here

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

    def sort(self, Ncol, order):
        """
        Sort table by given column number.
        """
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))       
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
    '''