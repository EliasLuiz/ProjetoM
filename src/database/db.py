# modulo de interface com a biblioteca do banco (psycopg)
# ou seja, e uma abstracao para o banco de dados
# facilitando se precisar alterar o banco

from codecs import encode
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
    
def sqlInsertGenerator(tableName, dictionary): #gera sql de insert baseado no dicionario
    #gerador de sql baseado no dicionario
    sql = 'INSERT INTO %s( ' % tableName
    sql2 = ') VALUES ( '
    for i in dictionary:
        sql += i + ","
        dictionary[i] = (str(dictionary[i])).strip()
        if dictionary[i] == "": #se n tiver nda insere null
            sql2 += "null,"
            continue
        elif dictionary[i] in ('True', 'False'): #se for bool insere
            sql2 += "%s," % dictionary[i]
            continue
        try: #tenta inserir numero
            if "E" in dictionary[i]:
                raise
            sql2 += "%s," % float(dictionary[i])
        except: #insere letra
            sql2 += "'%s'," % dictionary[i].replace("\'", "")
    sql = sql[:-1]
    sql2 = sql2[:-1]
    return sql + sql2 + ')'
            
    sql = sql[:-1]
    sql2 = sql2[:-1]
    return sql + sql2 + ')'

	
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
    
def latin2utf(dictionary):
    for i in dictionary:
        try:
            dictionary[i] = dictionary[i].strip()
        except:
            None
        try:
            dictionary[i] = dictionary[i].encode('utf-8')
        except:
            None