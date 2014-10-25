#!/usr/bin/python

from database.inep2012 import dados_LocalOferta as localOferta

diretorio = raw_input("Pasta da base de dados: ")

localOferta.txt_to_db(diretorio)