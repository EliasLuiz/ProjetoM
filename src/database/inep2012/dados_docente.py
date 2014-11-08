# realiza a leitura do arquivo /DADOS/DOCENTE.txt
# cria uma tabela no banco e salva os dados lidos


'''
%%%%%%%%     TESTAR     %%%%%%%%%
'''


from database import db
import codecs

def txt2db(diretorio):
    
    print "entrou em docente"

    db.commit()
    db.query("DROP TABLE IF EXISTS INEP2012.DOCENTE")
    db.query("""CREATE TABLE INEP2012.DOCENTE(
        CO_IES INT,
        CO_DOCENTE_IES INT,
        CO_DOCENTE BIGINT,
        CO_SITUACAO_DOCENTE INT,
        DS_SITUACAO_DOCENTE VARCHAR(100),
        CO_ESCOLARIDADE_DOCENTE INT,
        DS_ESCOLARIDADE_DOCENTE VARCHAR(14),
        CO_REGIME_TRABALHO INT,
        DS_REGIME_TRABALHO VARCHAR(38),
        IN_SEXO_DOCENTE BOOLEAN,
        DS_SEXO_DOCENTE VARCHAR(9),
        NU_ANO_DOCENTE_NASC INT,
        NU_MES_DOCENTE_NASC INT,
        NU_DIA_DOCENTE_NASC INT,
        NU_IDADE_DOCENTE INT,
        CO_COR_RACA_DOCENTE INT,
        DS_COR_RACA_DOCENTE VARCHAR(24),
        CO_PAIS_DOCENTE INT,
        CO_NACIONALIDADE_DOCENTE INT,
        CO_MUNICIPIO_NASCIMENTO INT,
        IN_DOCENTE_DEFICIENCIA BOOLEAN,
        IN_CEGUEIRA BOOLEAN,
        IN_BAIXA_VISAO BOOLEAN,
        IN_SURDEZ BOOLEAN,
        IN_DEFICIENCIA_AUDITIVA BOOLEAN,
        IN_DEFICIENCIA_FISICA BOOLEAN,
        IN_SURDOCEGUEIRA BOOLEAN,
        IN_DEFICIENCIA_MULTIPLA BOOLEAN,
        IN_DEFICIENCIA_INTELECTUAL BOOLEAN,
        IN_ATU_EAD BOOLEAN,
        IN_ATU_EXTENSAO BOOLEAN,
        IN_ATU_GESTAO BOOLEAN,
        IN_ATU_GRAD_PRESENCIAL BOOLEAN,
        IN_ATU_POS_EAD BOOLEAN,
        IN_ATU_POS_PRESENCIAL BOOLEAN,
        IN_ATU_SEQUENCIAL BOOLEAN,
        IN_ATU_PESQUISA BOOLEAN,
        IN_BOLSA_PESQUISA BOOLEAN,
        IN_SUBSTITUTO BOOLEAN,
        IN_EXERCICIO_DT_REF BOOLEAN,
        IN_VISITANTE BOOLEAN,
        IN_VISITANTE_IFES_VINCULO INT);""")
    
    
    firstExec = True
    
    
    for linha in codecs.open(diretorio + "/DADOS/DOCENTE.txt", "r", 'latin-1'):
        
        dic = {}
        
	#LEITURA DO ARQUIVO
        ############### DADOS DA IES ################
        dic['CO_IES'] = linha[0:8] #transforma em int
        #dic['NO_IES'] = linha[8:208].strip()
        #dic['CO_CATEGORIA_ADMINISTRATIVA'] = linha[208:216]
        #dic['DS_CATEGORIA_ADMINISTRATIVA'] = linha[216:316].strip()
        #dic['CO_ORGANIZACAO_ACADEMICA'] = linha[316:324]
        #dic['DS_ORGANIZACAO_ACADEMICA'] = linha[324:424].strip()
        #dic['IN_CAPITAL_IES'] = linha[424:432] == '       1'
        ############### DADOS DO DOCENTE ################
        dic['CO_DOCENTE_IES'] = linha[432:440]
        dic['CO_DOCENTE'] = linha[440:453]
        dic['CO_SITUACAO_DOCENTE'] = linha[453:461]
        dic['DS_SITUACAO_DOCENTE'] = linha[461:511].strip()
        dic['CO_ESCOLARIDADE_DOCENTE'] = linha[511:519]
        dic['DS_ESCOLARIDADE_DOCENTE'] = linha[519:533].strip()
        if(linha[533:579].isalnum()): #caso o campo nao esteja vazio
            dic['CO_REGIME_TRABALHO'] = linha[533:541]
            dic['DS_REGIME_TRABALHO'] = linha[541:579].strip()
        else:
            dic['CO_REGIME_TRABALHO'] = None
            dic['DS_REGIME_TRABALHO'] = None
        dic['IN_SEXO_DOCENTE'] = linha[579:587] == '       1'
        dic['DS_SEXO_DOCENTE'] = linha[587:596].strip()
        dic['NU_ANO_DOCENTE_NASC'] = linha[596:600]
        dic['NU_MES_DOCENTE_NASC'] = linha[600:602]
        dic['NU_DIA_DOCENTE_NASC'] = linha[602:604]
        dic['NU_IDADE_DOCENTE'] = linha[604:612]
        dic['CO_COR_RACA_DOCENTE'] = linha[612:620]
        dic['DS_COR_RACA_DOCENTE'] = linha[620:644].strip()
        dic['CO_PAIS_DOCENTE'] = linha[644:652]
        dic['CO_NACIONALIDADE_DOCENTE'] = linha[652:660]
        if(linha[660:676].isalnum()):
            #dic['CO_UF_NASCIMENTO'] = linha[660:668]
            dic['CO_MUNICIPIO_NASCIMENTO'] = linha[668:676]
        else:
            #dic['CO_UF_NASCIMENTO'] = None
            dic['CO_MUNICIPIO_NASCIMENTO'] = None
        dic['IN_DOCENTE_DEFICIENCIA'] = linha[676:684] == '       1'
        if(linha[684:692].isalnum()):
            dic['IN_CEGUEIRA'] = linha[684:692] == '       1'
        else:
            dic['IN_CEGUEIRA'] = None
        if(linha[692:700].isalnum()):
            dic['IN_BAIXA_VISAO'] = linha[692:700] == '       1'
        else:
            dic['IN_BAIXA_VISAO'] = None
        if(linha[700:708].isalnum()):
            dic['IN_SURDEZ'] = linha[700:708] == '       1'
        else:
            dic['IN_SURDEZ'] = None
        if(linha[708:716].isalnum()):
            dic['IN_DEFICIENCIA_AUDITIVA'] = linha[708:716] == '       1'
        else:
            dic['IN_DEFICIENCIA_AUDITIVA'] = None
        if(linha[716:724].isalnum()):
            dic['IN_DEFICIENCIA_FISICA'] = linha[716:724] == '       1'
        else:
            dic['IN_DEFICIENCIA_FISICA'] = None
        if(linha[724:732].isalnum()):
            dic['IN_SURDOCEGUEIRA'] = linha[724:732] == '       1'
        else:
            dic['IN_SURDOCEGUEIRA'] = None
        if(linha[732:740].isalnum()):
            dic['IN_DEFICIENCIA_MULTIPLA'] = linha[732:740] == '       1'
        else:
            dic['IN_DEFICIENCIA_MULTIPLA'] = None
        if(linha[740:748].isalnum()):
            dic['IN_DEFICIENCIA_INTELECTUAL'] = linha[740:748] == '       1'
        else:
            dic['IN_DEFICIENCIA_INTELECTUAL'] = None
        if(linha[748:756].isalnum()):
            dic['IN_ATU_EAD'] = linha[748:756] == '       1'
        else:
            dic['IN_ATU_EAD'] = None
        if(linha[756:764].isalnum()):
            dic['IN_ATU_EXTENSAO'] = linha[756:764] == '       1'
        else:
            dic['IN_ATU_EXTENSAO'] = None
        if(linha[764:772].isalnum()):
            dic['IN_ATU_GESTAO'] = linha[764:772] == '       1'
        else:
            dic['IN_ATU_GESTAO'] = None
        if(linha[772:780].isalnum()):
            dic['IN_ATU_GRAD_PRESENCIAL'] = linha[772:780] == '       1'
        else:
            dic['IN_ATU_GRAD_PRESENCIAL'] = None
        if(linha[780:788].isalnum()):
            dic['IN_ATU_POS_EAD'] = linha[780:788] == '       1'
        else:
            dic['IN_ATU_POS_EAD'] = None
        if(linha[788:796].isalnum()):
            dic['IN_ATU_POS_PRESENCIAL'] = linha[788:796] == '       1'
        else:
            dic['IN_ATU_POS_PRESENCIAL'] = None
        if(linha[796:804].isalnum()):
            dic['IN_ATU_SEQUENCIAL'] = linha[796:804] == '       1'
        else:
            dic['IN_ATU_SEQUENCIAL'] = None
        if(linha[804:812].isalnum()):
            dic['IN_ATU_PESQUISA'] = linha[804:812] == '       1'
        else:
            dic['IN_ATU_PESQUISA'] = None
        if(linha[812:820].isalnum()):
            dic['IN_BOLSA_PESQUISA'] = linha[812:820] == '       1'
        else:
            dic['IN_BOLSA_PESQUISA'] =None
        if(linha[820:828].isalnum()):
            dic['IN_SUBSTITUTO'] = linha[820:828] == '       1'
        else:
            dic['IN_SUBSTITUTO'] = None
        if(linha[828:836].isalnum()):
            dic['IN_EXERCICIO_DT_REF'] = linha[828:836] == '       1'
        else:
            dic['IN_EXERCICIO_DT_REF'] = None
        if(linha[836:844].isalnum()):
            dic['IN_VISITANTE'] = linha[836:844] == '       1'
        else:
            dic['IN_VISITANTE'] =None
        if(linha[844:852].isalnum()):
            dic['IN_VISITANTE_IFES_VINCULO'] = linha[844:852] #um codigo 1 ou 2 que eh optativo
        else:
            dic['IN_VISITANTE_IFES_VINCULO'] = None
        
        
        
        #CONVERSAO DE LATIN-1 PARA UTF-8
        db.latin2utf(dic)



        #INSERCAO NO BANCO DE DADOS
        if firstExec:
            db.prepareInsert('DOCENTE', 'INEP2012.DOCENTE', dic)
            db.commit()
            firstExec = False
            
	db.usePreparedInsert('DOCENTE', dic)
        
        
    db.commit()




        
'''       
        sqlDocente="INSERT INTO DOCENTE(CO_IES,CO_DOCENTE_IES,CO_DOCENTE,CO_SITUACAO_DOCENTE,DS_SITUACAO_DOCENTE,CO_ESCOLARIDADE_DOCENTE,DS_ESCOLARIDADE_DOCENTE,CO_REGIME_TRABALHO,DS_REGIME_TRABALHO,IN_SEXO_DOCENTE,DS_SEXO_DOCENTE,NU_ANO_DOCENTE_NASC,NU_MES_DOCENTE_NASC,NU_DIA_DOCENTE_NASC,NU_IDADE_DOCENTE,CO_COR_RACA_DOCENTE,DS_COR_RACA_DOCENTE,CO_PAIS_DOCENTE,CO_NACIONALIDADE_DOCENTE,CO_MUNICIPIO_NASCIMENTO,IN_DOCENTE_DEFICIENCIA,IN_CEGUEIRA,IN_BAIXA_VISAO,IN_SURDEZ,IN_DEFICIENCIA_AUDITIVA,IN_DEFICIENCIA_FISICA,IN_SURDOCEGUEIRA,IN_DEFICIENCIA_MULTIPLA,IN_DEFICIENCIA_INTELECTUAL,IN_ATU_EAD,IN_ATU_EXTENSAO,IN_ATU_GESTAO,IN_ATU_GRAD_PRESENCIAL,IN_ATU_POS_EAD,IN_ATU_POS_PRESENCIAL,IN_ATU_SEQUENCIAL,IN_ATU_PESQUISA,IN_BOLSA_PESQUISA,IN_SUBSTITUTO,IN_EXERCICIO_DT_REF,IN_VISITANTE,IN_VISITANTE_IFES_VINCULO) "
        sqlDocente2="VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"%(dic['CO_IES'],dic['CO_DOCENTE_IES'],dic['CO_DOCENTE'],dic['CO_SITUACAO_DOCENTE'],dic['DS_SITUACAO_DOCENTE'],dic['CO_ESCOLARIDADE_DOCENTE'],dic['DS_ESCOLARIDADE_DOCENTE'],dic['CO_REGIME_TRABALHO'],dic['DS_REGIME_TRABALHO'],dic['IN_SEXO_DOCENTE'],dic['DS_SEXO_DOCENTE'],dic['NU_ANO_DOCENTE_NASC'],dic['NU_MES_DOCENTE_NASC'],dic['NU_DIA_DOCENTE_NASC'],dic['NU_IDADE_DOCENTE'],dic['CO_COR_RACA_DOCENTE'],dic['DS_COR_RACA_DOCENTE'],dic['CO_PAIS_DOCENTE'],dic['CO_NACIONALIDADE_DOCENTE'],dic['CO_MUNICIPIO_NASCIMENTO'],dic['IN_DOCENTE_DEFICIENCIA'],dic['IN_CEGUEIRA'],dic['IN_BAIXA_VISAO'],dic['IN_SURDEZ'],dic['IN_DEFICIENCIA_AUDITIVA'],dic['IN_DEFICIENCIA_FISICA'],dic['IN_SURDOCEGUEIRA'],dic['IN_DEFICIENCIA_MULTIPLA'],dic['IN_DEFICIENCIA_INTELECTUAL'],dic['IN_ATU_EAD'],dic['IN_ATU_EXTENSAO'],dic['IN_ATU_GESTAO'],dic['IN_ATU_GRAD_PRESENCIAL'],dic['IN_ATU_POS_EAD'],dic['IN_ATU_POS_PRESENCIAL'],dic['IN_ATU_SEQUENCIAL'],dic['IN_ATU_PESQUISA'],dic['IN_BOLSA_PESQUISA'],dic['IN_SUBSTITUTO'],dic['IN_EXERCICIO_DT_REF'],dic['IN_VISITANTE'],dic['IN_VISITANTE_IFES_VINCULO'])
        sqlDocente=sqlDocente+sqlDocente2
        db.query(sqlDocente)
'''