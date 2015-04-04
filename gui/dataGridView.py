#-*- coding: latin -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

'''
EDIT+SORT=BUG
'''

class DataGridView(QWidget):
    def __init__(self, dados, cabecalho=None, titulo=None, editavel=False):
        super(DataGridView, self).__init__()

        # cria a tabela
        self.table = QTableView()

        # seta a tabela
        if editavel:
            self.table.setModel(MyTableModel(
                    [list(i) for i in dados], list(cabecalho), editavel, self))
        else:
            self.table.setModel(MyTableModel(dados, cabecalho, editavel, self))

        # propriedades do grid
        self.table.setShowGrid(True)

        # ajuste do cabecalho vertical
        vh = self.table.verticalHeader()
        vh.setVisible(False)

        # ajuste do cabecalho horizontal
        hh = self.table.horizontalHeader()
        if cabecalho == None:
            hh.setVisible(False)
        #hh.setStretchLastSection(True)

        # ajusta celulas ao conteudo
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()

        # habilita ordenacao
        self.table.setSortingEnabled(True)
        
        if titulo != None:
            self.setWindowTitle(titulo)
        
        # layout
        self.layout = QVBoxLayout()        

        self.layout.addWidget(self.table)
        self.setLayout(self.layout)
        
        
        self.show()
        

class MyTableModel(QAbstractTableModel):
    def __init__(self, dados, cabecalho=None, editavel=False, parent=None):
        """
        Args:
            dados: lista de listas
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
        if self.dados!=None and len(self.dados) > 0: 
            return len(self.dados[0]) 
        return 0
    
    
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant((str(self.dados[index.row()][index.column()])).decode('utf-8'))


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
        if self.cabecalho != None and orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if isinstance(self.cabecalho, str):
                return QVariant(self.cabecalho)
            else:
                return QVariant(self.cabecalho[col])
        return QVariant()


    def sort(self, Ncol, order):
        self.layoutAboutToBeChanged.emit()       
        if order == Qt.AscendingOrder:
            self.dados = sorted(self.dados, key=lambda array: array[Ncol])
        else:
            self.dados = sorted(self.dados, key=lambda array: array[Ncol], reverse=True)
        self.layoutChanged.emit()
        