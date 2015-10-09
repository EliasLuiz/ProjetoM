'''

'''

from database import db
import codecs


def txt2db(diretorio):
    
    #criando tabelas
    db.commit()
    db.query("DROP TABLE IF EXISTS CAGED.CLASSE20")
    db.query("""CREATE TABLE CAGED.CLASSE20(
    CO_CLASSE20 INT,
    CLASSE VARCHAR(200)
    )""")
    
    firstExec = True
    
    for linha in codecs.open(diretorio + "/CLASSE20.txt", "r", "latin-1"):
        
        dic = {}
        
        #leitura do arquivo
        dados = linha.split('\t')
        dic["co_classe20"] = int(dados[0])
        dic["classe"] = dados[1].strip("\n")
        
        db.latin2utf(dic)
        
        if firstExec:
            db.prepareInsert("CLASSE20", "CAGED.CLASSE20", dic)
            db.commit()
            firstExec = False
            
        db.usePreparedInsert("CLASSE20", dic)
        
    db.commit()