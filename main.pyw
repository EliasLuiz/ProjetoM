#!/usr/bin/python
# -*- coding: latin -*-

from PyQt4 import QtGui
from gui import mainWindow
import sys

def main():
    app = QtGui.QApplication(sys.argv)
    w = mainWindow.MainWindow()
    w.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()