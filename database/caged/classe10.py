'''

'''

from database import db
import codecs


def txt2db(diretorio):
    
    #criando tabelas
    db.commit()
    db.query("DROP TABLE IF EXISTS CAGED.CLASSE10")
    db.query("""CREATE TABLE CAGED.CLASSE10(
    CO_CLASSE10 INT,
    CLASSE VARCHAR(200)
    )""")
    
    firstExec = True
    
    for linha in codecs.open(diretorio + "/CLASSE10.txt", "r", "latin-1"):
        
        dic = {}
        
        #leitura do arquivo
        dados = linha.split('\t')
        dic["co_classe10"] = int(dados[0])
        dic["classe"] = dados[1].strip("\n")
        
        db.latin2utf(dic)
        
        if firstExec:
            db.prepareInsert("CLASSE10", "CAGED.CLASSE10", dic)
            db.commit()
            firstExec = False
            
        db.usePreparedInsert("CLASSE10", dic)
        
    db.commit()