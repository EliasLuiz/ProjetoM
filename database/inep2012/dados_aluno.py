'''
realiza a leitura do arquivo /DADOS/ALUNO.txt
cria uma tabela no banco e salva os dados lidos
'''

from database import db
import codecs


def txt2db(diretorio):
    
    #limpa/cria as tabelas a serem usadas
    db.commit()
    db.query("DROP TABLE IF EXISTS INEP2012.ALUNO")
    db.query("""CREATE TABLE INEP2012.ALUNO(
        CO_ALUNO BIGINT,
        CO_CURSO INT,
        CO_ALUNO_CURSO INT,
        CO_COR_RACA_ALUNO INT,
        DS_COR_RACA_ALUNO VARCHAR(24),
        IN_SEXO_ALUNO SMALLINT,
        DS_SEXO_ALUNO VARCHAR(9), 
        NU_ANO_ALUNO_NASC INT, 
        NU_MES_ALUNO_NASC INT,
        NU_DIA_ALUNO_NASC INT,
        NU_IDADE_ALUNO INT, 
        CO_NACIONALIDADE_ALUNO INT, 
        DS_NACIONALIDADE_ALUNO VARCHAR(48),
        CO_PAIS_ORIGEM_ALUNO INT, 
        DS_PAIS_ORIGEM_ALUNO VARCHAR(80), 
        CO_MUNICIPIO_NASCIMENTO INT, 
        DS_MUNICIPIO_NASCIMENTO VARCHAR(150),
        CO_ALUNO_SITUACAO INT, 
        DS_ALUNO_SITUACAO VARCHAR(41), 
        IN_ALUNO_DEF_TGD_SUPER BOOLEAN,
        IN_DEF_AUDITIVA BOOLEAN, 
        IN_DEF_FISICA BOOLEAN, 
        IN_DEF_INTELECTUAL BOOLEAN, 
        IN_DEF_MULTIPLA BOOLEAN, 
        IN_DEF_SURDEZ BOOLEAN,
        IN_DEF_SURDOCEGUEIRA BOOLEAN, 
        IN_DEF_BAIXA_VISAO BOOLEAN, 
        IN_DEF_SUPERDOTACAO BOOLEAN, 
        IN_TGD_AUTISMO_INFANTIL BOOLEAN,
        IN_TGD_SINDROME_ASPERGER BOOLEAN, 
        IN_TGD_SINDROME_RETT BOOLEAN, 
        IN_TGD_TRANSTOR_DESINTEGRATIVO BOOLEAN,
        DT_INGRESSO_CURSO VARCHAR(38), 
        IN_RESERVA_VAGAS BOOLEAN, 
        IN_FINANC_ESTUDANTIL BOOLEAN, 
        IN_ING_VESTIBULAR BOOLEAN,
        IN_ING_ENEM BOOLEAN, 
        IN_ING_OUTRO_TIPO_SELECAO BOOLEAN, 
        IN_ING_CONVENIO_PEC_G BOOLEAN, 
        IN_ING_OUTRA_FORMA BOOLEAN,
        IN_RESERVA_ETNICO BOOLEAN, 
        IN_RESERVA_DEFICIENCIA BOOLEAN, 
        IN_RES_RENDA_FAMILIAR BOOLEAN, 
        IN_RESERVA_OUTROS BOOLEAN,
        IN_FIN_REEMB_FIES BOOLEAN,
        IN_FIN_REEMB_ESTADUAL BOOLEAN, 
        IN_FIN_REEMB_MUNICIPAL BOOLEAN, 
        IN_FIN_REEMB_PROG_IES BOOLEAN,
        IN_FIN_REEMB_ENT_EXTERNA BOOLEAN, 
        IN_FIN_REEMB_OUTRA BOOLEAN, 
        IN_FIN_NAOREEMB_PROUNI_INTEGR BOOLEAN,
        IN_FIN_NAOREEMB_PROUNI_PARCIAL BOOLEAN, 
        IN_FIN_NAOREEMB_ESTADUAL BOOLEAN, 
        IN_FIN_NAOREEMB_MUNICIPAL BOOLEAN,
        IN_FIN_NAOREEMB_PROG_IES BOOLEAN, 
        IN_FIN_NAOREEMB_ENT_EXTERNA BOOLEAN, 
        IN_FIN_NAOREEMB_OUTRA BOOLEAN, 
        IN_APOIO_SOCIAL BOOLEAN,
        IN_APOIO_ALIMENTACAO BOOLEAN, 
        IN_APOIO_BOLSA_PERMANENCIA BOOLEAN, 
        IN_APOIO_BOLSA_TRABALHO BOOLEAN,
        IN_APOIO_MATERIAL_DIDATICO BOOLEAN, 
        IN_APOIO_MORADIA BOOLEAN, 
        IN_APOIO_TRANSPORTE BOOLEAN,
        IN_ATIVIDADE_EXTRACURRICULAR BOOLEAN, 
        IN_COMPL_ESTAGIO BOOLEAN, 
        IN_COMPL_EXTENSAO BOOLEAN, 
        IN_COMPL_MONITORIA BOOLEAN,
        IN_COMPL_PESQUISA BOOLEAN, 
        IN_BOLSA_ESTAGIO BOOLEAN, 
        IN_BOLSA_EXTENSAO BOOLEAN, 
        IN_BOLSA_MONITORIA BOOLEAN,
        IN_BOLSA_PESQUISA BOOLEAN, 
        TP_PROCEDE_EDUC_PUBLICA INT, 
        NU_SEMESTRE_CONCLUSAO INT, 
        IN_ALUNO_PARFOR BOOLEAN,
        IN_MATRICULA BOOLEAN, 
        IN_CONCLUINTE BOOLEAN, 
        IN_INGRESSO_TOTAL BOOLEAN, 
        IN_INGRESSO_PROCESSO_SELETIVO BOOLEAN,
        IN_INGRESSO_OUTRAS_FORMAS BOOLEAN, 
        ANO_INGRESSO INT);""")
        
    firstExec = True
    
    for linha in codecs.open(diretorio + "/ALUNO.txt", "r", 'latin-1'):
        
        dic = {}
        
        #LEITURA DO ARQUIVO
        ############### DADOS DA IES ################
        #dic['CO_IES'] = linha[0:8]
        #dic['NO_IES'] = linha[8:208].strip()
        #dic['CO_CATEGORIA_ADMINISTRATIVA'] = linha[208:216]
        #dic['DS_CATEGORIA_ADMINISTRATIVA'] = linha[216:316].strip()
        #dic['CO_ORGANIZACAO_ACADEMICA'] = linha[316:324]
        #dic['DS_ORGANIZACAO_ACADEMICA'] = linha[324:424].strip()
        ############### DADOS DO CURSO ################
        dic['CO_CURSO'] = linha[424:432]
        #dic['NO_CURSO'] = linha[432:632].strip()
        #dic['CO_CURSO_POLO'] = linha[632:640]
        #dic['CO_TURNO_ALUNO'] = linha[640:648]
        #dic['DS_TURNO_ALUNO'] = linha[648:673].strip()
        #dic['CO_GRAU_ACADEMICO'] = linha[673:681]
        #dic['DS_GRAU_ACADEMICO'] = linha[681:693].strip()
        #dic['CO_MODALIDADE_ENSINO'] = linha[693:701]
        #dic['DS_MODALIDADE_ENSINO'] = linha[701:712].strip()
        #dic['CO_NIVEL_ACADEMICO'] = linha[712:720]
        #dic['DS_NIVEL_ACADEMICO'] = linha[720:753].strip()
        ############### DADOS DO ALUNO ################
        dic['CO_ALUNO_CURSO'] = linha[753:761]
        dic['CO_ALUNO'] = linha[761:774]
        dic['CO_COR_RACA_ALUNO'] = linha[774:782]
        dic['DS_COR_RACA_ALUNO'] = linha[782:806].strip()  
        dic['IN_SEXO_ALUNO'] = linha[806:814]
        dic['DS_SEXO_ALUNO'] = linha[814:823].strip()
        dic['NU_ANO_ALUNO_NASC'] = linha[823:827]
        dic['NU_MES_ALUNO_NASC'] = linha[827:829]
        dic['NU_DIA_ALUNO_NASC'] = linha[829:831]
        dic['NU_IDADE_ALUNO'] = linha[831:839]
        dic['CO_NACIONALIDADE_ALUNO'] = linha[839:847]
        dic['DS_NACIONALIDADE_ALUNO'] = linha[847:895].strip()
        dic['CO_PAIS_ORIGEM_ALUNO'] = linha[895:903]
        dic['DS_PAIS_ORIGEM_ALUNO'] = linha[903:983].strip()
        #dic['CO_UF_NASCIMENTO'] = linha[983:991]
        #dic['DS_UF_NASCIMENTO'] = linha[991:1021].strip()
        try:
            dic['CO_MUNICIPIO_NASCIMENTO'] = int(linha[1021:1029])
        except:
            dic['CO_MUNICIPIO_NASCIMENTO'] = None
        dic['DS_MUNICIPIO_NASCIMENTO'] = linha[1029:1179].strip()
        dic['CO_ALUNO_SITUACAO'] = linha[1179:1187]
        dic['DS_ALUNO_SITUACAO'] = linha[1187:1228].strip()
        dic['IN_ALUNO_DEF_TGD_SUPER'] = linha[1228:1236] == '       1'
        dic['IN_DEF_AUDITIVA'] = linha[1236:1244] == '       1'
        dic['IN_DEF_FISICA'] = linha[1244:1252] == '       1'
        dic['IN_DEF_INTELECTUAL'] = linha[1252:1260] == '       1'
        dic['IN_DEF_MULTIPLA'] = linha[1260:1268] == '       1'
        dic['IN_DEF_SURDEZ'] = linha[1268:1276] == '       1'
        dic['IN_DEF_SURDOCEGUEIRA'] = linha[1276:1284] == '       1'
        dic['IN_DEF_BAIXA_VISAO'] = linha[1284:1292] == '       1'
        dic['IN_DEF_SUPERDOTACAO'] = linha[1292:1300] == '       1'
        dic['IN_TGD_AUTISMO_INFANTIL'] = linha[1300:1308] == '       1'
        dic['IN_TGD_SINDROME_ASPERGER'] = linha[1308:1316] == '       1'
        dic['IN_TGD_SINDROME_RETT'] = linha[1316:1324] == '       1'
        dic['IN_TGD_TRANSTOR_DESINTEGRATIVO'] = linha[1324:1332] == '       1'
        dic['DT_INGRESSO_CURSO'] = linha[1332:1370].split()
        dic['IN_RESERVA_VAGAS'] = linha[1370:1378] == '       1'
        dic['IN_FINANC_ESTUDANTIL'] = linha[1378:1386] == '       1'
        dic['IN_ING_VESTIBULAR'] = linha[1386:1394] == '       1'
        dic['IN_ING_ENEM'] = linha[1394:1402] == '       1'
        dic['IN_ING_OUTRO_TIPO_SELECAO'] = linha[1402:1410] == '       1'
        dic['IN_ING_CONVENIO_PEC_G'] = linha[1410:1418] == '       1'
        dic['IN_ING_OUTRA_FORMA'] = linha[1418:1426] == '       1'
        dic['IN_RESERVA_ETNICO'] = linha[1426:1434] == '       1'
        dic['IN_RESERVA_DEFICIENCIA'] = linha[1434:1442] == '       1'
        dic['IN_RES_RENDA_FAMILIAR'] = linha[1442:1450] == '       1'
        dic['IN_RESERVA_OUTROS'] = linha[1450:1458] == '       1'
        dic['IN_FIN_REEMB_FIES'] = linha[1458:1466] == '       1'
        dic['IN_FIN_REEMB_ESTADUAL'] = linha[1466:1474] == '       1'
        dic['IN_FIN_REEMB_MUNICIPAL'] = linha[1474:1482] == '       1'
        dic['IN_FIN_REEMB_PROG_IES'] = linha[1482:1490] == '       1'
        dic['IN_FIN_REEMB_ENT_EXTERNA'] = linha[1490:1498] == '       1'
        dic['IN_FIN_REEMB_OUTRA'] = linha[1498:1506] == '       1'
        dic['IN_FIN_NAOREEMB_PROUNI_INTEGR'] = linha[1506:1514] == '       1'
        dic['IN_FIN_NAOREEMB_PROUNI_PARCIAL'] = linha[1514:1522] == '       1'
        dic['IN_FIN_NAOREEMB_ESTADUAL'] = linha[1522:1530] == '       1'
        dic['IN_FIN_NAOREEMB_MUNICIPAL'] = linha[1530:1538] == '       1'
        dic['IN_FIN_NAOREEMB_PROG_IES'] = linha[1538:1546] == '       1'
        dic['IN_FIN_NAOREEMB_ENT_EXTERNA'] = linha[1546:1554] == '       1'
        dic['IN_FIN_NAOREEMB_OUTRA'] = linha[1554:1562] == '       1'
        dic['IN_APOIO_SOCIAL'] = linha[1562:1570] == '       1'
        dic['IN_APOIO_ALIMENTACAO'] = linha[1570:1578] == '       1'
        dic['IN_APOIO_BOLSA_PERMANENCIA'] = linha[1578:1586] == '       1'
        dic['IN_APOIO_BOLSA_TRABALHO'] = linha[1586:1594] == '       1'
        dic['IN_APOIO_MATERIAL_DIDATICO'] = linha[1594:1602] == '       1'
        dic['IN_APOIO_MORADIA'] = linha[1602:1610] == '       1'
        dic['IN_APOIO_TRANSPORTE'] = linha[1610:1618] == '       1'
        dic['IN_ATIVIDADE_EXTRACURRICULAR'] = linha[1618:1626] == '       1'
        dic['IN_COMPL_ESTAGIO'] = linha[1626:1634] == '       1'
        dic['IN_COMPL_EXTENSAO'] = linha[1634:1642] == '       1'
        dic['IN_COMPL_MONITORIA'] = linha[1642:1650] == '       1'
        dic['IN_COMPL_PESQUISA'] = linha[1650:1658] == '       1'
        dic['IN_BOLSA_ESTAGIO'] = linha[1658:1666] == '       1'
        dic['IN_BOLSA_EXTENSAO'] = linha[1666:1674] == '       1'
        dic['IN_BOLSA_MONITORIA'] = linha[1674:1682] == '       1'
        dic['IN_BOLSA_PESQUISA'] = linha[1682:1690] == '       1'
        try:
            dic['TP_PROCEDE_EDUC_PUBLICA'] = int(linha[1690:1698])
        except:
            dic['TP_PROCEDE_EDUC_PUBLICA'] = None
        try:
            dic['NU_SEMESTRE_CONCLUSAO'] = int(linha[1698:1706])
        except:
            dic['NU_SEMESTRE_CONCLUSAO'] = None
        dic['IN_ALUNO_PARFOR'] = linha[1706:1714] == '       1'
        ############### VARIAVEIS DERIVADAS ################
        dic['IN_MATRICULA'] = linha[1714:1722] == '       1'
        dic['IN_CONCLUINTE'] = linha[1722:1730] == '       1'
        dic['IN_INGRESSO_TOTAL'] = linha[1730:1738] == '       1'
        dic['IN_INGRESSO_PROCESSO_SELETIVO'] = linha[1738:1746] == '       1'
        dic['IN_INGRESSO_OUTRAS_FORMAS'] = linha[1746:1754] == '       1'
        try:
            dic['ANO_INGRESSO'] = int(linha[1754:1758])
        except:
            dic['ANO_INGRESSO'] = None
        
        
        
        #CONVERSAO DE LATIN-1 PARA UTF-8
        db.latin2utf(dic)



        #INSERCAO NO BANCO DE DADOS
        if firstExec:
            db.prepareInsert('ALUNO', 'INEP2012.ALUNO', dic)
            db.commit()
            firstExec = False
            
        db.usePreparedInsert('ALUNO', dic)
        
        
    db.commit()
    
    
    
    
    
    
    
        
'''
        db.query("INSERT INTO ALUNO(CO_IES, CO_CURSO, CO_ALUNO_CURSO, CO_ALUNO, CO_COR_RACA_ALUNO,\
        DS_COR_RACA_ALUNO, IN_SEXO_ALUNO, DS_SEXO_ALUNO, NU_ANO_ALUNO_NASC, NU_MES_ALUNO_NASC,\
        NU_DIA_ALUNO_NASC, NU_IDADE_ALUNO, CO_NACIONALIDADE_ALUNO, DS_NACIONALIDADE_ALUNO,\
        CO_PAIS_ORIGEM_ALUNO, DS_PAIS_ORIGEM_ALUNO, CO_UF_NASCIMENTO, DS_UF_NASCIMENTO,\
        CO_MUNICIPIO_NASCIMENTO, CO_ALUNO_SITUACAO, DS_ALUNO_SITUACAO, IN_ALUNO_DEF_TGD_SUPER,\
        IN_DEF_AUDITIVA, IN_DEF_FISICA, IN_DEF_INTELECTUAL, IN_DEF_MULTIPLA, IN_DEF_SURDEZ,\
        IN_DEF_SURDOCEGUEIRA, IN_DEF_BAIXA_VISAO, IN_DEF_SUPERDOTACAO, IN_TGD_AUTISMO_INFANTIL,\
        IN_TGD_SINDROME_ASPERGER, IN_TGD_SINDROME_RETT, IN_TGD_TRANSTOR_DESINTEGRATIVO,\
        DT_INGRESSO_CURSO, IN_RESERVA_VAGAS, IN_FINANC_ESTUDANTIL, IN_ING_VESTIBULAR,\
        IN_ING_ENEM, IN_ING_OUTRO_TIPO_SELECAO, IN_ING_CONVENIO_PEC_G, IN_ING_OUTRA_FORMA,\
        IN_RESERVA_ETNICO, IN_RESERVA_DEFICIENCIA, IN_RES_RENDA_FAMILIAR, IN_RESERVA_OUTROS,\
        IN_FIN_REEMB_FIES, IN_FIN_REEMB_ESTADUAL, IN_FIN_REEMB_MUNICIPAL, IN_FIN_REEMB_PROG_IES,\
        IN_FIN_REEMB_ENT_EXTERNA, IN_FIN_REEMB_OUTRA, IN_FIN_NAOREEMB_PROUNI_INTEGR,\
        IN_FIN_NAOREEMB_PROUNI_PARCIAL, IN_FIN_NAOREEMB_ESTADUAL, IN_FIN_NAOREEMB_MUNICIPAL,\
        IN_FIN_NAOREEMB_PROG_IES, IN_FIN_NAOREEMB_ENT_EXTERNA, IN_FIN_NAOREEMB_OUTRA, IN_APOIO_SOCIAL,\
        IN_APOIO_ALIMENTACAO, IN_APOIO_BOLSA_PERMANENCIA, IN_APOIO_BOLSA_TRABALHO,\
        IN_APOIO_MATERIAL_DIDATICO, IN_APOIO_MORADIA, IN_APOIO_TRANSPORTE,\
        IN_ATIVIDADE_EXTRACURRICULAR, IN_COMPL_ESTAGIO, IN_COMPL_EXTENSAO, IN_COMPL_MONITORIA,\
        IN_COMPL_PESQUISA, IN_BOLSA_ESTAGIO, IN_BOLSA_EXTENSAO, IN_BOLSA_MONITORIA,\
        IN_BOLSA_PESQUISA, TP_PROCEDE_EDUC_PUBLICA, NU_SEMESTRE_CONCLUSAO, IN_ALUNO_PARFOR,\
        IN_MATRICULA, IN_CONCLUINTE, IN_INGRESSO_TOTAL, IN_INGRESSO_PROCESSO_SELETIVO,\
        IN_INGRESSO_OUTRAS_FORMAS, ANO_INGRESSO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
        %s,%s,%s,%s,%s,%s)" % (dic['CO_IES'], dic['CO_CURSO'], dic['CO_ALUNO_CURSO'], dic['CO_ALUNO'],\
        dic['CO_COR_RACA_ALUNO'], dic['DS_COR_RACA_ALUNO'], dic['IN_SEXO_ALUNO'], dic['DS_SEXO_ALUNO'],\
        dic['NU_ANO_ALUNO_NASC'], dic['NU_MES_ALUNO_NASC'], dic['NU_DIA_ALUNO_NASC'],\
        dic['NU_IDADE_ALUNO'], dic['CO_NACIONALIDADE_ALUNO'], dic['DS_NACIONALIDADE_ALUNO'],\
        dic['CO_PAIS_ORIGEM_ALUNO'], dic['DS_PAIS_ORIGEM_ALUNO'], dic['CO_UF_NASCIMENTO'],\
        dic['DS_UF_NASCIMENTO'], dic['CO_MUNICIPIO_NASCIMENTO'], dic['CO_ALUNO_SITUACAO'],\
        dic['DS_ALUNO_SITUACAO'], dic['IN_ALUNO_DEF_TGD_SUPER'], dic['IN_DEF_AUDITIVA'],\
        dic['IN_DEF_FISICA'], dic['IN_DEF_INTELECTUAL'], dic['IN_DEF_MULTIPLA'], dic['IN_DEF_SURDEZ'],\
        dic['IN_DEF_SURDOCEGUEIRA'], dic['IN_DEF_BAIXA_VISAO'], dic['IN_DEF_SUPERDOTACAO'],\
        dic['IN_TGD_AUTISMO_INFANTIL'], dic['IN_TGD_SINDROME_ASPERGER'], dic['IN_TGD_SINDROME_RETT'],\
        dic['IN_TGD_TRANSTOR_DESINTEGRATIVO'], dic['DT_INGRESSO_CURSO'], dic['IN_RESERVA_VAGAS'],\
        dic['IN_FINANC_ESTUDANTIL'], dic['IN_ING_VESTIBULAR'], dic['IN_ING_ENEM'],\
        dic['IN_ING_OUTRO_TIPO_SELECAO'], dic['IN_ING_CONVENIO_PEC_G'], dic['IN_ING_OUTRA_FORMA'],\
        dic['IN_RESERVA_ETNICO'], dic['IN_RESERVA_DEFICIENCIA'], dic['IN_RES_RENDA_FAMILIAR'],\
        dic['IN_RESERVA_OUTROS'], dic['IN_FIN_REEMB_FIES'], dic['IN_FIN_REEMB_ESTADUAL'],\
        dic['IN_FIN_REEMB_MUNICIPAL'], dic['IN_FIN_REEMB_PROG_IES'], dic['IN_FIN_REEMB_ENT_EXTERNA'],\
        dic['IN_FIN_REEMB_OUTRA'], dic['IN_FIN_NAOREEMB_PROUNI_INTEGR'],\
        dic['IN_FIN_NAOREEMB_PROUNI_PARCIAL'], dic['IN_FIN_NAOREEMB_ESTADUAL'],\
        dic['IN_FIN_NAOREEMB_MUNICIPAL'], dic['IN_FIN_NAOREEMB_PROG_IES'],\
        dic['IN_FIN_NAOREEMB_ENT_EXTERNA'], dic['IN_FIN_NAOREEMB_OUTRA'], dic['IN_APOIO_SOCIAL'],\
        dic['IN_APOIO_ALIMENTACAO'], dic['IN_APOIO_BOLSA_PERMANENCIA'], dic['IN_APOIO_BOLSA_TRABALHO'],\
        dic['IN_APOIO_MATERIAL_DIDATICO'], dic['IN_APOIO_MORADIA'], dic['IN_APOIO_TRANSPORTE'],\
        dic['IN_ATIVIDADE_EXTRACURRICULAR'], dic['IN_COMPL_ESTAGIO'], dic['IN_COMPL_EXTENSAO'],\
        dic['IN_COMPL_MONITORIA'], dic['IN_COMPL_PESQUISA'], dic['IN_BOLSA_ESTAGIO'],\
        dic['IN_BOLSA_EXTENSAO'], dic['IN_BOLSA_MONITORIA'], dic['IN_BOLSA_PESQUISA'],\
        dic['TP_PROCEDE_EDUC_PUBLICA'], dic['NU_SEMESTRE_CONCLUSAO'], dic['IN_ALUNO_PARFOR'],\
        dic['IN_MATRICULA'], dic['IN_CONCLUINTE'], dic['IN_INGRESSO_TOTAL'],\
        dic['IN_INGRESSO_PROCESSO_SELETIVO'], dic['IN_INGRESSO_OUTRAS_FORMAS'], dic['ANO_INGRESSO']))
'''