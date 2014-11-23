#!/usr/bin/python
# -.- coding:latin -.-

from database import db
'''
import sys

diretorio = raw_input("Pasta da base de dados: ")
#diretorio = "/media/elias/4DF85F7166976ABF/CEFET/Projeto Maurilio/microdados_educacao_superior_2012"

db.carregaINEP2012(diretorio)

sys.exit(0)
'''

res = db.sqlSelectGeneratorSearchFilter(tabelas=['inep2012.curso'], camposDeBusca=[('in_gratuito',True)],
        camposDeFiltro=[('no_curso', 'CIÊNCIA % COMPUTAÇÃO'), ('no_curso', 'ENGENHARIA % COMPUTAÇÃO')])
for i in res:
    print i
print len(res)