#!/usr/bin/python

from database.inep2012 import dados_localOferta as localOferta
from database.inep2012 import dados_instituicao as ies
from database.inep2012 import dados_curso as curso
from database.inep2012 import dados_aluno as aluno
from database.inep2012 import dados_docente as docente
import sys

#diretorio = raw_input("Pasta da base de dados: ")

#localOferta.txt_to_db(diretorio)

localOferta.txt_to_db('/media/elias/4DF85F7166976ABF/CEFET/Projeto Maurilio/microdados_educacao_superior_2012')
ies.txt_to_db('/media/elias/4DF85F7166976ABF/CEFET/Projeto Maurilio/microdados_educacao_superior_2012')
curso.txt_to_db('/media/elias/4DF85F7166976ABF/CEFET/Projeto Maurilio/microdados_educacao_superior_2012')
docente.txt_to_db('/media/elias/4DF85F7166976ABF/CEFET/Projeto Maurilio/microdados_educacao_superior_2012')
aluno.txt_to_db('/media/elias/4DF85F7166976ABF/CEFET/Projeto Maurilio/microdados_educacao_superior_2012')

sys.exit(0)