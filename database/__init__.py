'''
colocar as configuracoes iniciais do modulo aqui
'''

import psycopg2 as pg
import sys

try:
    conn = pg.connect("user='projetom' host='localhost' password='maurilio'")
    conn.autocommit = True
    cur = conn.cursor()
    #cur.execute("CREATE DATABASE IF NOT EXISTS ProjetoM;")
except:
    print "Nao foi possivel conectar ao banco de dados"
    raw_input('Pressione enter para encerrar o programa')
    sys.exit(1)