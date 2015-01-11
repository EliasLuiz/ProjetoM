# modulo de interface com a biblioteca do banco (psycopg)
# ou seja, e uma abstracao para o banco de dados
# facilitando se precisar alterar o banco

import psycopg2 as pg
import sys





try:
    conn = pg.connect("dbname='projetom' user='projetom' host='localhost' password='maurilio'")
    cur = conn.cursor()
except:
    print "Nao foi possivel conectar ao banco de dados"
    raw_input('Pressione enter para encerrar o programa')
    sys.exit(1)
    
    
    
    
    
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
            dictionary[i] = j.encode('utf-8')
        except:
            None
            
            
            
            
            
def sqlSelectGeneratorSearch(tabelas, camposDeRetorno=['* '], camposDeBusca=None, ordenacao=None):
    '''
    tabelas = lista com nome das tabelas na qual a pesquisa se feita
    camposDeRetorno = lista com o nome dos campos a serem retornados (identificar tabela)
        caso nao seja especificado, retornara todos os campos (cuidado ao usar multiplas tabelas ?)
    camposDeBusca = lista de tuplas contendo os nomes dos campos e os valores aos quais devem ser iguais
        caso nao seja especificado nao havera filtragem
    ordenacao = campo utilizado para ordenar os resultados
        caso nao seja especificado nao ordenara os resultados
    ''' 
    sql = "SELECT"
    latin2utf(camposDeBusca)
    
    for i in camposDeRetorno:
        sql += " %s," % i
    sql = sql[:-1] #retira a ultima virgula
    
    sql += " FROM"
    for i in tabelas:
        sql += " %s," % i
    sql = sql[:-1] #retira a ultima virgula
        
    values = []
    if camposDeBusca != None:
        sql += " WHERE"
        for i, j in camposDeBusca:
            sql += " %s" % i
            sql += " = %s and"
            values += [j]
        sql = sql[:-3] #retira o ultimo and
    
    if ordenacao != None:
        sql += " ORDER BY %s" % ordenacao
        
    return query(cur.mogrify(sql + ';', tuple(values)))

def sqlSelectGeneratorFilter(tabelas, camposDeRetorno=['* '], camposDeFiltro=None, ordenacao=None):
    '''
    tabelas = lista com nome das tabelas na qual a pesquisa se feita
    camposDeRetorno = lista com o nome dos campos a serem retornados (identificar tabela)
        caso nao seja especificado, retornara todos os campos (cuidado ao usar multiplas tabelas ?)
    camposDeFiltro = lista de tuplas contendo os nomes dos campos e os valores aos quais devem ser parecidos
        caso nao seja especificado nao havera filtragem
    ordenacao = campo utilizado para ordenar os resultados
        caso nao seja especificado nao ordenara os resultados
    ''' 
    sql = "SELECT"
    latin2utf(camposDeFiltro)
    
    for i in camposDeRetorno:
        sql += " %s," % i
    sql = sql[:-1] #retira a ultima virgula
    
    sql += " FROM"
    for i in tabelas:
        sql += " %s," % i
    sql = sql[:-1] #retira a ultima virgula
        
    values = []
    if camposDeFiltro != None:
        sql += " WHERE"
        for i, j in camposDeFiltro:
            sql += " %s" % i
            sql += " like %s or"
            values += ['%' + j + '%']
        sql = sql[:-3] #retira o ultimo or
    
    if ordenacao != None:
        sql += " ORDER BY %s" % ordenacao
        
    return query(cur.mogrify(sql + ';', tuple(values)))

def sqlSelectGeneratorSearchFilter(tabelas, camposDeRetorno=['* '], camposDeBusca=None, 
        camposDeFiltro=None, ordenacao=None):
    '''
    tabelas = lista com nome das tabelas na qual a pesquisa se feita
    camposDeRetorno = lista com o nome dos campos a serem retornados (identificar tabela)
        caso nao seja especificado, retornara todos os campos (cuidado ao usar multiplas tabelas ?)
    camposDeBusca = lista de tuplas contendo os nomes dos campos e os valores aos quais devem ser iguais
        caso nao seja especificado nao havera filtragem
    camposDeFiltro = lista de tuplas contendo os nomes dos campos e os valores aos quais devem ser parecidos
        caso nao seja especificado nao havera filtragem
    ordenacao = campo utilizado para ordenar os resultados
        caso nao seja especificado nao ordenara os resultados
    ''' 
    sql = "SELECT"
    latin2utf(camposDeFiltro)
    
    for i in camposDeRetorno:
        sql += " %s," % i
    sql = sql[:-1] #retira a ultima virgula
    
    sql += " FROM"
    for i in tabelas:
        sql += " %s," % i
    sql = sql[:-1] #retira a ultima virgula
        
    values = []
    if camposDeBusca != None:
        sql += " WHERE"
        for i, j in camposDeBusca:
            sql += " %s" % i
            sql += " = %s and"
            values += [j]
        
    if camposDeFiltro != None:
        sql += " ("
        for i, j in camposDeFiltro:
            sql += " %s" % i
            sql += " like %s or"
            values += ['%' + j + '%']
        sql = sql[:-3] + ')' #retira o ultimo or
    
    if ordenacao != None:
        sql += " ORDER BY %s" % ordenacao
        
    return query(cur.mogrify(sql + ';', tuple(values)))





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
    print sql
    query(sql)

def usePreparedInsert(statementName, dictionary): #prepara sql de insert baseado no dicionario
    #gerador de sql baseado no dicionario
    sql = 'EXECUTE %s_INS ( ' % statementName
    values=[]
    for i, j in dictionary.iteritems():
        sql += "%s,"
        values.append(j if j != "" else None)
    sql = sql[:-1]
    sql = cur.mogrify(sql + ')', tuple(values))
#    print sql
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
    
