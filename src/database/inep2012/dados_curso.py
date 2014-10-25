# realiza a leitura do arquivo /DADOS/CURSO.txt
# cria uma tabela no banco e salva os dados lidos

from database import db

def txt_to_db(diretorio):

    file = open(diretorio + "/DADOS/CURSO.txt", "r")

    for linha in file.readlines():

        dic = {}
        ############### DADOS DA IES ################
        dic['CO_IES'] = int(linha[0:8])
        dic['NO_IES'] = linha[8:208]
        dic['CO_CATEGORIA_ADMINISTRATIVA'] = int(linha[208:216])
        dic['DS_CATEGORIA_ADMINISTRATIVA'] = linha[216:316]
        dic['CO_ORGANIZACAO_ACADEMICA'] = int(linha[316:324])
        dic['DS_ORGANIZACAO_ACADEMICA'] = linha[324:424]
        ############### DADOS DO CURSO ################
        dic['CO_MUNICIPIO_CURSO'] = int(linha[424:432])
        dic['NO_MUNICIPIO_CURSO'] = linha[432:582]
        dic['CO_UF_CURSO'] = int(linha[582:590])
        dic['SGL_UF_CURSO'] = linha[590:592]
        dic['NO_REGIAO_CURSO'] = linha[592:622]
        dic['IN_CAPITAL_CURSO'] = linha[622:630] == '       1'
        dic['CO_CURSO'] = int(linha[630:638])
        dic['NO_CURSO'] = linha[638:838]
        dic['CO_OCDE'] = linha[838:850]
        dic['NO_OCDE'] = linha[850:970]
        dic['CO_OCDE_AREA_GERAL'] = linha[970:982]
        dic['NO_OCDE_AREA_GERAL'] = linha[982:1102]
        dic['CO_OCDE_AREA_ESPECIFICA'] = linha[1102:1114]
        dic['NO_OCDE_AREA_ESPECIFICA'] = linha[1114:1234]
        dic['CO_OCDE_AREA_DETALHADA'] = linha[1234:1246]
        dic['NO_OCDE_AREA_DETALHADA'] = linha[1246:1366]
        dic['CO_GRAU_ACADEMICO'] = int(linha[1366:1374])
        dic['DS_GRAU_ACADEMICO'] = linha[1374:1386]
        dic['CO_MODALIDADE_ENSINO'] = int(linha[1386:1394])
        dic['DS_MODALIDADE_ENSINO'] = linha[1394:1405]
        dic['CO_NIVEL_ACADEMICO'] = int(linha[1405:1413])
        dic['DS_NIVEL_ACADEMICO'] = linha[1413:1446]
        dic['IN_GRATUITO'] = linha[1446:1454] == '       1'
        dic['TP_ATRIBUTO_INGRESSO'] = int(linha[1454:1462])
        dic['CO_LOCAL_OFERTA'] = int(linha[1462:1470])
        dic['NU_CARGA_HORARIA'] = int(linha[1470:1478])
        dic['DT_INICIO_FUNCIONAMENTO'] = int(linha[1478:1516])
        dic['DT_AUTORIZACAO_CURSO'] = int(linha[1516:1554])
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
        dic['NU_PERC_CARGA_HOR_DISTANCIA'] = int(linha[1690:1698])
        dic['NU_INTEGRALIZACAO_MATUTINO'] = int(linha[1698:1706])
        dic['NU_INTEGRALIZACAO_VESPERTINO'] = int(linha[1706:1714])
        dic['NU_INTEGRALIZACAO_NOTURNO'] = int(linha[1714:1722])
        dic['NU_INTEGRALIZACAO_INTEGRAL'] = int(linha[1722:1730])
        dic['NU_INTEGRALIZACAO_EAD'] = int(linha[1730:1738])
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
        dic['QT_MATRICULA_CURSO'] = int(linha[1818:1826])
        dic['QT_CONCLUINTE_CURSO'] = int(linha[1826:1834])
        dic['QT_INGRESSO_CURSO'] = int(linha[1834:1842])
        dic['QT_INGRESSO_PROCESSO_SELETIVO'] = int(linha[1842:1850])
        dic['QT_INGRESSO_OUTRA_FORMA'] = int(linha[1850:1858])
        

    file.close()