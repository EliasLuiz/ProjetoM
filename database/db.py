#-*- coding: latin -*-
'''
modulo de interface com a biblioteca do banco (psycopg)
ou seja, e uma abstracao para o banco de dados
facilitando se precisar alterar o banco
'''
import psycopg2 as pg
import sys
import grafo





try:
    conn = pg.connect("dbname='projetom' user='projetom' host='localhost' password='maurilio'")
    cur = conn.cursor()
except:
    print "Não foi possivel conectar ao banco de dados"
    raw_input('Pressione qualquer botão para encerrar o programa')
    sys.exit(1)


#grafos é um dicionário que contem um "grafo" para cada schema do banco
#esse grafo é a lista de adjacência, representada por um dicionário
#cada entrada desse dicionário representa uma tabela e guarda uma lista com
#as tabelas com as quais ela pode se ligar diretamente
#o objetivo é ser capaz de descobrir quais tabelas são necessárias para
#  conseguir gerar um determinado sql
grafos = {}

def iniciaSchema(schema):
    '''
    Gera o grafo utilizado para ligar as tabelas
    schema é o schema do BD que será utilizado
    
    Assume que as chaves estrangeiras do banco seguem o padrão
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
    

#funções gerais relativas ao banco    
    
def query(sql): #executa uma query sql
    try:
        cur.execute(sql)
    except pg.Error, e:
        print e.pgerror + "SQL:" +  sql
    try:
        return cur.fetchall()
    except:
        return None

def latin2utf(dictionary):
    for i, j in dictionary.iteritems():
        try:
            dictionary[i] = j.strip()
        except:
            None
        try:
            dictionary[i] = (j.encode('utf-8')).upper()
            dictionary[i] = dictionary[i].replace('á', 'Á')
            dictionary[i] = dictionary[i].replace('ã', 'Ã')
            dictionary[i] = dictionary[i].replace('à', 'À')
            dictionary[i] = dictionary[i].replace('â', 'Â')
            dictionary[i] = dictionary[i].replace('é', 'É')
            dictionary[i] = dictionary[i].replace('ẽ', 'Ẽ')
            dictionary[i] = dictionary[i].replace('ê', 'Ê')
            dictionary[i] = dictionary[i].replace('í', 'Í')
            dictionary[i] = dictionary[i].replace('ó', 'Ó')
            dictionary[i] = dictionary[i].replace('ô', 'Ô')
            dictionary[i] = dictionary[i].replace('õ', 'Õ')
            dictionary[i] = dictionary[i].replace('ú', 'Ú')
            dictionary[i] = dictionary[i].replace('ü', 'Ü')
            dictionary[i] = dictionary[i].replace('ç', 'Ç')
        except:
            None

            
            
            
#Geradores de sql para selects            
        
def camposRetornoSql(sql):
    s = sql.lower()
    selectPos = s.find('select')
    selectPos += 6
    fromPos = s.find('from')
    return [i.strip() for i in sql[selectPos:fromPos].split(',')]

def camposRetornoCabecalho(camposDeRetorno):
    res = []
    if camposDeRetorno == None or camposDeRetorno == "count(*)":
        return camposDeRetorno
    for i, j in camposDeRetorno.iteritems():
        for k in j:
            res.append(" %s.%s" % (i, k))
    return res
    


def sqlSelectGeneratorSearchFilter(schema, tabelas, camposDeRetorno="*", camposDeBusca=None, 
        camposDeFiltro=None, ordenacao=None):
    '''
    tabelas = lista com nome das tabelas na qual a pesquisa sera feita
    camposDeRetorno = dicionario com lista contendo o nome dos campos a serem retornados por tabela 
        caso não seja especificado, retornara todos os campos (cuidado ao usar multiplas tabelas ?)
    camposDeBusca = dicionario por tabela, cada uma sendo lista de tuplas contendo os nomes dos campos
            e os valores aos quais devem ser iguais
        caso não seja especificado nao havera filtragem
    camposDeFiltro = dicionario por tabela, cada uma sendo lista de tuplas contendo os nomes dos campos
            e os valores aos quais devem ser parecidos
        caso não seja especificado nao havera filtragem
    ordenacao = campo utilizado para ordenar os resultados
        caso não seja especificado nao ordenara os resultados
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
    #descobre as tabelas não-repetidas que participam do caminho
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
    
        
    sql += " ("
    filtro = False
    for i, j in camposDeFiltro.iteritems():
        for k, l in j:
            sql += " %s.%s" % (i, k)
            sql += " like %s or"
            values += ['%' + l + '%']
            filtro = True
            
    if filtro:
        sql = sql[:-3] + ')' #retira o ultimo or
    else:
        sql = sql[:-6]
        if not busca:
            sql = sql[:-2] #retira o  where se nao precisar
        
    if ordenacao != None:
        sql += " ORDER BY %s" % ordenacao
    
    return cur.mogrify(sql + ';', tuple(values))



#Geradores de sql para inserts

def prepareInsert(statementName, tableName, dictionary): #prepara sql de insert baseado no dicionario
    #gerador de sql baseado no dicionario
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
    


#Manipulação de configurações do postgresql
     
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
    else: # se nao passar parametro retorna o valor atual
        return state
    
def commit(): #executa commit na transacao
    conn.commit()
