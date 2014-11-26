from PyQt4 import QtGui
import sys
import mainWindow as mw

app = QtGui.QApplication(sys.argv)

win = mw.MainWindow()

sys.exit(app.exec_())