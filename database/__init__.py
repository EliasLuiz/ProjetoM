'''
colocar as configuracoes iniciais do modulo aqui
'''

import psycopg2 as pg
import sys

try:
    conn = pg.connect("user='projetom' host='localhost' password='maurilio'")
    cur = conn.cursor()
except:
    print "Nao foi possivel conectar ao banco de dados"
    sys.exit(1)