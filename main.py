#!/usr/bin/python
# -*- coding: latin -*-

from database import inep2012
#import gui
import sys

diretorio = "/media/elias/726F27DC62421D70/CEFET/Projeto Maurilio/microdados_educacao_superior_2012"

inep2012.carrega(diretorio)

sys.exit(0)