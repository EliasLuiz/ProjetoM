# -*- coding: latin -*-

import os
from database import db
from database.caged import cbo2002
from database.caged import classe10
from database.caged import classe20
from database.caged import municipio
from database.caged import subclasse
from database.caged import dados

def carrega(arquivo):
    
    db.query("CREATE SCHEMA IF NOT EXISTS CAGED")
    
    #Caso nao haja tabelas sao carrega as tabelas auxiliares
    if len(db.buscaTabelas("CAGED")) < 5:
        caminhoBase = os.path.dirname(os.path.realpath(__file__))  
        cbo2002.txt2db(caminhoBase)
        classe10.txt2db(caminhoBase)
        classe20.txt2db(caminhoBase)
        municipio.txt2db(caminhoBase)
        subclasse.txt2db(caminhoBase)
    
    dados.txt2db(arquivo)