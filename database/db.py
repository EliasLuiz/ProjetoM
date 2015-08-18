#-*- coding: latin -*-
'''
modulo de interface com a biblioteca do banco (psycopg)
ou seja, e uma abstracao para o banco de dados
facilitando se precisar alterar o banco
'''
import psycopg2 as pg
import sys
import grafo
import codecs





try:
    conn = pg.connect("dbname='projetom' user='projetom' host='localhost' password='maurilio'")
    cur = conn.cursor()
except pg.Error, e:
    #insereErrorLog(e.pgerror)
    sys.exit(1)


#grafos e um dicionario que contem um "grafo" para cada schema do banco
#esse grafo e a lista de adjacencia, representada por um dicionario
#cada entrada desse dicionario representa uma tabela e guarda uma lista com
#as tabelas com as quais ela pode se ligar diretamente
#o objetivo e ser capaz de descobrir quais tabelas sao necessarias para
#  conseguir gerar um determinado sql
grafos = {}

def iniciaSchema(schema):
    '''
    Gera o grafo utilizado para ligar as tabelas
    schema Ã© o schema do BD que serÃ¡ utilizado
    
    Assume que as chaves estrangeiras do banco seguem o padrÃ£o
        int co_tabela, relacionando com a chave primaria da tabela
    '''

    global grafos

    tabelas = [i[2] for i in query('''
        SELECT * FROM information_schema.tables
        WHERE table_schema = ''' + "'" + schema + "'" + '''
        ''')]

    colunas = {}
    for tabela in tabelas:
        colunas[tabela] = [i[3] for i in query('''
            SELECT *
            FROM information_schema.columns
            WHERE table_schema = ''' + "'" + schema + ''''
            AND table_name   = ''' + "'" + tabela + "'")]
            
    #identifica as ligacoes diretas
    ligacoes = {}
    for tabela1 in tabelas:
        ligacoes[tabela1] = []
        for tabela2 in tabelas:
            if tabela2 != tabela1 and ("co_" + tabela2.lower()) in colunas[tabela1]:
                ligacoes[tabela1].append((tabela2, "co_" + tabela2.lower()))
                
    for tabela1 in tabelas:
        for tabela2 in tabelas:
            for (t, c) in ligacoes[tabela1]:
                if t == tabela2 and (tabela1, c) not in ligacoes[tabela2]:
                    ligacoes[tabela2].append((tabela1, c))
    
    grafos[schema] = grafo.Grafo()
    
    for tabela, lig in ligacoes.iteritems():
        grafos[schema].addElemento(tabela, [i[0] for i in lig], [int(query('''
                select count(*) from ''' + schema + "." + i[0])[0][0]) for i in lig], [i[1] for i in lig],
                None, None, None)
    

#funcoes gerais relativas ao banco    
    
def query(sql): #executa uma query sql
    try:
        cur.execute(sql)
    except pg.Error, e:
        insereSqlLog(e.pgerror)
    try:
        return cur.fetchall()
    except:
        return []

def latin2utf(dictionary):
    for i, j in dictionary.iteritems():
        try:
            dictionary[i] = j.strip()
        except:
            None
        try:
            minusculo = ('á', 'à', 'â', 'ã', 'é', 'ê', 'í', 'ó', 'ô', 'õ', 'ú', 'ü', 'ç')
            maiusculo = ('Á', 'À', 'Â', 'Ã', 'É', 'Ê', 'Í', 'Ó', 'Ô', 'Õ', 'Ú', 'Ü', 'Ç')
            dictionary[i] = (j.encode('utf-8')).upper()
            for k in range(len(minusculo)):
                dictionary[i] = dictionary[i].replace(minusculo[k], maiusculo[k])
        except:
            None

def insereErrorLog(string):
    from time import strftime
    log = codecs.open('errorlog.txt', 'a', 'latin-1')
    log.write(strftime("[%d/%m/%Y %H:%M:%S] ") + string.decode("utf-8") + '\r\n')
            
def insereSqlLog(string):
    from time import strftime
    log = codecs.open('sqllog.txt', 'a', 'latin-1')
    log.write(strftime("[%d/%m/%Y %H:%M:%S] ") + string.decode("utf-8") + '\r\n')
    
            
            
#Geradores de sql para selects            
        
def camposRetornoSql(sql):
    s = sql.lower()
    selectPos = s.find('select')
    selectPos += 6
    fromPos = s.find('from')
    return [i.strip() for i in sql[selectPos:fromPos].split(',')]

def camposRetornoCabecalho(schema, camposDeRetorno):
    res = []
    if camposDeRetorno == None or camposDeRetorno == "count(*)":
        return camposDeRetorno
    for tabela, i in camposDeRetorno.iteritems():
        if '*' in i: #se * busca todos os campos da tabela
            res += [ "%s.%s" % (tabela, campo) for campo in 
                    [i[3] for i in query('''
                        SELECT *
                        FROM information_schema.columns
                        WHERE table_schema = ''' + "'" + schema + ''''
                        AND table_name   = ''' + "'" + tabela + "'")]
                    ]
            continue
        for coluna in i:
            res.append(" %s.%s" % (tabela, coluna))
    return res

def buscaSchemas():
    #busca do banco os schemas
    schemas = [i[0] for i in query('''select schema_name from
        information_schema.schemata''')]
    schemas.sort()
    
    #remove schemas nao apropriados que podem ter sido criados
    #durante a instalacao do banco
    
    if 'projetom' in schemas:
        schemas.remove('projetom')
    if 'information_schema' in schemas:
        schemas.remove('information_schema')
    if 'pg_catalog' in schemas:
        schemas.remove('pg_catalog')
    if 'public' in schemas:
        schemas.remove('public')
     
    return schemas
        
def buscaTabelas(schema):        
    tabelas = [i[2] for i in query('''
        SELECT * FROM information_schema.tables 
        WHERE table_schema = ''' + "'" + schema + "'" + '''
        ''')]
    tabelas.sort()
        
    return tabelas
    
def buscaColunas(schema, tabela):
    return [i[3] for i in query('''
            SELECT *
            FROM information_schema.columns
            WHERE table_schema = ''' + "'" + schema + ''''
            AND table_name   = ''' + "'" + tabela + "'")]
    


def sqlSelectGeneratorSearchFilter(schema, tabelas, camposDeRetorno="*", camposDeBusca=None, 
        camposDeFiltro=None, insereErrorLogordenacao=None):
    '''
    tabelas = lista com nome das tabelas na qual a pesquisa sera feita
    camposDeRetorno = dicionario com lista contendo o nome dos campos a serem retornados por tabela 
        caso nao seja especificado, retornara todos os campos (cuidado ao usar multiplas tabelas ?)
    camposDeBusca = dicionario por tabela, cada uma sendo lista de tuplas contendo os nomes dos campos
            e os valores aos quais devem ser iguais
        caso nao seja especificado nao havera filtragem
    camposDeFiltro = dicionario por tabela, cada uma sendo lista de tuplas contendo os nomes dos campos
            e os valores aos quais devem ser parecidos
        caso nao seja especificado nao havera filtragem
    ordenacao = campo utilizado para ordenar os resultados
        caso nao seja especificado nao ordenara os resultados
    ''' 
    
    if schema not in grafos:
        iniciaSchema(schema)
    
    if camposDeRetorno == None:
        return []        
    
    sql = "SELECT"
    
    if camposDeRetorno != "*" and camposDeRetorno != "count(*)":
        latin2utf(camposDeRetorno)
    
    if camposDeBusca != None:
        latin2utf(camposDeBusca)
    
    if camposDeFiltro != None:
        latin2utf(camposDeFiltro)
    
    if camposDeRetorno == "count(*)":
        sql += " %s" % camposDeRetorno
    else:
        for i, j in camposDeRetorno.iteritems():
            for k in j:
                sql += " %s.%s," % (i, k)
        sql = sql[:-1] #retira a ultima virgula
    
    
    sql += " FROM"
    #busca as ligacoes entre as tabelas que geram o caminho
    ligacoes = grafos[schema].caminho(tabelas)
    #descobre as tabelas nÃ£o-repetidas que participam do caminho
    if ligacoes != []:
        tabelas = []
    for i in ligacoes:
        for j in i:
            tabelas.append(j[:j.find('.')])
    tabelas = sorted(set(tabelas))
    #adiciona ao sql
    for i in tabelas:
        sql += " %s.%s," % (schema, i)
    sql = sql[:-1] #retira a ultima virgula
    
    
    values = []
    sql += " WHERE"
    busca = False
    for i, j in camposDeBusca.iteritems():
        for k, l in j:
            sql += " %s.%s" % (i, k)
            sql += " = %s and"
            values += [l]
            busca = True
    for i, j in ligacoes:
        sql += " %s = %s and" % (i, j)
        busca = True
    
        
    #sql += " ("
    filtro = False
    for i, j in camposDeFiltro.iteritems():
        for k, l in j:
            sql += " %s.%s" % (i, k)
            #sql += " like %s or"
            sql += " like %s and"
            values += ['%' + l + '%']
            filtro = True
    
    if filtro or busca:
        sql = sql[:-4] #retira o ultimo and
    else:
        sql = sql[:-6] #retira o  where se nao precisar
        
    sql = cur.mogrify(sql + ';', tuple(values))
    
    insereSqlLog(sql)
    
    return sql
 


#Geradores de sql para inserts

def prepareInsert(statementName, tableName, dictionary): #prepara sql de insert baseado no dicionario
    #gerador de sql baseado no dicionaricamposDeBuscao
    sql = 'PREPARE %s_INS AS INSERT INTO %s( ' % (statementName, tableName)
    sql2 = ') VALUES ( '
    cont=1
    for i in dictionary:
        sql += i + ","
        sql2 += "$%d," % cont
        cont+=1
    sql = sql[:-1]
    sql2 = sql2[:-1]
    sql = sql + sql2 + ')'
    query(sql)

def usePreparedInsert(statementName, dictionary): #prepara sql de insert baseado no dicionario
    #gerador de sql baseado no dicionario
    sql = 'EXECUTE %s_INS ( ' % statementName
    values=[]
    for _, j in dictionary.iteritems():
        sql += "%s,"
        values.append(j if j != "" else None)
    sql = sql[:-1]
    sql = cur.mogrify(sql + ')', tuple(values))
    #print sql
    query(sql)

def sqlInsertGenerator(tableName, dictionary): #gera sql de insert baseado no dicionario
    #gerador de sql baseado no dicionario
    sql = 'INSERT INTO %s( ' % tableName
    sql2 = ') VALUES ( '
    values = []
    for i, j in dictionary:
        sql += i + ","
        sql2 += "%s," 
        values.append((str(j)).strip())
    sql = sql[:-1]
    sql2 = sql2[:-1]
    sql = cur.mogrify(sql + sql2 + ')', tuple(values))
    return sql
    


#Manipulacao de configuracoes do postgresql
     
def pgAutoCommit(state = None): #altera o valor de auto-commit do postgres
    if state != None: #se passar parametro tenta alterar a politica
        if type(state) != bool:
            raise TypeError
    try:
            conn.autocommit = state
    except:
            print "Erro ao alterar a politica de commits do banco de dados"
            raw_input('Pressione enter para encerrar o programa')
            sys.exit(1)
    else: # se nao passar parinsereErrorLogametro retorna o valor atual
        return state
    
def commit(): #executa commit na transacao
    conn.commit()
