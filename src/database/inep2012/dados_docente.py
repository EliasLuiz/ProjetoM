# realiza a leitura do arquivo /DADOS/DOCENTE.txt
# cria uma tabela no banco e salva os dados lidos


'''
%%%%%%%%     TESTAR     %%%%%%%%%
'''


from database import db

def txt_to_db(diretorio):
    
    file = open(diretorio + "/DADOS/DOCENTE.txt", "r")
    
    for linha in file.readlines():
        
        dic = {}
        
        ############### DADOS DA IES ################
        dic['CO_IES'] = int(linha[0:8]) #transforma em int
        dic['NO_IES'] = linha[8:208].strip()
        dic['CO_CATEGORIA_ADMINISTRATIVA'] = int(linha[208:216])
        dic['DS_CATEGORIA_ADMINISTRATIVA'] = linha[216:316].strip()
        dic['CO_ORGANIZACAO_ACADEMICA'] = int(linha[316:324])
        dic['DS_ORGANIZACAO_ACADEMICA'] = linha[324:424].strip()
        dic['IN_CAPITAL_IES'] = linha[424:432] == ' 1'
        ############### DADOS DO DOCENTE ################
        dic['CO_DOCENTE_IES'] = int(linha[432:440])
        dic['CO_DOCENTE'] = int(linha[440:453])
        dic['CO_SITUACAO_DOCENTE'] = int(linha[453:461])
        dic['DS_SITUACAO_DOCENTE'] = linha[461:511].strip()
        dic['CO_ESCOLARIDADE_DOCENTE'] = int(linha[511:519])
        dic['DS_ESCOLARIDADE_DOCENTE'] = linha[519:533].strip()
        if(linha[533:579].isalnum()): #caso o campo não esteja vazio
            dic['CO_REGIME_TRABALHO'] = int(linha[533:541])
            dic['DS_REGIME_TRABALHO'] = linha[541:579].strip()
        else:
            dic['CO_REGIME_TRABALHO'] = None
            dic['DS_REGIME_TRABALHO'] = None
        dic['IN_SEXO_DOCENTE'] = linha[579:587] == ' 1'
        dic['DS_SEXO_DOCENTE'] = linha[587:596].strip()
        dic['NU_ANO_DOCENTE_NASC'] = int(linha[596:600])
        dic['NU_MES_DOCENTE_NASC'] = int(linha[600:602])
        dic['NU_DIA_DOCENTE_NASC'] = int(linha[602:604])
        dic['NU_IDADE_DOCENTE'] = int(linha[604:612])
        dic['CO_COR_RACA_DOCENTE'] = int(linha[612:620])
        dic['DS_COR_RACA_DOCENTE'] = linha[620:644].strip()
        dic['CO_PAIS_DOCENTE'] = int(linha[644:652])
        dic['CO_NACIONALIDADE_DOCENTE'] = int(linha[652:660])
        if(linha[660:676].isalnum()):
            dic['CO_UF_NASCIMENTO'] = int(linha[660:668])
            dic['CO_MUNICIPIO_NASCIMENTO'] = int(linha[668:676])
        else:
            dic['CO_UF_NASCIMENTO'] = None
            dic['CO_MUNICIPIO_NASCIMENTO'] = None
        dic['IN_DOCENTE_DEFICIENCIA'] = linha[676:684] == ' 1'
        if(linha[684:692].isalnum()):
            dic['IN_CEGUEIRA'] = linha[684:692] == ' 1'
        else:
            dic['IN_CEGUEIRA'] = None
        if(linha[692:700].isalnum()):
            dic['IN_BAIXA_VISAO'] = linha[692:700] == ' 1'
        else:
            dic['IN_BAIXA_VISAO'] = None
        if(linha[700:708].isalnum()):
            dic['IN_SURDEZ'] = linha[700:708] == ' 1'
        else:
            dic['IN_SURDEZ'] = None
        if(linha[708:716].isalnum()):
            dic['IN_DEFICIENCIA_AUDITIVA'] = linha[708:716] == ' 1'
        else:
            dic['IN_DEFICIENCIA_AUDITIVA'] = None
        if(linha[716:724].isalnum()):
            dic['IN_DEFICIENCIA_FISICA'] = linha[716:724] == ' 1'
        else:
            dic['IN_DEFICIENCIA_FISICA'] = None
        if(linha[724:732].isalnum()):
            dic['IN_SURDOCEGUEIRA'] = linha[724:732] == ' 1'
        else:
            dic['IN_SURDOCEGUEIRA'] = None
        if(linha[732:740].isalnum()):
            dic['IN_DEFICIENCIA_MULTIPLA'] = linha[732:740] == ' 1'
        else:
            dic['IN_DEFICIENCIA_MULTIPLA'] = None
        if(linha[740:748].isalnum()):
            dic['IN_DEFICIENCIA_INTELECTUAL'] = linha[740:748] == ' 1'
        else:
            dic['IN_DEFICIENCIA_INTELECTUAL'] = None
        if(linha[748:756].isalnum()):
            dic['IN_ATU_EAD'] = linha[748:756] == ' 1'
        else:
            dic['IN_ATU_EAD'] = None
        if(linha[756:764].isalnum()):
            dic['IN_ATU_EXTENSAO'] = linha[756:764] == ' 1'
        else:
            dic['IN_ATU_EXTENSAO'] = None
        if(linha[764:772].isalnum()):
            dic['IN_ATU_GESTAO'] = linha[764:772] == ' 1'
        else:
            dic['IN_ATU_GESTAO'] = None
        if(linha[772:780].isalnum()):
            dic['IN_ATU_GRAD_PRESENCIAL'] = linha[772:780] == ' 1'
        else:
            dic['IN_ATU_GRAD_PRESENCIAL'] = None
        if(linha[780:788].isalnum()):
            dic['IN_ATU_POS_EAD'] = linha[780:788] == ' 1'
        else:
            dic['IN_ATU_POS_EAD'] = None
        if(linha[788:796].isalnum()):
            dic['IN_ATU_POS_PRESENCIAL'] = linha[788:796] == ' 1'
        else:
            dic['IN_ATU_POS_PRESENCIAL'] = None
        if(linha[796:804].isalnum()):
            dic['IN_ATU_SEQUENCIAL'] = linha[796:804] == ' 1'
        else:
            dic['IN_ATU_SEQUENCIAL'] = None
        if(linha[804:812].isalnum()):
            dic['IN_ATU_PESQUISA'] = linha[804:812] == ' 1'
        else:
            dic['IN_ATU_PESQUISA'] = None
        if(linha[812:820].isalnum()):
            dic['IN_BOLSA_PESQUISA'] = linha[812:820] == ' 1'
        else:
            dic['IN_BOLSA_PESQUISA'] =None
        if(linha[820:828].isalnum()):
            dic['IN_SUBSTITUTO'] = linha[820:828] == ' 1'
        else:
            dic['IN_SUBSTITUTO'] = None
        if(linha[828:836].isalnum()):
            dic['IN_EXERCICIO_DT_REF'] = linha[828:836] == ' 1'
        else:
            dic['IN_EXERCICIO_DT_REF'] = None
        if(linha[836:844].isalnum()):
            dic['IN_VISITANTE'] = linha[836:844] == ' 1'
        else:
            dic['IN_VISITANTE'] =None
        if(linha[844:852].isalnum()):
            dic['IN_VISITANTE_IFES_VINCULO'] = linha[844:852] == ' 1'
        else:
            dic['IN_VISITANTE_IFES_VINCULO'] = None
        print(dic)
       
    file.close()

