# -*- coding: latin -*-

from database import db

def carrega(diretorio):
    db.query("CREATE SCHEMA IF NOT EXISTS INEP2012")
    from database.inep2012 import dados_localOferta as localOferta
    from database.inep2012 import dados_instituicao as ies
    from database.inep2012 import dados_curso as curso
    from database.inep2012 import dados_aluno as aluno
    from database.inep2012 import dados_docente as docente
    ies.txt2db(diretorio)
    localOferta.txt2db(diretorio)
    '''
    curso nao pode NUNCA, em hipotese ALGUMA, ser inserido antes
        de local oferta
        Motivo: curso faz gambiarra pra reestruturar a base
        do governo que precisa de local oferta no lugar
    '''
    curso.txt2db(diretorio)
    docente.txt2db(diretorio)
    aluno.txt2db(diretorio)
    