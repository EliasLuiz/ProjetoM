'''

'''

from database import db
import codecs


def txt2db(arquivo):
    #criando tabelas
    db.commit()
    db.query("""CREATE TABLE IF NOT EXISTS CAGED.DADOS(
    CO_ADM_DESL INT,
    NO_ADM_DESL VARCHAR(12),
    ANO INT,
    MES INT,
    CO_MUNICIPIO INT,
    ANO_COMP INT,
    CO_CBO2002 INT,
    CO_CLASSE10 INT,
    CO_CLASSE20 INT,
    CO_SUBCLASSE INT,
    CO_FX_EMP_JAN INT,
    NO_FX_EMP_JAN VARCHAR(12),
    CO_GRAU_INSTR INT,
    NO_GRAU_INSTR VARCHAR(23),
    HORAS_CONTP INT,
    CO_IBGE_SUBSETOR INT,
    NO_IBGE_SUBSETOR VARCHAR(67),
    IDADE_P INT,
    IND_APRENDIZ BOOLEAN,
    PORT_DEFIC BOOLEAN,
    CO_RACA_COR INT,
    NO_RACA_COR VARCHAR(16),
    SAL_MENSAL FLOAT,
    SALDO_MOV INT,
    CO_SEXO INT,
    NO_SEXO VARCHAR(9),
    TEMP_EMP_P FLOAT,
    CO_TIPO_ESTBL INT,
    NO_TIPO_ESTBL VARCHAR(16),
    CO_TP_DEFIC INT,
    NO_TP_DEFIC VARCHAR(20),
    CO_TP_MOV_DESAG INT,
    NO_TP_MOV_DESAG VARCHAR(43)
    )""")

    firstExec = True
    primeiraLinha = True
    ano = 0
    
    for linha in codecs.open(arquivo, "r", "latin-1"):

        try:
            
            if primeiraLinha:
                primeiraLinha = False
                continue
            
            dic = {}
            
            #leitura do arquivo
            dados = linha.split(';')
        
            try:
                dic['co_adm_desl'] = int(dados[0])
            except:
                dic['co_adm_desl'] = 1 if dados[0] == 'ADMITIDOS' else '2'
            
            dic['no_adm_desl'] = 'Admissao' if dic['co_adm_desl'] == 1 else 'Desligamento'
        
            try:
                dic['ano'] = int(dados[1][0:4])
                dic['mes'] = int(dados[1][4:6])
            except:
                dic['mes'] = int(dados[1][0:2])
                dic['ano'] = int(dados[1][3:7])
            ano = dic['ano']
            
            if len(dados[2]) == 6:
                dic['co_municipio'] = int(dados[2])
            else:
                dic['co_municipio'] = None
                
                #####################################################
        
            dic['ano_comp'] = int(dados[3]) if dados[3] != '-1' else None
        
            dic['co_cbo2002'] = int(dados[4].replace('CBO ', '')) if dados[4] != '-1' else None
        
            dic['co_classe10'] = int(dados[5]) if dados[5] != '-1' else None
        
            dic['co_classe20'] = int(dados[6]) if dados[6] != '-1' else None
        
            dic['co_subclasse'] = int(dados[7]) if dados[7] != '-1' else None
        
            try:
                dic['co_fx_emp_jan'] = int(dados[8]) if dados[8] != '-1' else None
            except:
                dic['no_fx_emp_jan'] = {
                    'ate 4' : 1,
                    'de 5 a 9' : 2,
                    'de 10 a 19' : 3,
                    'de 20 a 49' : 4,
                    'de 50 a 99' : 5,
                    'de 100 a 249' : 6,
                    'de 250 a 499' : 7,
                    'de 500 a 999' : 8,
                    '1000 ou mais' : 9,
                    'ignorado' : -1
                }[dados[8].lower()]
            
            dic['no_fx_emp_jan'] = {
                1: 'Ate 4',
                2: 'De 5 a 9',
                3: 'De 10 a 19',
                4: 'De 20 a 49',
                5: 'De 50 a 99',
                6: 'De 100 a 249',
                7: 'De 250 a 499',
                8: 'De 500 a 999',
                9: '1000 ou mais',
                -1: 'Ignorado'
            }[dic['no_fx_emp_jan']]
        
            dic['co_grau_instr'] = int(dados[9]) if dados[9] != -1 else None
            dic['no_grau_instr'] = {
                1: 'Analfabeto',
                2: 'Ate 5a Incompleto',
                3: '5a Completo Fundamental',
                4: '6a a 9a Fundamental',
                5: 'Fundamental Completo',
                6: 'Medio Incompleto',
                7: 'Medio Completo',
                8: 'Superior Incompleto',
                9: 'Superior Completo',
                10: 'Mestrado',
                11: 'Doutorado',
                -1: 'Ignorado'
            }[int(dados[9])]
        
            dic['horas_contp'] = int(dados[10])
            
            # ATE AQUI OK CAGED 2009
            
            try:
                int(dados[11])
            except:
                dados[11] = {
                    'INST FINANC':18,
                    'ADM TEC PROF':19,
                    'AGRICULTURA':25,
                    'COM VAREJ':16,
                    'ALOJ COMUNIC':21,
                    'ENSINO':23,
                    'CONSTR CIVIL':15,
                    'MED ODON VET':22,
                    'TRAN E COMUN':20,
                    'COM ATACAD':17,
                    'IND TEXTIL':11,
                    'PAPEL E GRAF':8,
                    'ALIM E BEB':13,
                    'IND METALURG':3,
                    'IND MECANICA':4,
                    'BOR FUM COUR':9,
                    'MIN NAO MET':2,
                    'ELET E COMUN':5,
                    'MAD E MOBIL':7,
                    'IND QUIMICA':10,
                    'MAT TRANSP':6,
                    'EXTR MINERAL':1,
                    'IND CALCADOS':12,
                    'ADM PUBLICA':24,
                    'SER UTIL PUB':14
                }[dados[11]]
            
            dic['co_ibge_subsetor'] = int(dados[11]) if dados[11] != '-1' else None
            dic['no_ibge_subsetor'] = {
                1: 'Extrativa mineral',
                2: 'Industria de produtos minerais nao metalicos',
                3: 'Industria metalurgica',
                4: 'Industria mecanica',
                5: 'Industria do material eletrico e de comunicacoes',
                6: 'Industria do material de transporte',
                7: 'Industria da madeira e do mobiliario',
                8: 'Industria do papel, papelao, editorial e grafica',
                9: 'Ind. da borracha, fumo, couros, peles, similares, ind. diversas',
                10: 'Ind. quimica de produtos farmaceuticos, veterinarios, perfumaria',
                11: 'Industria textil do vestuario e artefatos de tecidos',
                12: 'Industria de calcados',
                13: 'Industria de produtos alimenticios, bebidas e alcool etilico',
                14: 'Servicos industriais de utilidade publica',
                15: 'Construcao civil',
                16: 'Comercio varejista',
                17: 'Comercio atacadista',
                18: 'Instituicoes de credito, seguros e capitalizacao',
                19: 'Com. e administracao de imoveis, dicores mobiliarios, serv. Tecnico',
                20: 'Transportes e comunicacoes',
                21: 'Serv. de alojamento, alimentacao, reparacao, manutencao, redacao',
                22: 'Servicos medicos, odontologicos e veterinarios',
                23: 'Ensino',
                24: 'Administracao publica direta e autarquica',
                25: 'Agricultura, silvicultura, criacao de animais, extrativismo vegetal',
                -1: 'Ignorado'
            }[int(dados[11])]
        
            dic['idade_p'] = int(dados[12])
        
            dic['ind_aprendiz'] = int(dados[13]) == 1
        
            dic['port_defic'] = int(dados[14]) == 1
        
            dic['co_raca_cor'] = int(dados[15]) if dados[15] != '-1' else None
            dic['no_raca_cor'] = {
                1: 'Indigena',
                2: 'Branca',
                4: 'Preta',
                6: 'Amarela',
                8: 'Parda',
                9: 'Nao Identificado',
                -1: 'Ignorado'
            }[int(dados[15])]
        
            dic['sal_mensal'] = float(dados[16].replace(',', '.'))
            
            dic['saldo_mov'] = int(dados[17])
        
            dic['co_sexo'] = int(dados[18])
            dic['no_sexo'] = {
                1: 'Masculino',
                2: 'Feminino',
                -1: 'Ignorado'
            }[int(dados[18])]
        
            dic['temp_emp_p'] = float(dados[19].replace(',', '.'))
        
            dic['co_tipo_estbl'] = int(dados[20]) if dados[20] != '-1' else None
            dic['no_tipo_estbl'] = {
                1: 'CNPJ',
                3: 'CEI',
                9: 'Nao identificado',
                -1: 'Ignorado'
            }[int(dados[20])]
        
            dic['co_tp_defic'] = int(dados[21]) if dados[21] != '-1' else None
            dic['no_tp_defic'] = {
                1: 'Fisica',
                2: 'Auditiva',
                3: 'Visual',
                4: 'Intelectual (Mental)',
                5: 'Multipla',
                6: 'Reabilitado',
                0: 'Nao Deficiente',
                -1: 'Ignorado'
            }[int(dados[21])]
        
            dic['co_tp_mov_desag'] = int(dados[22]) if dados[22] != '-1' else None
            dic['no_tp_mov_desag'] = {
                1: 'Admissao por Primeiro Emprego',
                2: 'Admissao por Reemprego',
                3: 'Admissao por Transferencia',
                4: 'Desligamento por Demissao sem Justa Causa',
                5: 'Desligamento por Demissao com Justa Causa',
                6: 'Desligamento a Pedido',
                7: 'Desligamento por Aposentadoria',
                8: 'Desligamento por Morte',
                9: 'Desligamento por Transferencia',
                10: 'Admissao por Reintegracao',
                11: 'Desligamento por Termino de Contrato',
                25: 'Contrato Trabalho Prazo Determinado',
                43: 'Termino Contrato Trabalho Prazo Determinado',
                -1: 'Ignorado'
            }[int(dados[22])]
            '''
            dic['co_uf'] = int(dados[23]) if dados[23] != '-1' else None
            dic['no_uf'] = {
                11: 'Rondonia',
                12: 'Acre',
                13: 'Amazonas',
                14: 'Roraima',
                15: 'Para',
                16: 'Amapa',
                17: 'Tocantins',
                21: 'Maranhao',
                22: 'Piaui',
                23: 'Ceara',
                24: 'Rio Grande do Norte',
                25: 'Paraiba',
                26: 'Pernambuco',
                27: 'Alagoas',
                28: 'Sergipe',
                29: 'Bahia',
                31: 'Minas Gerais',
                32: 'Espirito Santo',
                33: 'Rio de Janeiro',
                35: 'Sao Paulo',
                41: 'Parana',
                42: 'Santa Catarina',
                43: 'Rio Grande do Sul',
                50: 'Mato Grosso do Sul',
                51: 'Mato Grosso',
                52: 'Goias',
                53: 'Distrito Federal'
            }[int(dados[23])]
            '''
            db.latin2utf(dic)
            
            print 'first exec'
            
            if firstExec:    
                #checa se particao ja existe
                filhos = [i[1] for i in db.query("""
                        SELECT cn.nspname AS schema_child, c.relname AS child, pn.nspname AS schema_parent, p.relname AS parent
                        FROM pg_inherits 
                        JOIN pg_class AS c ON (inhrelid=c.oid)
                        JOIN pg_class as p ON (inhparent=p.oid)
                        JOIN pg_namespace pn ON pn.oid = p.relnamespace
                        JOIN pg_namespace cn ON cn.oid = c.relnamespace
                        WHERE p.relname = 'dados' and pn.nspname = 'caged';""")]
                #se nao existe cria particao
                if ("dados%s" % ano) not in filhos:
                    print 'TABELA %s NAO EXISTE' % ano
                    db.query("CREATE TABLE IF NOT EXISTS CAGED.DADOS%s () INHERITS (CAGED.DADOS);" % ano)
                    db.query("CREATE INDEX indcbo%s ON CAGED.DADOS%s (co_cbo2002);" % (ano, ano))
                    db.query("CREATE INDEX indclasse%s ON CAGED.DADOS%s (co_classe20);" % (ano, ano))
                #se ja existe retira constraint (insercao mais rapida)
                else:
                    print 'TABELA %s EXISTE' % ano
                    db.query("ALTER TABLE CAGED.DADOS%s DROP CONSTRAINT indano;" % ano)
                
                db.prepareInsert("DADOS%s" % ano, "CAGED.DADOS%s" % ano, dic)
                db.commit()
                firstExec = False
                
            db.usePreparedInsert("DADOS%s" % dic['ano'], dic)
            
        except:
            pass
    
    db.query("ALTER TABLE CAGED.DADOS%s ADD CONSTRAINT indano CHECK (ano = %s);" % (ano, ano))
    db.query("REINDEX TABLE CAGED.DADOS%s;" % ano)
    db.commit()