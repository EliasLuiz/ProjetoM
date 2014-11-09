#!/usr/bin/python

from database.inep2012 import dados_localOferta as localOferta
from database.inep2012 import dados_instituicao as ies
from database.inep2012 import dados_curso as curso
from database.inep2012 import dados_aluno as aluno
from database.inep2012 import dados_docente as docente
import sys

diretorio = raw_input("Pasta da base de dados: ")

ies.txt2db(diretorio)
localOferta.txt2db(diretorio)
curso.txt2db(diretorio)
docente.txt2db(diretorio)
aluno.txt2db(diretorio)

sys.exit(0)
