# colocar as configuracoes iniciais do modulo aqui

import psycopg2 as pg
import sys

conn = pg.connect("user='projetom' host='localhost' password='maurilio'")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE SCHEMA IF NOT EXISTS ProjetoM;")