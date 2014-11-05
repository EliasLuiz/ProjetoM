# modulo de interface com a biblioteca do banco (psycopg)
# ou seja, e uma abstracao para o banco de dados
# facilitando se precisar alterar o banco

import psycopg2 as pg
import sys

try:
    conn = pg.connect("dbname='projetom' user='projetom' host='localhost' password='maurilio'")
    conn.autocommit = True
except:
    print "Nao foi possivel conectar ao banco de dados"
    raw_input('Pressione enter para encerrar o programa')
    sys.exit(1)
     
cur = conn.cursor()

def query(sql):
    cur.execute(sql)
    try:
        return cur.fetchall()
    except:
        return None
    
def sqlGenerator(tableName, dicionary):
    #gerador de sql baseado no dicionario
    # %%%%%%%%%%%%% TESTAR %%%%%%%%%%%%%%
    sql = 'INSERT INTO %s( ' % tableName
    sql2 = ') VALUES ( '
    for i in dic.keys:
        sql += i + ","
        sql2 = "%s," % dic[i]
    sql = sql[:-1]
    sql2 = sql2[:-1]
    #return sql + ')' + sql2 + ')'
    return sql + ')' + sql2 + ')'
    