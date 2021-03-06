# -*- coding: latin -*-
'''
realiza a leitura do arquivo /DADOS/INSTITUICAO.txt
cria duas tabela no banco e salva os dados lidos,
    uma para instituição e outra para município
'''

from database import db
import codecs

def txt2db(diretorio):
    
    db.commit()
    db.pgAutoCommit(False)
    db.query("DROP TABLE IF EXISTS INEP2012.MUNICIPIO")
    db.query("DROP TABLE IF EXISTS INEP2012.IES")
    db.query("""CREATE TABLE INEP2012.MUNICIPIO(
        CO_MUNICIPIO INT,
        NO_MUNICIPIO VARCHAR(150),
        CO_UF INT,
        SGL_UF CHAR(2),
        NO_REGIAO VARCHAR(30), 
        IN_CAPITAL BOOLEAN);""")
    db.query("""CREATE TABLE INEP2012.IES(
        CO_IES INT, 
        NO_IES VARCHAR(200), 
        CO_MANTENEDORA INT, 
        CO_CATEGORIA_ADMINISTRATIVA INT, 
        DS_CATEGORIA_ADMINISTRATIVA VARCHAR(100), 
        CO_ORGANIZACAO_ACADEMICA INT, 
        DS_ORGANIZACAO_ACADEMICA VARCHAR(100), 
        CO_MUNICIPIO_IES INT, 
        QT_TEC_TOTAL INT, 
        QT_TEC_FUND_INCOMP_MASC INT, 
        QT_TEC_FUND_INCOMP_FEM INT, 
        QT_TEC_FUND_COMP_MASC INT, 
        QT_TEC_FUND_COMP_FEM INT, 
        QT_TEC_MEDIO_MASC INT, 
        QT_TEC_MEDIO_FEM INT, 
        QT_TEC_SUPERIOR_MASC INT, 
        QT_TEC_SUPERIOR_FEM INT, 
        QT_TEC_ESPECIALIZACAO_MASC INT, 
        QT_TEC_ESPECIALIZACAO_FEM INT, 
        QT_TEC_MESTRADO_MASC INT, 
        QT_TEC_MESTRADO_FEM INT, 
        QT_TEC_DOUTORADO_MASC INT, 
        QT_TEC_DOUTORADO_FEM INT, 
        IN_ACESSO_PORTAL_CAPES BOOLEAN, 
        IN_ACESSO_OUTRAS_BASES BOOLEAN, 
        IN_REFERENTE INT, 
        VL_RECEITA_PROPRIA DECIMAL(14,2), 
        VL_TRANSFERENCIA DECIMAL(14,2), 
        VL_OUTRA_RECEITA DECIMAL(14,2), 
        VL_DES_PESSOAL_REM_DOCENTE DECIMAL(14,2), 
        VL_DES_PESSOAL_REM_TECNICO DECIMAL(14,2), 
        VL_DES_PESSOAL_ENCARGO DECIMAL(14,2), 
        VL_DES_CUSTEIO DECIMAL(14,2), 
        VL_DES_INVESTIMENTO DECIMAL(14,2), 
        VL_DES_PESQUISA DECIMAL(14,2), 
        VL_DES_OUTRAS DECIMAL(14,2));""")
        
        
    firstExec = True
    
    
    for linha in codecs.open(diretorio + "/INSTITUICAO.txt", "r", 'latin-1'):
        
        dic = {}
        dic2 = {}
        
        #LEITURA DO ARQUIVO
        dic['CO_IES'] = linha[0:8]
        dic['NO_IES'] = linha[8:208].strip()
        dic['CO_MANTENEDORA'] = linha[208:216]
        dic['CO_CATEGORIA_ADMINISTRATIVA'] = linha[216:224]
        dic['DS_CATEGORIA_ADMINISTRATIVA'] = linha[224:324].strip()
        dic['CO_ORGANIZACAO_ACADEMICA'] = linha[324:332]
        dic['DS_ORGANIZACAO_ACADEMICA'] = linha[332:432].strip()
        #dic2['CO_MUNICIPIO_IES'] = dic['CO_MUNICIPIO'] = linha[432:440]
        dic2['CO_MUNICIPIO'] = linha[432:440]
        dic2['NO_MUNICIPIO'] = linha[440:590].strip()
        dic2['CO_UF'] = linha[590:598]
        dic2['SGL_UF'] = linha[598:600].strip()
        dic2['NO_REGIAO'] = linha[600:630].strip()
        dic2['IN_CAPITAL'] = linha[630:638] == '       1'
        dic['QT_TEC_TOTAL'] = linha[638:646]
        dic['QT_TEC_FUND_INCOMP_MASC'] = linha[646:654]
        dic['QT_TEC_FUND_INCOMP_FEM'] = linha[654:662]
        dic['QT_TEC_FUND_COMP_MASC'] = linha[662:670]
        dic['QT_TEC_FUND_COMP_FEM'] = linha[670:678]
        dic['QT_TEC_MEDIO_MASC'] = linha[678:686]
        dic['QT_TEC_MEDIO_FEM'] = linha[686:694]
        dic['QT_TEC_SUPERIOR_MASC'] = linha[694:702]
        dic['QT_TEC_SUPERIOR_FEM'] = linha[702:710]
        dic['QT_TEC_ESPECIALIZACAO_MASC'] = linha[710:718]
        dic['QT_TEC_ESPECIALIZACAO_FEM'] = linha[718:726]
        dic['QT_TEC_MESTRADO_MASC'] = linha[726:734]
        dic['QT_TEC_MESTRADO_FEM'] = linha[734:742]
        dic['QT_TEC_DOUTORADO_MASC'] = linha[742:750]
        dic['QT_TEC_DOUTORADO_FEM'] = linha[750:758]
        dic['IN_ACESSO_PORTAL_CAPES'] = linha[758:766] == '       1'
        dic['IN_ACESSO_OUTRAS_BASES'] = linha[766:774] == '       1'
        dic['IN_REFERENTE'] = linha[774:782]
        dic['VL_RECEITA_PROPRIA'] = float(linha[782:796])
        dic['VL_TRANSFERENCIA'] = float(linha[796:810])
        dic['VL_OUTRA_RECEITA'] = float(linha[810:824])
        dic['VL_DES_PESSOAL_REM_DOCENTE'] = float(linha[824:838])
        dic['VL_DES_PESSOAL_REM_TECNICO'] = float(linha[838:852])
        dic['VL_DES_PESSOAL_ENCARGO'] = float(linha[852:866])
        dic['VL_DES_CUSTEIO'] = float(linha[866:880])
        dic['VL_DES_INVESTIMENTO'] = float(linha[880:894])
        dic['VL_DES_PESQUISA'] = float(linha[894:908])
        dic['VL_DES_OUTRAS'] = float(linha[908:922])
        
        
        
        #CONVERSAO DE LATIN-1 PARA UTF-8
        db.latin2utf(dic)
        db.latin2utf(dic2)
        
        
        
        #INSERCAO NO BANCO DE DADOS
        if firstExec:
            db.prepareInsert('IES', 'INEP2012.IES', dic)
            db.prepareInsert('MUNICIPIO', 'INEP2012.MUNICIPIO', dic2)
            db.commit()
            firstExec = False
            
        db.usePreparedInsert('IES', dic)
        try:
            db.usePreparedInsert('MUNICIPIO', dic2)
        except:
            None
        
    db.commit()
    
    #retira as cidades repetidas
    db.query('''
    CREATE TABLE INEP2012.tmp as SELECT DISTINCT * FROM INEP2012.MUNICIPIO;
    DROP TABLE INEP2012.MUNICIPIO;
    ALTER TABLE INEP2012.tmp RENAME TO MUNICIPIO;''')
    
    db.commit()






'''
            db.query("""INSERT INTO INEP2012.MUNICIPIO(CO_MUNICIPIO,NO_MUNICIPIO,
                CO_UF,SGL_UF) VALUES(%s, '%s', %s, '%s')""" % (dic['CO_MUNICIPIO_LOCAL_OFERTA'], \
                dic['NO_MUNICIPIO_LOCAL_OFERTA'], dic['CO_UF_LOCAL_OFERTA'], dic['SGL_UF_LOCAL_OFERTA'])
'''
'''
        sqlMunicipio = "INSERT INTO MUNICIPIO(CO_MUNICIPIO,NO_MUNICIPIO,CO_UF,SGL_UF)"
        sqlMunicipio2 = " VALUES(%s,%s,%s,%s)" % (dic['CO_MUNICIPIO_IES'], dic['NO_MUNICIPIO_IES'], \
                dic['CO_UF_IES'], dic['SGL_UF_IES'])
        sqlMunicipio = sqlMunicipio + sqlMunicipio2
        #db.query(sqlMunicipio)
        
        
        sqlIES = "INSERT INTO IES(CO_IES, NO_IES, CO_MANTENEDORA, CO_CATEGORIA_ADMINISTRATIVA, \
                DS_CATEGORIA_ADMINISTRATIVA, CO_ORGANIZACAO_ACADEMICA, DS_ORGANIZACAO_ACADEMICA, \
                CO_MUNICIPIO_IES, NO_REGIAO_IES, IN_CAPITAL_IES, QT_TEC_TOTAL, QT_TEC_FUND_INCOMP_MASC, \
                QT_TEC_FUND_INCOMP_FEM, QT_TEC_FUND_COMP_MASC, QT_TEC_FUND_COMP_FEM, QT_TEC_MEDIO_MASC, \
                QT_TEC_MEDIO_FEM, QT_TEC_SUPERIOR_MASC, QT_TEC_SUPERIOR_FEM, QT_TEC_ESPECIALIZACAO_MASC, \
                QT_TEC_ESPECIALIZACAO_FEM, QT_TEC_MESTRADO_MASC, QT_TEC_MESTRADO_FEM, QT_TEC_DOUTORADO_MASC, \
                QT_TEC_DOUTORADO_FEM, IN_ACESSO_PORTAL_CAPES, IN_ACESSO_OUTRAS_BASES, IN_REFERENTE, \
                VL_RECEITA_PROPRIA, VL_TRANSFERENCIA, VL_OUTRA_RECEITA, VL_DES_PESSOAL_REM_DOCENTE, \
                VL_DES_PESSOAL_REM_TECNICO, VL_DES_PESSOAL_ENCARGO, VL_DES_CUSTEIO, VL_DES_INVESTIMENTO, \
                VL_DES_PESQUISA, VL_DES_OUTRAS) "
        sqlIES += "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (dic['CO_IES'], \
                dic['NO_IES'], dic['CO_MANTENEDORA'], dic['CO_CATEGORIA_ADMINISTRATIVA'], \
                dic['DS_CATEGORIA_ADMINISTRATIVA'], dic['CO_ORGANIZACAO_ACADEMICA'], \
                dic['DS_ORGANIZACAO_ACADEMICA'], dic['CO_MUNICIPIO_IES'], dic['NO_REGIAO_IES'], \
                dic['IN_CAPITAL_IES'], dic['QT_TEC_TOTAL'], dic['QT_TEC_FUND_INCOMP_MASC'], \
                dic['QT_TEC_FUND_INCOMP_FEM'], dic['QT_TEC_FUND_COMP_MASC'], dic['QT_TEC_FUND_COMP_FEM'], \
                dic['QT_TEC_MEDIO_MASC'], dic['QT_TEC_MEDIO_FEM'], dic['QT_TEC_SUPERIOR_MASC'], \
                dic['QT_TEC_SUPERIOR_FEM'], dic['QT_TEC_ESPECIALIZACAO_MASC'], dic['QT_TEC_ESPECIALIZACAO_FEM'], \
                dic['QT_TEC_MESTRADO_MASC'], dic['QT_TEC_MESTRADO_FEM'], dic['QT_TEC_DOUTORADO_MASC'], \
                dic['QT_TEC_DOUTORADO_FEM'], dic['IN_ACESSO_PORTAL_CAPES'], dic['IN_ACESSO_OUTRAS_BASES'], \
                dic['IN_REFERENTE'], dic['VL_RECEITA_PROPRIA'], dic['VL_TRANSFERENCIA'], \
                dic['VL_OUTRA_RECEITA'], dic['VL_DES_PESSOAL_REM_DOCENTE'], dic['VL_DES_PESSOAL_REM_TECNICO'], \
                dic['VL_DES_PESSOAL_ENCARGO'], dic['VL_DES_CUSTEIO'], dic['VL_DES_INVESTIMENTO'], \
                dic['VL_DES_PESQUISA'], dic['VL_DES_OUTRAS'])
        print sqlIES
        #db.query(sqlIES)
'''