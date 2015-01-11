import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DataGridView(QWidget):

    def __init__(self, dados, cabecalho=None, editavel=False):
        super(DataGridView, self).__init__()

        # create the view
        self.table = QTableView()

        # set the table model
        if editavel:
            self.table.setModel(MyTableModel(
                    [list(i) for i in dados], list(cabecalho), editavel, self))
        else:
            self.table.setModel(MyTableModel(dados, cabecalho, editavel, self))

        # hide grid
        self.table.setShowGrid(True)

        # hide vertical header
        vh = self.table.verticalHeader()
        vh.setVisible(False)

        # set horizontal header properties
        hh = self.table.horizontalHeader()
        if cabecalho == None:
            hh.setVisible(False)
        #hh.setStretchLastSection(True)

        # set column width to fit contents
        self.table.resizeColumnsToContents()

        # set row height
        self.table.resizeRowsToContents()

        # enable sorting
        self.table.setSortingEnabled(True)
        
        # layout
        self.layout = QVBoxLayout()        

        self.layout.addWidget(self.table)
        self.setLayout(self.layout)
        

class MyTableModel(QAbstractTableModel):
    def __init__(self, dados, cabecalho=None, editavel=False, parent=None):
        """
        Args:
            datain: lista de listas
            cabecalho: lista de strings
            editavel: bool
        """
        super(MyTableModel, self).__init__()
        self.editavel = editavel
        self.parent = parent
        
        self.dados = dados
        
        self.cabecalho = cabecalho
        
        parent.table.resizeColumnsToContents()
        parent.table.resizeRowsToContents()

    def rowCount(self, parent):
        return len(self.dados)

    def columnCount(self, parent):
        if len(self.dados) > 0: 
            return len(self.dados[0]) 
        return 0

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.dados[index.row()][index.column()])

    def setData(self, index, value, role):
        if self.editavel:
            self.dados[index.row()][index.column()] = value.toPyObject()
            self.parent.table.resizeColumnsToContents()
            self.parent.table.resizeRowsToContents()
            return True
        else:
            pass
    
    def flags(self, index):
        if self.editavel:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
        else:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, col, orientation, role):
        if self.cabecalho!=None and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.cabecalho[col])
        return QVariant()

    def sort(self, Ncol, order):
        self.layoutAboutToBeChanged.emit()       
        if order == Qt.AscendingOrder:
            self.dados = sorted(self.dados, key=lambda array: array[Ncol])
        else:
            self.dados = sorted(self.dados, key=lambda array: array[Ncol], reverse=True)
        self.layoutChanged.emit()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DataGridView(((1, 2, 3),(6, 5, 4)),('a', 'b', 'c'),True)
    w.show()
    sys.exit(app.exec_())