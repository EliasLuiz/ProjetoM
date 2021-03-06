'''
realiza a leitura do arquivo /DADOS/CURSO.txt
cria uma tabela no banco e salva os dados lidos
'''

from database import db
import codecs

def txt2db(diretorio):
    
    db.commit()
    db.query("DROP TABLE IF EXISTS INEP2012.CURSO")
    db.query("""CREATE TABLE INEP2012.CURSO(
        CO_IES INT,
        CO_MUNICIPIO INT,
        CO_LOCAL_OFERTA INT,
        CO_CURSO INT,
        NO_CURSO VARCHAR(200),
        CO_OCDE VARCHAR(12),
        NO_OCDE VARCHAR(120),
        CO_OCDE_AREA_GERAL VARCHAR(12),
        NO_OCDE_AREA_GERAL VARCHAR(120),
        CO_OCDE_AREA_ESPECIFICA VARCHAR(12),
        NO_OCDE_AREA_ESPECIFICA VARCHAR(120),
        CO_OCDE_AREA_DETALHADA VARCHAR(12),
        NO_OCDE_AREA_DETALHADA VARCHAR(120),
        CO_GRAU_ACADEMICO INT,
        DS_GRAU_ACADEMICO VARCHAR(12),
        CO_MODALIDADE_ENSINO INT,
        DS_MODALIDADE_ENSINO VARCHAR(11),
        CO_NIVEL_ACADEMICO INT,
        DS_NIVEL_ACADEMICO VARCHAR(33),
        IN_GRATUITO BOOLEAN,
        TP_ATRIBUTO_INGRESSO INT,
        NU_CARGA_HORARIA INT,
        DT_INICIO_FUNCIONAMENTO VARCHAR(38),
        DT_AUTORIZACAO_CURSO VARCHAR(38),
        IN_AJUDA_DEFICIENTE BOOLEAN,
        IN_MATERIAL_DIGITAL BOOLEAN,
        IN_MATERIAL_AMPLIADO BOOLEAN,
        IN_MATERIAL_TATIL BOOLEAN,
        IN_MATERIAL_IMPRESSO BOOLEAN,
        IN_MATERIAL_AUDIO BOOLEAN,
        IN_MATERIAL_BRAILLE BOOLEAN,
        IN_DISCIPLINA_LIBRAS BOOLEAN,
        IN_GUIA_INTERPRETE BOOLEAN,
        IN_MATERIAL_LIBRAS BOOLEAN,
        IN_RECURSOS_COMUNICACAO BOOLEAN,
        IN_RECURSOS_INFORMATICA BOOLEAN,
        IN_TRADUTOR_LIBRAS BOOLEAN,
        IN_INTEGRAL_CURSO BOOLEAN,
        IN_MATUTINO_CURSO BOOLEAN,
        IN_NOTURNO_CURSO BOOLEAN,
        IN_VESPERTINO_CURSO BOOLEAN,
        NU_PERC_CARGA_HOR_DISTANCIA DECIMAL(8,4),
        NU_INTEGRALIZACAO_MATUTINO DECIMAL(8,1),
        NU_INTEGRALIZACAO_VESPERTINO DECIMAL(8,1),
        NU_INTEGRALIZACAO_NOTURNO DECIMAL(8,1),
        NU_INTEGRALIZACAO_INTEGRAL DECIMAL(8,1),
        NU_INTEGRALIZACAO_EAD DECIMAL(8,1),
        QT_INSCRITOS_ANO_EAD INT,
        QT_VAGAS_ANUAL_EAD INT,
        QT_VAGAS_INTEGRAL_PRES INT,
        QT_VAGAS_MATUTINO_PRES INT,
        QT_VAGAS_VESPERTINO_PRES INT,
        QT_VAGAS_NOTURNO_PRES INT,
        QT_INSCRITOS_MATUTINO_PRES INT,
        QT_INSCRITOS_VESPERTINO_PRES INT,
        QT_INSCRITOS_NOTURNO_PRES INT,
        QT_INSCRITOS_INTEGRAL_PRES INT,
        QT_MATRICULA_CURSO INT,
        QT_CONCLUINTE_CURSO INT,
        QT_INGRESSO_CURSO INT,
        QT_INGRESSO_PROCESSO_SELETIVO INT,
        QT_INGRESSO_OUTRA_FORMA INT);""")
        
        
    firstExec = True


    for linha in codecs.open(diretorio + "/CURSO.txt", "r", 'latin-1'):

        dic = {}
        
        
        #LEITURA DO ARQUIVO
        ############### DADOS DA IES ################
        dic['CO_IES'] = linha[0:8]
        #dic['NO_IES'] = linha[8:208].strip()
        #dic['CO_CATEGORIA_ADMINISTRATIVA'] = linha[208:216]
        #dic['DS_CATEGORIA_ADMINISTRATIVA'] = linha[216:316].strip()
        #dic['CO_ORGANIZACAO_ACADEMICA'] = linha[316:324]
        #dic['DS_ORGANIZACAO_ACADEMICA'] = linha[324:424].strip()
        ############### DADOS DO CURSO ################
        try:
            dic['CO_MUNICIPIO'] = int(linha[424:432])
        except:
            dic['CO_MUNICIPIO'] = None
        #dic['NO_MUNICIPIO_CURSO'] = linha[432:582].strip()
        #dic['CO_UF_CURSO'] = linha[582:590]
        #dic['SGL_UF_CURSO'] = linha[590:592]
        #dic['NO_REGIAO_CURSO'] = linha[592:622].strip()
        #dic['IN_CAPITAL_CURSO'] = linha[622:630] == '       1'
        dic['CO_CURSO'] = linha[630:638]
        dic['NO_CURSO'] = linha[638:838].strip()
        dic['CO_OCDE'] = linha[838:850].strip()
        dic['NO_OCDE'] = linha[850:970].strip()
        dic['CO_OCDE_AREA_GERAL'] = linha[970:982].strip()
        dic['NO_OCDE_AREA_GERAL'] = linha[982:1102].strip()
        dic['CO_OCDE_AREA_ESPECIFICA'] = linha[1102:1114].strip()
        dic['NO_OCDE_AREA_ESPECIFICA'] = linha[1114:1234].strip()
        dic['CO_OCDE_AREA_DETALHADA'] = linha[1234:1246].strip()
        dic['NO_OCDE_AREA_DETALHADA'] = linha[1246:1366].strip()
        try:
            dic['CO_GRAU_ACADEMICO'] = int(linha[1366:1374])
        except:
            dic['CO_GRAU_ACADEMICO'] = None
        dic['DS_GRAU_ACADEMICO'] = linha[1374:1386].strip()
        dic['CO_MODALIDADE_ENSINO'] = linha[1386:1394]
        dic['DS_MODALIDADE_ENSINO'] = linha[1394:1405].strip()
        dic['CO_NIVEL_ACADEMICO'] = linha[1405:1413]
        dic['DS_NIVEL_ACADEMICO'] = linha[1413:1446].strip()
        dic['IN_GRATUITO'] = linha[1446:1454] == '       1'
        dic['TP_ATRIBUTO_INGRESSO'] = linha[1454:1462]
        dic['NU_CARGA_HORARIA'] = linha[1470:1478]
        dic['DT_INICIO_FUNCIONAMENTO'] = linha[1478:1516]
        dic['DT_AUTORIZACAO_CURSO'] = linha[1516:1554]
        dic['IN_AJUDA_DEFICIENTE'] = linha[1554:1562] == '       1'
        dic['IN_MATERIAL_DIGITAL'] = linha[1562:1570] == '       1'
        dic['IN_MATERIAL_AMPLIADO'] = linha[1570:1578] == '       1'
        dic['IN_MATERIAL_TATIL'] = linha[1578:1586] == '       1'
        dic['IN_MATERIAL_IMPRESSO'] = linha[1586:1594] == '       1'
        dic['IN_MATERIAL_AUDIO'] = linha[1594:1602] == '       1'
        dic['IN_MATERIAL_BRAILLE'] = linha[1602:1610] == '       1'
        dic['IN_DISCIPLINA_LIBRAS'] = linha[1610:1618] == '       1'
        dic['IN_GUIA_INTERPRETE'] = linha[1618:1626] == '       1'
        dic['IN_MATERIAL_LIBRAS'] = linha[1626:1634] == '       1'
        dic['IN_RECURSOS_COMUNICACAO'] = linha[1634:1642] == '       1'
        dic['IN_RECURSOS_INFORMATICA'] = linha[1642:1650] == '       1'
        dic['IN_TRADUTOR_LIBRAS'] = linha[1650:1658] == '       1'
        dic['IN_INTEGRAL_CURSO'] = linha[1658:1666] == '       1'
        dic['IN_MATUTINO_CURSO'] = linha[1666:1674] == '       1'
        dic['IN_NOTURNO_CURSO'] = linha[1674:1682] == '       1'
        dic['IN_VESPERTINO_CURSO'] = linha[1682:1690] == '       1'
        try:
            dic['NU_PERC_CARGA_HOR_DISTANCIA'] = float(linha[1690:1698])
        except:
            dic['NU_PERC_CARGA_HOR_DISTANCIA'] = None
        try:
            dic['NU_INTEGRALIZACAO_MATUTINO'] = float(linha[1698:1706])
        except:
            dic['NU_INTEGRALIZACAO_MATUTINO'] = None
        try:
            dic['NU_INTEGRALIZACAO_VESPERTINO'] = float(linha[1706:1714])
        except:
            dic['NU_INTEGRALIZACAO_VESPERTINO'] = None
        try:
            dic['NU_INTEGRALIZACAO_NOTURNO'] = float(linha[1714:1722])
        except:
            dic['NU_INTEGRALIZACAO_NOTURNO'] = None
        try:
            dic['NU_INTEGRALIZACAO_INTEGRAL'] = float(linha[1722:1730])
        except:
            dic['NU_INTEGRALIZACAO_INTEGRAL'] = None
        try:
            dic['NU_INTEGRALIZACAO_EAD'] = float(linha[1730:1738])
        except:
            dic['NU_INTEGRALIZACAO_EAD'] = None
        try:
            dic['QT_INSCRITOS_ANO_EAD'] = int(linha[1738:1746])
        except:
            dic['QT_INSCRITOS_ANO_EAD'] = None
        try:
            dic['QT_VAGAS_ANUAL_EAD'] = int(linha[1746:1754])
        except:
            dic['QT_VAGAS_ANUAL_EAD'] = None
        try:
            dic['QT_VAGAS_INTEGRAL_PRES'] = int(linha[1754:1762])
        except:
            dic['QT_VAGAS_INTEGRAL_PRES'] = None
        try: 
            dic['QT_VAGAS_MATUTINO_PRES'] = int(linha[1762:1770])
        except:
            dic['QT_VAGAS_MATUTINO_PRES'] = None
        try: 
            dic['QT_VAGAS_VESPERTINO_PRES'] = int(linha[1770:1778])
        except:
            dic['QT_VAGAS_VESPERTINO_PRES'] = None
        try: 
            dic['QT_VAGAS_NOTURNO_PRES'] = int(linha[1778:1786])
        except:
            dic['QT_VAGAS_NOTURNO_PRES'] = None
        try: 
            dic['QT_INSCRITOS_MATUTINO_PRES'] = int(linha[1786:1794])
        except:
            dic['QT_INSCRITOS_MATUTINO_PRES'] = None
        try: 
            dic['QT_INSCRITOS_VESPERTINO_PRES'] = int(linha[1794:1802])
        except:
            dic['QT_INSCRITOS_VESPERTINO_PRES'] = None
        try: 
            dic['QT_INSCRITOS_NOTURNO_PRES'] = int(linha[1802:1810])
        except:
            dic['QT_INSCRITOS_NOTURNO_PRES'] = None
        try: 
            dic['QT_INSCRITOS_INTEGRAL_PRES'] = int(linha[1810:1818])
        except:
            dic['QT_INSCRITOS_INTEGRAL_PRES'] = None
        ############### VARIAVEIS DERIVADAS ################
        try:
            dic['QT_MATRICULA_CURSO'] = int(linha[1818:1826])
        except:
            dic['QT_MATRICULA_CURSO'] = None
        try:
            dic['QT_CONCLUINTE_CURSO'] = int(linha[1826:1834])
        except:
            dic['QT_CONCLUINTE_CURSO'] = None
        dic['QT_INGRESSO_CURSO'] = linha[1834:1842]
        dic['QT_INGRESSO_PROCESSO_SELETIVO'] = linha[1842:1850]
        dic['QT_INGRESSO_OUTRA_FORMA'] = linha[1850:1858]
        
        
        
        #CONVERSAO DE LATIN-1 PARA UTF-8
        db.latin2utf(dic)



        #INSERCAO NO BANCO DE DADOS
        if firstExec:
            db.prepareInsert('CURSO', 'INEP2012.CURSO', dic)
            db.commit()
            firstExec = False
            
        db.usePreparedInsert('CURSO', dic)



    #ajusta a base de dados para a relacao local_oferta curso ser 1-n
    db.query('''CREATE TABLE INEP2012.cursotmp as SELECT c.CO_CURSO, NO_CURSO, l.CO_IES, l.CO_LOCAL_OFERTA, 
        CO_OCDE, NO_OCDE, CO_OCDE_AREA_GERAL, NO_OCDE_AREA_GERAL, CO_OCDE_AREA_ESPECIFICA,
        NO_OCDE_AREA_ESPECIFICA, CO_OCDE_AREA_DETALHADA, NO_OCDE_AREA_DETALHADA, CO_GRAU_ACADEMICO,
        DS_GRAU_ACADEMICO, CO_MODALIDADE_ENSINO, DS_MODALIDADE_ENSINO, CO_NIVEL_ACADEMICO,
        DS_NIVEL_ACADEMICO, IN_GRATUITO, TP_ATRIBUTO_INGRESSO, NU_CARGA_HORARIA, DT_INICIO_FUNCIONAMENTO,
        DT_AUTORIZACAO_CURSO, IN_AJUDA_DEFICIENTE, IN_MATERIAL_DIGITAL, IN_MATERIAL_AMPLIADO,
        IN_MATERIAL_TATIL, IN_MATERIAL_IMPRESSO, IN_MATERIAL_AUDIO, IN_MATERIAL_BRAILLE,
        IN_DISCIPLINA_LIBRAS, IN_GUIA_INTERPRETE, IN_MATERIAL_LIBRAS, IN_RECURSOS_COMUNICACAO,
        IN_RECURSOS_INFORMATICA, IN_TRADUTOR_LIBRAS, IN_INTEGRAL_CURSO, IN_MATUTINO_CURSO,
        IN_NOTURNO_CURSO, IN_VESPERTINO_CURSO, NU_PERC_CARGA_HOR_DISTANCIA, NU_INTEGRALIZACAO_MATUTINO,
        NU_INTEGRALIZACAO_VESPERTINO, NU_INTEGRALIZACAO_NOTURNO, NU_INTEGRALIZACAO_INTEGRAL,
        NU_INTEGRALIZACAO_EAD, QT_INSCRITOS_ANO_EAD, QT_VAGAS_ANUAL_EAD, QT_VAGAS_INTEGRAL_PRES,
        QT_VAGAS_MATUTINO_PRES, QT_VAGAS_VESPERTINO_PRES, QT_VAGAS_NOTURNO_PRES, QT_INSCRITOS_MATUTINO_PRES,
        QT_INSCRITOS_VESPERTINO_PRES, QT_INSCRITOS_NOTURNO_PRES, QT_INSCRITOS_INTEGRAL_PRES,
        QT_MATRICULA_CURSO, QT_CONCLUINTE_CURSO, QT_INGRESSO_CURSO, QT_INGRESSO_PROCESSO_SELETIVO,
        QT_INGRESSO_OUTRA_FORMA FROM INEP2012.CURSO c INNER JOIN INEP2012.LOCAL_OFERTA l
        ON c.co_curso = l.co_curso;
    CREATE TABLE INEP2012.localtmp AS SELECT DISTINCT(CO_LOCAL_OFERTA), CO_IES, CO_MUNICIPIO, IN_SEDE,
        IN_LOCAL_OFERTA_NEAD, IN_LOCAL_OFERTA_UAB, IN_LOCAL_OFERTA_REITORIA, IN_LOCAL_OFERTA_POLO,
        IN_LOCAL_OFERTA_UNID_ACADEMICA FROM INEP2012.LOCAL_OFERTA;
    CREATE TABLE INEP2012.cursotmp2 AS SELECT DISTINCT ON (co_curso) cursotmp.* FROM INEP2012.cursotmp;
    DROP TABLE INEP2012.LOCAL_OFERTA;
    DROP TABLE INEP2012.CURSO;
    DROP TABLE INEP2012.cursotmp;
    ALTER TABLE INEP2012.localtmp RENAME TO LOCAL_OFERTA;
    ALTER TABLE INEP2012.cursotmp2 RENAME TO CURSO;''')
    
    db.commit()
        