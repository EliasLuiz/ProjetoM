'''

'''

from database import db
import codecs


def txt2db(diretorio):
    
    #criando tabelas
    db.commit()
    db.query("DROP TABLE IF EXISTS CAGED.SUBCLASSE")
    db.query("""CREATE TABLE CAGED.SUBCLASSE(
    CO_SUBCLASSE INT,
    CLASSE VARCHAR(160)
    )""")
    
    firstExec = True
    
    for linha in codecs.open(diretorio + "/SUBCLASSE.txt", "r", "latin-1"):
        
        dic = {}
        
        #leitura do arquivo
        dados = linha.split('\t')
        dic["co_subclasse"] = int(dados[0])
        dic["classe"] = dados[1]
        
        db.latin2utf(dic)
        
        if firstExec:
            db.prepareInsert("SUBCLASSE", "CAGED.SUBCLASSE", dic)
            db.commit()
            firstExec = False
            
        db.usePreparedInsert("SUBCLASSE", dic)
        
    db.commit()