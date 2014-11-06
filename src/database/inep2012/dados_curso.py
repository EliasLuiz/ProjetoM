# realiza a leitura do arquivo /DADOS/CURSO.txt
# cria uma tabela no banco e salva os dados lidos


'''
%%%%%%%%     TESTAR     %%%%%%%%%
'''


from database import db

def txt_to_db(diretorio):
    
    db.query("DROP TABLE IF EXISTS INEP2012.CURSO")
    db.query("""CREATE TABLE INEP2012.CURSO(
        CO_IES,
        CO_MUNICIPIO_CURSO,
        NO_REGIAO_CURSO,
        IN_CAPITAL_CURSO,
        CO_CURSO,
        NO_CURSO,
        CO_OCDE,
        NO_OCDE,
        CO_OCDE_AREA_GERAL,
        NO_OCDE_AREA_GERAL,
        CO_OCDE_AREA_ESPECIFICA,
        NO_OCDE_AREA_ESPECIFICA,
        CO_OCDE_AREA_DETALHADA,
        NO_OCDE_AREA_DETALHADA,
        CO_GRAU_ACADEMICO,
        DS_GRAU_ACADEMICO,
        CO_MODALIDADE_ENSINO,
        DS_MODALIDADE_ENSINO,
        CO_NIVEL_ACADEMICO,
        DS_NIVEL_ACADEMICO,
        IN_GRATUITO,
        TP_ATRIBUTO_INGRESSO,
        CO_LOCAL_OFERTA,
        NU_CARGA_HORARIA,
        DT_INICIO_FUNCIONAMENTO,
        DT_AUTORIZACAO_CURSO,
        IN_AJUDA_DEFICIENTE,
        IN_MATERIAL_DIGITAL,
        IN_MATERIAL_AMPLIADO,
        IN_MATERIAL_TATIL,
        IN_MATERIAL_IMPRESSO,
        IN_MATERIAL_AUDIO,
        IN_MATERIAL_BRAILLE,
        IN_DISCIPLINA_LIBRAS,
        IN_GUIA_INTERPRETE,
        IN_MATERIAL_LIBRAS,
        IN_RECURSOS_COMUNICACAO,
        IN_RECURSOS_INFORMATICA,
        IN_TRADUTOR_LIBRAS,
        IN_INTEGRAL_CURSO,
        IN_MATUTINO_CURSO,
        IN_NOTURNO_CURSO,
        IN_VESPERTINO_CURSO,
        NU_PERC_CARGA_HOR_DISTANCIA,
        NU_INTEGRALIZACAO_MATUTINO,
        NU_INTEGRALIZACAO_VESPERTINO,
        NU_INTEGRALIZACAO_NOTURNO,
        NU_INTEGRALIZACAO_INTEGRAL,
        NU_INTEGRALIZACAO_EAD,
        QT_INSCRITOS_ANO_EAD,
        QT_INSCRITOS_ANO_EAD,
        QT_VAGAS_ANUAL_EAD,
        QT_VAGAS_ANUAL_EAD,
        QT_VAGAS_INTEGRAL_PRES,
        QT_VAGAS_INTEGRAL_PRES,
        QT_VAGAS_MATUTINO_PRES,
        QT_VAGAS_MATUTINO_PRES,
        QT_VAGAS_VESPERTINO_PRES,
        QT_VAGAS_VESPERTINO_PRES,
        QT_VAGAS_NOTURNO_PRES,
        QT_VAGAS_NOTURNO_PRES,
        QT_INSCRITOS_MATUTINO_PRES,
        QT_INSCRITOS_MATUTINO_PRES,
        QT_INSCRITOS_VESPERTINO_PRES,
        QT_INSCRITOS_VESPERTINO_PRES,
        QT_INSCRITOS_NOTURNO_PRES,
        QT_INSCRITOS_NOTURNO_PRES,
        QT_INSCRITOS_INTEGRAL_PRES,
        QT_INSCRITOS_INTEGRAL_PRES,
        QT_MATRICULA_CURSO,
        QT_CONCLUINTE_CURSO,
        QT_INGRESSO_CURSO,
        QT_INGRESSO_PROCESSO_SELETIVO,
        QT_INGRESSO_OUTRA_FORMA);""")

    file = open(diretorio + "/DADOS/CURSO.txt", "r")

    for linha in file.readlines():

        dic = {}
        
        ############### DADOS DA IES ################
        dic['CO_IES'] = linha[0:8]
        #dic['NO_IES'] = linha[8:208].strip()
        #dic['CO_CATEGORIA_ADMINISTRATIVA'] = linha[208:216]
        #dic['DS_CATEGORIA_ADMINISTRATIVA'] = linha[216:316].strip()
        #dic['CO_ORGANIZACAO_ACADEMICA'] = linha[316:324]
        #dic['DS_ORGANIZACAO_ACADEMICA'] = linha[324:424].strip()
        ############### DADOS DO CURSO ################
        dic['CO_MUNICIPIO_CURSO'] = linha[424:432]
        #dic['NO_MUNICIPIO_CURSO'] = linha[432:582].strip()
        #dic['CO_UF_CURSO'] = linha[582:590]
        #dic['SGL_UF_CURSO'] = linha[590:592]
        dic['NO_REGIAO_CURSO'] = linha[592:622].strip()
        dic['IN_CAPITAL_CURSO'] = linha[622:630] == '       1'
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
        dic['CO_GRAU_ACADEMICO'] = linha[1366:1374]
        dic['DS_GRAU_ACADEMICO'] = linha[1374:1386].strip()
        dic['CO_MODALIDADE_ENSINO'] = linha[1386:1394]
        dic['DS_MODALIDADE_ENSINO'] = linha[1394:1405].strip()
        dic['CO_NIVEL_ACADEMICO'] = linha[1405:1413]
        dic['DS_NIVEL_ACADEMICO'] = linha[1413:1446].strip()
        dic['IN_GRATUITO'] = linha[1446:1454] == '       1'
        dic['TP_ATRIBUTO_INGRESSO'] = linha[1454:1462]
        dic['CO_LOCAL_OFERTA'] = linha[1462:1470]
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
        dic['NU_PERC_CARGA_HOR_DISTANCIA'] = linha[1690:1698]
        dic['NU_INTEGRALIZACAO_MATUTINO'] = linha[1698:1706]
        dic['NU_INTEGRALIZACAO_VESPERTINO'] = linha[1706:1714]
        dic['NU_INTEGRALIZACAO_NOTURNO'] = linha[1714:1722]
        dic['NU_INTEGRALIZACAO_INTEGRAL'] = linha[1722:1730]
        dic['NU_INTEGRALIZACAO_EAD'] = linha[1730:1738]
        try:
            dic['QT_INSCRITOS_ANO_EAD'] = linha[1738:1746]
        except:
            dic['QT_INSCRITOS_ANO_EAD'] = ""
        try:
            dic['QT_VAGAS_ANUAL_EAD'] = linha[1746:1754]
        except:
            dic['QT_VAGAS_ANUAL_EAD'] = ""
        try:
            dic['QT_VAGAS_INTEGRAL_PRES'] = linha[1754:1762]
        except:
            dic['QT_VAGAS_INTEGRAL_PRES'] = ""
        try: 
            dic['QT_VAGAS_MATUTINO_PRES'] = linha[1762:1770]
        except:
            dic['QT_VAGAS_MATUTINO_PRES'] = ""
        try: 
            dic['QT_VAGAS_VESPERTINO_PRES'] = linha[1770:1778]
        except:
            dic['QT_VAGAS_VESPERTINO_PRES'] = ""
        try: 
            dic['QT_VAGAS_NOTURNO_PRES'] = linha[1778:1786]
        except:
            dic['QT_VAGAS_NOTURNO_PRES'] = ""
        try: 
            dic['QT_INSCRITOS_MATUTINO_PRES'] = linha[1786:1794]
        except:
            dic['QT_INSCRITOS_MATUTINO_PRES'] = ""
        try: 
            dic['QT_INSCRITOS_VESPERTINO_PRES'] = linha[1794:1802]
        except:
            dic['QT_INSCRITOS_VESPERTINO_PRES'] = ""
        try: 
            dic['QT_INSCRITOS_NOTURNO_PRES'] = linha[1802:1810]
        except:
            dic['QT_INSCRITOS_NOTURNO_PRES'] = ""
        try: 
            dic['QT_INSCRITOS_INTEGRAL_PRES'] = linha[1810:1818]
        except:
            dic['QT_INSCRITOS_INTEGRAL_PRES'] = ""
        ############### VARIAVEIS DERIVADAS ################
        dic['QT_MATRICULA_CURSO'] = linha[1818:1826]
        dic['QT_CONCLUINTE_CURSO'] = linha[1826:1834]
        dic['QT_INGRESSO_CURSO'] = linha[1834:1842]
        dic['QT_INGRESSO_PROCESSO_SELETIVO'] = linha[1842:1850]
        dic['QT_INGRESSO_OUTRA_FORMA'] = linha[1850:1858]

        #gerador de sql baseado no dicionario
        # %%%%%%%%%%%%% TESTAR %%%%%%%%%%%%%%
        db.query(db.sqlGenerator('INEP2012.CURSO', dic))
        
        '''
        sqlCurso="INSERT INTO CURSO(CO_IES,CO_MUNICIPIO_CURSO,NO_REGIAO_CURSO,IN_CAPITAL_CURSO,CO_CURSO,NO_CURSO,CO_OCDE,NO_OCDE,CO_OCDE_AREA_GERAL,NO_OCDE_AREA_GERAL,CO_OCDE_AREA_ESPECIFICA,NO_OCDE_AREA_ESPECIFICA,CO_OCDE_AREA_DETALHADA,NO_OCDE_AREA_DETALHADA,CO_GRAU_ACADEMICO,DS_GRAU_ACADEMICO,CO_MODALIDADE_ENSINO,DS_MODALIDADE_ENSINO,CO_NIVEL_ACADEMICO,DS_NIVEL_ACADEMICO,IN_GRATUITO,TP_ATRIBUTO_INGRESSO,CO_LOCAL_OFERTA,NU_CARGA_HORARIA,DT_INICIO_FUNCIONAMENTO,DT_AUTORIZACAO_CURSO,IN_AJUDA_DEFICIENTE,IN_MATERIAL_DIGITAL,IN_MATERIAL_AMPLIADO,IN_MATERIAL_TATIL,IN_MATERIAL_IMPRESSO,IN_MATERIAL_AUDIO,IN_MATERIAL_BRAILLE,IN_DISCIPLINA_LIBRAS,IN_GUIA_INTERPRETE,IN_MATERIAL_LIBRAS,IN_RECURSOS_COMUNICACAO,IN_RECURSOS_INFORMATICA,IN_TRADUTOR_LIBRAS,IN_INTEGRAL_CURSO,IN_MATUTINO_CURSO,IN_NOTURNO_CURSO,IN_VESPERTINO_CURSO,NU_PERC_CARGA_HOR_DISTANCIA,NU_INTEGRALIZACAO_MATUTINO,NU_INTEGRALIZACAO_VESPERTINO,NU_INTEGRALIZACAO_NOTURNO,NU_INTEGRALIZACAO_INTEGRAL,NU_INTEGRALIZACAO_EAD,QT_INSCRITOS_ANO_EAD,QT_INSCRITOS_ANO_EAD,QT_VAGAS_ANUAL_EAD,QT_VAGAS_ANUAL_EAD,QT_VAGAS_INTEGRAL_PRES,QT_VAGAS_INTEGRAL_PRES,QT_VAGAS_MATUTINO_PRES,QT_VAGAS_MATUTINO_PRES,QT_VAGAS_VESPERTINO_PRES,QT_VAGAS_VESPERTINO_PRES,QT_VAGAS_NOTURNO_PRES,QT_VAGAS_NOTURNO_PRES,QT_INSCRITOS_MATUTINO_PRES,QT_INSCRITOS_MATUTINO_PRES,QT_INSCRITOS_VESPERTINO_PRES,QT_INSCRITOS_VESPERTINO_PRES,QT_INSCRITOS_NOTURNO_PRES,QT_INSCRITOS_NOTURNO_PRES,QT_INSCRITOS_INTEGRAL_PRES,QT_INSCRITOS_INTEGRAL_PRES,QT_MATRICULA_CURSO,QT_CONCLUINTE_CURSO,QT_INGRESSO_CURSO,QT_INGRESSO_PROCESSO_SELETIVO,QT_INGRESSO_OUTRA_FORMA) "
        sqlCurso2="VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"%(dic['CO_IES'],dic['CO_MUNICIPIO_CURSO'],dic['NO_REGIAO_CURSO'],dic['IN_CAPITAL_CURSO'],dic['CO_CURSO'],dic['NO_CURSO'],dic['CO_OCDE'],dic['NO_OCDE'],dic['CO_OCDE_AREA_GERAL'],dic['NO_OCDE_AREA_GERAL'],dic['CO_OCDE_AREA_ESPECIFICA'],dic['NO_OCDE_AREA_ESPECIFICA'],dic['CO_OCDE_AREA_DETALHADA'],dic['NO_OCDE_AREA_DETALHADA'],dic['CO_GRAU_ACADEMICO'],dic['DS_GRAU_ACADEMICO'],dic['CO_MODALIDADE_ENSINO'],dic['DS_MODALIDADE_ENSINO'],dic['CO_NIVEL_ACADEMICO'],dic['DS_NIVEL_ACADEMICO'],dic['IN_GRATUITO'],dic['TP_ATRIBUTO_INGRESSO'],dic['CO_LOCAL_OFERTA'],dic['NU_CARGA_HORARIA'],dic['DT_INICIO_FUNCIONAMENTO'],dic['DT_AUTORIZACAO_CURSO'],dic['IN_AJUDA_DEFICIENTE'],dic['IN_MATERIAL_DIGITAL'],dic['IN_MATERIAL_AMPLIADO'],dic['IN_MATERIAL_TATIL'],dic['IN_MATERIAL_IMPRESSO'],dic['IN_MATERIAL_AUDIO'],dic['IN_MATERIAL_BRAILLE'],dic['IN_DISCIPLINA_LIBRAS'],dic['IN_GUIA_INTERPRETE'],dic['IN_MATERIAL_LIBRAS'],dic['IN_RECURSOS_COMUNICACAO'],dic['IN_RECURSOS_INFORMATICA'],dic['IN_TRADUTOR_LIBRAS'],dic['IN_INTEGRAL_CURSO'],dic['IN_MATUTINO_CURSO'],dic['IN_NOTURNO_CURSO'],dic['IN_VESPERTINO_CURSO'],dic['NU_PERC_CARGA_HOR_DISTANCIA'],dic['NU_INTEGRALIZACAO_MATUTINO'],dic['NU_INTEGRALIZACAO_VESPERTINO'],dic['NU_INTEGRALIZACAO_NOTURNO'],dic['NU_INTEGRALIZACAO_INTEGRAL'],dic['NU_INTEGRALIZACAO_EAD'],dic['QT_INSCRITOS_ANO_EAD'],dic['QT_INSCRITOS_ANO_EAD'],dic['QT_VAGAS_ANUAL_EAD'],dic['QT_VAGAS_ANUAL_EAD'],dic['QT_VAGAS_INTEGRAL_PRES'],dic['QT_VAGAS_INTEGRAL_PRES'],dic['QT_VAGAS_MATUTINO_PRES'],dic['QT_VAGAS_MATUTINO_PRES'],dic['QT_VAGAS_VESPERTINO_PRES'],dic['QT_VAGAS_VESPERTINO_PRES'],dic['QT_VAGAS_NOTURNO_PRES'],dic['QT_VAGAS_NOTURNO_PRES'],dic['QT_INSCRITOS_MATUTINO_PRES'],dic['QT_INSCRITOS_MATUTINO_PRES'],dic['QT_INSCRITOS_VESPERTINO_PRES'],dic['QT_INSCRITOS_VESPERTINO_PRES'],dic['QT_INSCRITOS_NOTURNO_PRES'],dic['QT_INSCRITOS_NOTURNO_PRES'],dic['QT_INSCRITOS_INTEGRAL_PRES'],dic['QT_INSCRITOS_INTEGRAL_PRES'],dic['QT_MATRICULA_CURSO'],dic['QT_CONCLUINTE_CURSO'],dic['QT_INGRESSO_CURSO'],dic['QT_INGRESSO_PROCESSO_SELETIVO'],dic['QT_INGRESSO_OUTRA_FORMA'])
        sqlCurso=sqlCurso+sqlCurso2
        db.query(sqlCurso)
        '''

    file.close()