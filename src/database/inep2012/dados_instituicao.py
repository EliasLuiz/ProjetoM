# realiza a leitura do arquivo /DADOS/INSTITUICAO.txt
# cria uma tabela no banco e salva os dados lidos


'''
%%%%%%%%     TESTAR     %%%%%%%%%
'''


from database import db

def txt_to_db(diretorio):
    
    file = open(diretorio + "/DADOS/INSTITUICAO.txt", "r")
    
    for linha in file.readlines():
        
        dic = {}
        
        dic['CO_IES'] = int(linha[0:8])
        dic['NO_IES'] = linha[8:208].strip()
        dic['CO_MANTENEDORA'] = int(linha[208:216])
        dic['CO_CATEGORIA_ADMINISTRATIVA'] = int(linha[216:224])
        dic['DS_CATEGORIA_ADMINISTRATIVA'] = linha[224:324].strip()
        dic['CO_ORGANIZACAO_ACADEMICA'] = int(linha[324:332])
        dic['DS_ORGANIZACAO_ACADEMICA'] = linha[332:432].strip()
        dic['CO_MUNICIPIO_IES'] = int(linha[432:440])
        dic['NO_MUNICIPIO_IES'] = linha[440:590].strip()
        dic['CO_UF_IES'] = int(linha[590:598])
        dic['SGL_UF_IES'] = linha[598:600].strip()
        dic['NO_REGIAO_IES'] = linha[600:630].strip()
        dic['IN_CAPITAL_IES'] = linha[630:638] == ' 1'
        dic['QT_TEC_TOTAL'] = int(linha[638:646])
        dic['QT_TEC_FUND_INCOMP_MASC'] = int(linha[646:654])
        dic['QT_TEC_FUND_INCOMP_FEM'] = int(linha[654:662])
        dic['QT_TEC_FUND_COMP_MASC'] = int(linha[662:670])
        dic['QT_TEC_FUND_COMP_FEM'] = int(linha[670:678])
        dic['QT_TEC_MEDIO_MASC'] = int(linha[678:686])
        dic['QT_TEC_MEDIO_FEM'] = int(linha[686:694])
        dic['QT_TEC_SUPERIOR_MASC'] = int(linha[694:702])
        dic['QT_TEC_SUPERIOR_FEM'] = int(linha[702:710])
        dic['QT_TEC_ESPECIALIZACAO_MASC'] = int(linha[710:718])
        dic['QT_TEC_ESPECIALIZACAO_FEM'] = int(linha[718:726])
        dic['QT_TEC_MESTRADO_MASC'] = int(linha[726:734])
        dic['QT_TEC_MESTRADO_FEM'] = int(linha[734:742])
        dic['QT_TEC_DOUTORADO_MASC'] = int(linha[742:750])
        dic['QT_TEC_DOUTORADO_FEM'] = int(linha[750:758])
        dic['IN_ACESSO_PORTAL_CAPES'] = linha[758:766] == ' 1'
        dic['IN_ACESSO_OUTRAS_BASES'] = linha[766:774] == ' 1'
        dic['IN_REFERENTE'] = int(linha[774:782])
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
        sqlMunicipio="INSERT INTO MUNICIPIO(CO_MUNICIPIO,NO_MUNICIPIO,CO_UF,SGL_UF) "
        sqlMunicipio2="VALUES(%d,%s,%d,%s)"%(dic['CO_MUNICIPIO_IES'],dic['NO_MUNICIPIO_IES'],dic['CO_UF_IES'],dic['SGL_UF_IES'])
        sqlMunicipio=sqlMunicipio+sqlMunicipio2
        db.query(sqlMunicipio)
        sqlIES="INSERT INTO IES(CO_IES,NO_IES,CO_MANTENEDORA,CO_CATEGORIA_ADMINISTRATIVA,DS_CATEGORIA_ADMINISTRATIVA,CO_ORGANIZACAO_ACADEMICA,DS_ORGANIZACAO_ACADEMICA,CO_MUNICIPIO_IES,NO_REGIAO_IES,IN_CAPITAL_IES,QT_TEC_TOTAL,QT_TEC_FUND_INCOMP_MASC,QT_TEC_FUND_INCOMP_FEM,QT_TEC_FUND_COMP_MASC,QT_TEC_FUND_COMP_FEM,QT_TEC_MEDIO_MASC,QT_TEC_MEDIO_FEM,QT_TEC_SUPERIOR_MASC,QT_TEC_SUPERIOR_FEM,QT_TEC_ESPECIALIZACAO_MASC,QT_TEC_ESPECIALIZACAO_FEM,QT_TEC_MESTRADO_MASC,QT_TEC_MESTRADO_FEM,QT_TEC_DOUTORADO_MASC,QT_TEC_DOUTORADO_FEM,IN_ACESSO_PORTAL_CAPES,IN_ACESSO_OUTRAS_BASES,IN_REFERENTE,VL_RECEITA_PROPRIA,VL_TRANSFERENCIA,VL_OUTRA_RECEITA,VL_DES_PESSOAL_REM_DOCENTE,VL_DES_PESSOAL_REM_TECNICO,VL_DES_PESSOAL_ENCARGO,VL_DES_CUSTEIO,VL_DES_INVESTIMENTO,VL_DES_PESQUISA,VL_DES_OUTRAS) "
        sqlIES2="VALUES(%d,%s,%d,%d,%s,%d,%s,%d,%s,%s,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%s,%s,%d,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"%(dic['CO_IES'],dic['NO_IES'],dic['CO_MANTENEDORA'],dic['CO_CATEGORIA_ADMINISTRATIVA'],dic['DS_CATEGORIA_ADMINISTRATIVA'],dic['CO_ORGANIZACAO_ACADEMICA'],dic['DS_ORGANIZACAO_ACADEMICA'],dic['CO_MUNICIPIO_IES'],dic['NO_REGIAO_IES'],dic['IN_CAPITAL_IES'],dic['QT_TEC_TOTAL'],dic['QT_TEC_FUND_INCOMP_MASC'],dic['QT_TEC_FUND_INCOMP_FEM'],dic['QT_TEC_FUND_COMP_MASC'],dic['QT_TEC_FUND_COMP_FEM'],dic['QT_TEC_MEDIO_MASC'],dic['QT_TEC_MEDIO_FEM'],dic['QT_TEC_SUPERIOR_MASC'],dic['QT_TEC_SUPERIOR_FEM'],dic['QT_TEC_ESPECIALIZACAO_MASC'],dic['QT_TEC_ESPECIALIZACAO_FEM'],dic['QT_TEC_MESTRADO_MASC'],dic['QT_TEC_MESTRADO_FEM'],dic['QT_TEC_DOUTORADO_MASC'],dic['QT_TEC_DOUTORADO_FEM'],dic['IN_ACESSO_PORTAL_CAPES'],dic['IN_ACESSO_OUTRAS_BASES'],dic['IN_REFERENTE'],dic['VL_RECEITA_PROPRIA'],dic['VL_TRANSFERENCIA'],dic['VL_OUTRA_RECEITA'],dic['VL_DES_PESSOAL_REM_DOCENTE'],dic['VL_DES_PESSOAL_REM_TECNICO'],dic['VL_DES_PESSOAL_ENCARGO'],dic['VL_DES_CUSTEIO'],dic['VL_DES_INVESTIMENTO'],dic['VL_DES_PESQUISA'],dic['VL_DES_OUTRAS'])
        sqlIES=sqlIES+sqlIES2
        db.query(sqlIES)
    file.close()
