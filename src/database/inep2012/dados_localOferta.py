# realiza a leitura do arquivo /DADOS/LOCAL_OFERTA.txt
# cria uma tabela no banco e salva os dados lidos

from database import db

def txt_to_db(diretorio):
    
    #limpa/cria as tabelas a serem usadas
    db.query("DROP TABLE IF EXISTS INEP2012.MUNICIPIO")
    db.query("DROP TABLE IF EXISTS INEP2012.LOCAL_OFERTA")
    db.query("""CREATE TABLE INEP2012.MUNICIPIO(
        CO_MUNICIPIO INT PRIMARY KEY,
        NO_MUNICIPIO VARCHAR(150),
        CO_UF INT,
        SGL_UF CHAR(2));""")
    db.query("""CREATE TABLE INEP2012.LOCAL_OFERTA(
        CO_LOCAL_OFERTA_IES INT,
        CO_IES INT,
        CO_MUNICIPIO_LOCAL_OFERTA INT,
        IN_SEDE BOOLEAN,
        CO_CURSO_POLO INT,
        CO_CURSO INT,
        IN_LOCAL_OFERTA_NEAD BOOLEAN,
        IN_LOCAL_OFERTA_UAB BOOLEAN,
        IN_LOCAL_OFERTA_REITORIA BOOLEAN,
        IN_LOCAL_OFERTA_POLO BOOLEAN,
        IN_LOCAL_OFERTA_UNID_ACADEMICA BOOLEAN);""")


    file = open(diretorio + "/DADOS/LOCAL_OFERTA.txt", "r")

    for linha in file.readlines():

        dic = {}
        dic2 = {}

        #LEITURA DO ARQUIVO
        dic['CO_LOCAL_OFERTA_IES'] = linha[0:8]
        dic['CO_IES'] = linha[8:16]
        dic['CO_MUNICIPIO_LOCAL_OFERTA'] = dic2['CO_MUNICIPIO'] = linha[16:24]
        dic2['NO_MUNICIPIO'] = linha[24:174].strip()
        dic2['CO_UF'] = linha[174:182]
        dic2['SGL_UF'] = linha[182:184]
        dic['IN_SEDE'] = linha[184:192] == '       1' #transforma em bool
        try:   #algumas linhas vem com o campo vazio
            dic['CO_CURSO_POLO'] = linha[192:200]
        except:
            dic['CO_CURSO_POLO'] = ""
        dic['CO_CURSO'] = linha[200:208]
        dic['IN_LOCAL_OFERTA_NEAD'] = linha[208:216] == '       1'
        dic['IN_LOCAL_OFERTA_UAB'] = linha[216:224] == '       1'
        dic['IN_LOCAL_OFERTA_REITORIA'] = linha[224:232] == '       1'
        dic['IN_LOCAL_OFERTA_POLO'] = linha[232:240] == '       1'
        dic['IN_LOCAL_OFERTA_UNID_ACADEMICA'] = linha[240:248] == '       1'

        
        #INSERCAO NO BANCO DE DADOS
        try:
            db.query(db.sqlGenerator('INEP2012.LOCAL_OFERTA', dic))
        except:
            None
        try:
            '''
            db.query("""INSERT INTO INEP2012.MUNICIPIO(CO_MUNICIPIO,NO_MUNICIPIO,
                CO_UF,SGL_UF) VALUES(%s, '%s', %s, '%s')""" % (dic['CO_MUNICIPIO_LOCAL_OFERTA'], \
                dic['NO_MUNICIPIO_LOCAL_OFERTA'], dic['CO_UF_LOCAL_OFERTA'], dic['SGL_UF_LOCAL_OFERTA']))'''
            db.query(db.sqlGenerator('INEP2012.MUNICIPIO', dic2))
        except:
            None
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
        '''    

    file.close()
    
