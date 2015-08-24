# -*- coding: latin -*-
'''
realiza a leitura do arquivo /DADOS/LOCAL_OFERTA.txt
cria uma tabela no banco e salva os dados lidos
'''

from database import db
import codecs

def txt2db(diretorio):
    
    #limpa/cria as tabelas a serem usadas
    db.commit()
    db.query("DROP TABLE IF EXISTS INEP2012.LOCAL_OFERTA")
    db.query("""CREATE TABLE INEP2012.LOCAL_OFERTA(
        CO_LOCAL_OFERTA INT,
        CO_IES INT,
        CO_MUNICIPIO INT,
        IN_SEDE BOOLEAN,
        CO_CURSO INT,
        IN_LOCAL_OFERTA_NEAD BOOLEAN,
        IN_LOCAL_OFERTA_UAB BOOLEAN,
        IN_LOCAL_OFERTA_REITORIA BOOLEAN,
        IN_LOCAL_OFERTA_POLO BOOLEAN,
        IN_LOCAL_OFERTA_UNID_ACADEMICA BOOLEAN);""")
        
    firstExec = True


    for linha in codecs.open(diretorio + "/LOCAL_OFERTA.txt", "r", 'latin-1'):

        dic = {}

        #LEITURA DO ARQUIVO
        dic['CO_LOCAL_OFERTA'] = linha[0:8]
        dic['CO_IES'] = linha[8:16]
        dic['CO_MUNICIPIO'] = linha[16:24]
        #dic['NO_MUNICIPIO_LOCAL_OFERTA'] = linha[24:174].strip()
        #dic['CO_UF_LOCAL_OFERTA'] = linha[174:182]
        #dic['SGL_UF_LOCAL_OFERTA'] = linha[182:184]
        dic['IN_SEDE'] = linha[184:192] == '       1' #transforma em bool
        #try:   #algumas linhas vem com o campo vazio
        #    dic['CO_CURSO_POLO'] = int(linha[192:200])
        #except:
        #    dic['CO_CURSO_POLO'] = None
        dic['CO_CURSO'] = linha[200:208]
        dic['IN_LOCAL_OFERTA_NEAD'] = linha[208:216] == '       1'
        dic['IN_LOCAL_OFERTA_UAB'] = linha[216:224] == '       1'
        dic['IN_LOCAL_OFERTA_REITORIA'] = linha[224:232] == '       1'
        dic['IN_LOCAL_OFERTA_POLO'] = linha[232:240] == '       1'
        dic['IN_LOCAL_OFERTA_UNID_ACADEMICA'] = linha[240:248] == '       1'
        
        
        
        #CONVERSAO DE LATIN-1 PARA UTF-8
        db.latin2utf(dic)
        
        
        
        #INSERCAO NO BANCO DE DADOS
        if firstExec:
            db.prepareInsert('LOCAL_OFERTA', 'INEP2012.LOCAL_OFERTA', dic)
            db.commit()
            firstExec = False
            
        db.usePreparedInsert('LOCAL_OFERTA', dic)



    db.commit()



        
'''
        try:
            db.query("""INSERT INTO INEP2012.LOCAL_OFERTA(CO_LOCAL_OFERTA_IES,CO_IES,
                CO_MUNICIPIO_LOCAL_OFERTA,IN_SEDE,CO_CURSO_POLO,CO_CURSO,IN_LOCAL_OFERTA_NEAD,IN_LOCAL_OFERTA_UAB,
                IN_LOCAL_OFERTA_REITORIA, IN_LOCAL_OFERTA_POLO,IN_LOCAL_OFERTA_UNID_ACADEMICA) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" % (dic['CO_LOCAL_OFERTA_IES'], \
                dic['CO_IES'], dic['CO_MUNICIPIO_LOCAL_OFERTA'], dic['IN_SEDE'], dic['CO_CURSO_POLO'], \
                dic['CO_CURSO'], dic['IN_LOCAL_OFERTA_NEAD'], dic['IN_LOCAL_OFERTA_UAB'], \
                dic['IN_LOCAL_OFERTA_REITORIA'], dic['IN_LOCAL_OFERTA_POLO'],\
                dic['IN_LOCAL_OFERTA_UNID_ACADEMICA']))
        except:
            None
=======
# -*- coding: latin -*-
'''
realiza a leitura do arquivo /DADOS/LOCAL_OFERTA.txt
cria uma tabela no banco e salva os dados lidos
'''

from database import db
import codecs

def txt2db(diretorio):
    
    #limpa/cria as tabelas a serem usadas
    db.commit()
    db.query("DROP TABLE IF EXISTS INEP2012.LOCAL_OFERTA")
    db.query("""CREATE TABLE INEP2012.LOCAL_OFERTA(
        CO_LOCAL_OFERTA INT,
        CO_IES INT,
        CO_MUNICIPIO INT,
        IN_SEDE BOOLEAN,
        CO_CURSO INT,
        IN_LOCAL_OFERTA_NEAD BOOLEAN,
        IN_LOCAL_OFERTA_UAB BOOLEAN,
        IN_LOCAL_OFERTA_REITORIA BOOLEAN,
        IN_LOCAL_OFERTA_POLO BOOLEAN,
        IN_LOCAL_OFERTA_UNID_ACADEMICA BOOLEAN);""")
        
    firstExec = True


    for linha in codecs.open(diretorio + "/LOCAL_OFERTA.txt", "r", 'latin-1'):

        dic = {}

        #LEITURA DO ARQUIVO
        dic['CO_LOCAL_OFERTA'] = linha[0:8]
        dic['CO_IES'] = linha[8:16]
        dic['CO_MUNICIPIO'] = linha[16:24]
        #dic['NO_MUNICIPIO_LOCAL_OFERTA'] = linha[24:174].strip()
        #dic['CO_UF_LOCAL_OFERTA'] = linha[174:182]
        #dic['SGL_UF_LOCAL_OFERTA'] = linha[182:184]
        dic['IN_SEDE'] = linha[184:192] == '       1' #transforma em bool
        #try:   #algumas linhas vem com o campo vazio
        #    dic['CO_CURSO_POLO'] = int(linha[192:200])
        #except:
        #    dic['CO_CURSO_POLO'] = None
        dic['CO_CURSO'] = linha[200:208]
        dic['IN_LOCAL_OFERTA_NEAD'] = linha[208:216] == '       1'
        dic['IN_LOCAL_OFERTA_UAB'] = linha[216:224] == '       1'
        dic['IN_LOCAL_OFERTA_REITORIA'] = linha[224:232] == '       1'
        dic['IN_LOCAL_OFERTA_POLO'] = linha[232:240] == '       1'
        dic['IN_LOCAL_OFERTA_UNID_ACADEMICA'] = linha[240:248] == '       1'
        
        
        
        #CONVERSAO DE LATIN-1 PARA UTF-8
        db.latin2utf(dic)
        
        
        
        #INSERCAO NO BANCO DE DADOS
        if firstExec:
            db.prepareInsert('LOCAL_OFERTA', 'INEP2012.LOCAL_OFERTA', dic)
            db.commit()
            firstExec = False
            
        db.usePreparedInsert('LOCAL_OFERTA', dic)



    db.commit()



        
'''
        try:
            db.query("""INSERT INTO INEP2012.LOCAL_OFERTA(CO_LOCAL_OFERTA_IES,CO_IES,
                CO_MUNICIPIO_LOCAL_OFERTA,IN_SEDE,CO_CURSO_POLO,CO_CURSO,IN_LOCAL_OFERTA_NEAD,IN_LOCAL_OFERTA_UAB,
                IN_LOCAL_OFERTA_REITORIA, IN_LOCAL_OFERTA_POLO,IN_LOCAL_OFERTA_UNID_ACADEMICA) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" % (dic['CO_LOCAL_OFERTA_IES'], \
                dic['CO_IES'], dic['CO_MUNICIPIO_LOCAL_OFERTA'], dic['IN_SEDE'], dic['CO_CURSO_POLO'], \
                dic['CO_CURSO'], dic['IN_LOCAL_OFERTA_NEAD'], dic['IN_LOCAL_OFERTA_UAB'], \
                dic['IN_LOCAL_OFERTA_REITORIA'], dic['IN_LOCAL_OFERTA_POLO'],\
                dic['IN_LOCAL_OFERTA_UNID_ACADEMICA']))
        except:
            None
>>>>>>> c73e324cd23f8a5131df6537b0fbfabe30dd85d6
'''