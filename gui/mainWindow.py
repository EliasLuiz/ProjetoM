from PyQt4 import QtGui

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Projeto M")
        
        self.show()