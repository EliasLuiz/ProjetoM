# realiza a leitura do arquivo /DADOS/INSTITUICAO.txt
# cria uma tabela no banco e salva os dados lidos


'''
%%%%%%%%     TESTAR     %%%%%%%%%
'''


from database import db

def txt_to_db(diretorio):
    
    file = open(diretorio + "/DADOS/ALUNO.txt", "r")
    
    for linha in file.readlines():
        
        dic = {}
        
        ############### DADOS DA IES ################
        dic['CO_IES'] = int(linha[0:8])
        dic['NO_IES'] = linha[8:208].strip()
        dic['CO_CATEGORIA_ADMINISTRATIVA'] = int(linha[208:216])
        dic['DS_CATEGORIA_ADMINISTRATIVA'] = linha[216:316].strip()
        dic['CO_ORGANIZACAO_ACADEMICA'] = int(linha[316:324])
        dic['DS_ORGANIZACAO_ACADEMICA'] = linha[324:424].strip()
        ############### DADOS DO CURSO ################
        dic['CO_CURSO'] = int(linha[424:432])
        dic['NO_CURSO'] = linha[432:632].strip()
        dic['CO_CURSO_POLO'] = int(linha[632:640])
        dic['CO_TURNO_ALUNO'] = int(linha[640:648])
        dic['DS_TURNO_ALUNO'] = linha[648:673].strip()
        dic['CO_GRAU_ACADEMICO'] = int(linha[673:681])
        dic['DS_GRAU_ACADEMICO'] = linha[681:693].strip()
        dic['CO_MODALIDADE_ENSINO'] = int(linha[693:701])
        dic['DS_MODALIDADE_ENSINO'] = linha[701:712].strip()
        dic['CO_NIVEL_ACADEMICO'] = int(linha[712:720])
        dic['DS_NIVEL_ACADEMICO'] = linha[720:753].strip()
        ############### DADOS DO ALUNO ################
        dic['CO_ALUNO_CURSO'] = int(linha[753:761])
        dic['CO_ALUNO'] = int(linha[761:774])
        dic['CO_COR_RACA_ALUNO'] = int(linha[774:782])
        dic['DS_COR_RACA_ALUNO'] = linha[782:806].strip()  
        dic['IN_SEXO_ALUNO'] = int(linha[806:814])
        dic['DS_SEXO_ALUNO'] = linha[814:823].strip()
        dic['NU_ANO_ALUNO_NASC'] = int(linha[823:827])
        dic['NU_MES_ALUNO_NASC'] = int(linha[827:829])
        dic['NU_DIA_ALUNO_NASC'] = int(linha[829:831])
        dic['NU_IDADE_ALUNO'] = int(linha[831:839])
        dic['CO_NACIONALIDADE_ALUNO'] = int(linha[839:847])
        dic['DS_NACIONALIDADE_ALUNO'] = linha[847:895].strip()
        dic['CO_PAIS_ORIGEM_ALUNO'] = int(linha[895:903])
        dic['DS_PAIS_ORIGEM_ALUNO'] = linha[903:983].strip()
        dic['CO_UF_NASCIMENTO'] = int(linha[983:991])
        dic['DS_UF_NASCIMENTO'] = linha[991:1021].strip()
        dic['CO_MUNICIPIO_NASCIMENTO'] = int(linha[1021:1029])
        dic['DS_MUNICIPIO_NASCIMENTO'] = linha[1029:1179].strip()
        dic['CO_ALUNO_SITUACAO'] = int(linha[1179:1187])
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
        dic['TP_PROCEDE_EDUC_PUBLICA'] = int(linha[1690:1698])
        dic['NU_SEMESTRE_CONCLUSAO'] = int(linha[1698:1706])
        dic['IN_ALUNO_PARFOR'] = linha[1706:1714] == '       1'
        ############### VARIÁVEIS DERIVADAS ################
        dic['IN_MATRICULA'] = linha[1714:1722] == '       1'
        dic['IN_CONCLUINTE'] = linha[1722:1730] == '       1'
        dic['IN_INGRESSO_TOTAL'] = linha[1730:1738] == '       1'
        dic['IN_INGRESSO_PROCESSO_SELETIVO'] = linha[1738:1746] == '       1'
        dic['IN_INGRESSO_OUTRAS_FORMAS'] = linha[1746:1754] == '       1'
        dic['ANO_INGRESSO'] = int(linha[1754:1758])
        
    file.close()