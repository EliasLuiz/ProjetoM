#!/usr/bin/python
# -*- coding: latin -*-
from PyQt4 import QtGui
from database import inep2012
from database import db
from gui import dataGridView
#import gui
import sys

#diretorio = "/media/elias/726F27DC62421D70/CEFET/Projeto Maurilio/microdados_educacao_superior_2012"
#inep2012.carrega(diretorio)

app = QtGui.QApplication(sys.argv)
w = dataGridView.DataGridView([['']],None)
w.show()
sys.exit(app.exec_())

sys.exit(0)