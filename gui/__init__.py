from PyQt4 import QtGui
import sys
from database import db

from gui import inep2012

app = QtGui.QApplication(sys.argv)

aux = inep2012.MainWindow()
aux.show()

sys.exit(app.exec_())