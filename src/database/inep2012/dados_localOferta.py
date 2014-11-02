# realiza a leitura do arquivo /DADOS/LOCAL_OFERTA.txt
# cria uma tabela no banco e salva os dados lidos

from database import db

def txt_to_db(diretorio):
    
    #limpa/cria as tabelas a serem usadas
    db.query("DROP TABLE IF EXISTS INEP2012.MUNICIPIO")
    db.query("DROP TABLE IF EXISTS INEP2012.LOCAL_OFERTA")
    db.query("""CREATE TABLE INEP2012.MUNICIPIO(
CO_MUNICIPIO_LOCAL_OFERTA int PRIMARY KEY,
NO_MUNICIPIO_LOCAL_OFERTA varchar(150), \
CO_UF_LOCAL_OFERTA int,
SGL_UF_LOCAL_OFERTA char(2));""")


    file = open(diretorio + "/DADOS/LOCAL_OFERTA.txt", "r")

    for linha in file.readlines():

        dic = {}

        #LEITURA DO ARQUIVO
        dic['CO_LOCAL_OFERTA_IES'] = int(linha[0:8])
        dic['CO_IES'] = int(linha[8:16])
        dic['CO_MUNICIPIO_LOCAL_OFERTA'] = int(linha[16:24])
        dic['NO_MUNICIPIO_LOCAL_OFERTA'] = linha[24:174].strip()
        dic['CO_UF_LOCAL_OFERTA'] = int(linha[174:182])
        dic['SGL_UF_LOCAL_OFERTA'] = linha[182:184]
        dic['IN_SEDE'] = linha[184:192] == '       1' #transforma em bool
        try:   #algumas linhas vem com o campo vazio
            dic['CO_CURSO_POLO'] = int(linha[192:200])
        except:
            dic['CO_CURSO_POLO'] = ""
        dic['CO_CURSO'] = int(linha[200:208])
        dic['IN_LOCAL_OFERTA_NEAD'] = linha[208:216] == '       1'
        dic['IN_LOCAL_OFERTA_UAB'] = linha[216:224] == '       1'
        dic['IN_LOCAL_OFERTA_REITORIA'] = linha[224:232] == '       1'
        dic['IN_LOCAL_OFERTA_POLO'] = linha[232:240] == '       1'
        dic['IN_LOCAL_OFERTA_UNID_ACADEMICA'] = linha[240:248] == '       1'
    
        #INSERCAO NO BANCO DE DADOS
        sqlMunicipio = "INSERT INTO INEP2012.MUNICIPIO(CO_MUNICIPIO_LOCAL_OFERTA,NO_MUNICIPIO_LOCAL_OFERTA, \
CO_UF_LOCAL_OFERTA,SGL_UF_LOCAL_OFERTA) VALUES(%s, '%s', %s, '%s')" % (dic['CO_MUNICIPIO_LOCAL_OFERTA'], \
dic['NO_MUNICIPIO_LOCAL_OFERTA'], dic['CO_UF_LOCAL_OFERTA'], dic['SGL_UF_LOCAL_OFERTA'])
        db.query(sqlMunicipio)
        '''
        sqlLocalOferta="INSERT INTO LOCAL_OFERTA(CO_LOCAL_OFERTA_IES,CO_IES,CO_MUNICIPIO_LOCAL_OFERTA, \
IN_SEDE,CO_CURSO_POLO,CO_CURSO,IN_LOCAL_OFERTA_NEAD,IN_LOCAL_OFERTA_UAB,IN_LOCAL_OFERTA_REITORIA, \
IN_LOCAL_OFERTA_POLO,IN_LOCAL_OFERTA_UNID_ACADEMICA) " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % \
(dic['CO_LOCAL_OFERTA_IES'], dic['CO_IES'], dic['CO_MUNICIPIO_LOCAL_OFERTA'], dic['IN_SEDE'],  \
dic['CO_CURSO_POLO'], dic['CO_CURSO'], dic['IN_LOCAL_OFERTA_NEAD'], dic['IN_LOCAL_OFERTA_UAB'], \
dic['IN_LOCAL_OFERTA_REITORIA'], dic['IN_LOCAL_OFERTA_POLO'], dic['IN_LOCAL_OFERTA_UNID_ACADEMICA'])
        print sqlLocalOferta
        '''

    file.close()
    
