'''

'''

from database import db
import codecs


def txt2db(diretorio):
    
    #criando tabelas
    db.commit()
    db.query("DROP TABLE IF EXISTS CAGED.MUNICIPIO")
    db.query("""CREATE TABLE CAGED.MUNICIPIO(
    CO_MUNICIPIO INT,
    UF CHAR(2),
    MUNICIPIO VARCHAR(40)
    )""")
    
    firstExec = True
    
    for linha in codecs.open(diretorio + "/municipio.txt", "r", "latin-1"):
        
        dic = {}
        
        dados = linha.split('\t')
        #LEITURA DO ARQUIVO
        dic["co_municipio"] = int(dados[0])
        dic["uf"] = dados[1]
        dic["municipio"] = dados[2].strip("\n")
        
        db.latin2utf(dic)
        
        if firstExec:
            db.prepareInsert("MUNICIPIO", "CAGED.MUNICIPIO", dic)
            db.commit()
            firstExec = False
            
        db.usePreparedInsert("MUNICIPIO", dic)
        
    db.commit()