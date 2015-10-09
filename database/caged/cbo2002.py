'''

'''

from database import db
import codecs


def txt2db(diretorio):
    
    #criando tabelas
    db.commit()
    db.query("DROP TABLE IF EXISTS CAGED.CBO2002")
    db.query("""CREATE TABLE CAGED.CBO2002(
    CO_CBO2002 INT,
    CLASSE VARCHAR(150)
    )""")
    
    firstExec = True
    
    for linha in codecs.open(diretorio + "/CBO2002.txt", "r", "latin-1"):
        
        dic = {}
        
        #leitura do arquivo
        dados = linha.split('\t')
        dic["co_cbo2002"] = int(dados[0])
        dic["classe"] = dados[1].strip("\n")
        
        db.latin2utf(dic)
        
        if firstExec:
            db.prepareInsert("CBO2002", "CAGED.CBO2002", dic)
            db.commit()
            firstExec = False
            
        db.usePreparedInsert("CBO2002", dic)
        
    db.commit()