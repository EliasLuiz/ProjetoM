# modulo de interface com a biblioteca do banco (psycopg)
# ou seja, e uma abstracao para o banco de dados
# facilitando se precisar alterar o banco

import psycopg2 as pg
import sys

try:
    conn = pg.connect("dbname='projetom' user='projetom' host='localhost' password='maurilio'")
    conn.autocommit = True
	cur = conn.cursor()
except:
    print "Nao foi possivel conectar ao banco de dados"
    raw_input('Pressione enter para encerrar o programa')
    sys.exit(1)

def query(sql):
    cur.execute(sql)
    try:
        return cur.fetchall()
    except:
        return None
    
def sqlInsertGenerator(tableName, dictionary):
    #gerador de sql baseado no dicionario
    sql = 'INSERT INTO %s( ' % tableName
    sql2 = ') VALUES ( '
    for i in dictionary.keys():
        sql += i + ","
        try: #insere numero
            if type(dictionary[i]) != boolean: #bool da erro pq casta pra numero
                sql2 += "%s," % float(dictionary[i])
        except: #insere letra
            sql2 += "'%s'," % dictionary[i]
    sql = sql[:-1]
    sql2 = sql2[:-1]
    return sql + sql2 + ')'
    

	
def pgAutoCommit(state = None):
	if state != None: #se passar parametro tenta alterar a politica
		if type(state) != boolean:
			raise TypeError
		try:
			conn.autocommit = state
		except:
			print "Erro ao alterar a politica de commits do banco de dados"
			raw_input('Pressione enter para encerrar o programa')
			sys.exit(1)
	else: # se nao passar parametro retorna o valor atual
		return state