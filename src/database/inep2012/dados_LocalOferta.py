#!/usr/bin/python

# realiza a leitura do arquivo /DADOS/LOCAL_OFERTA.txt
# cria uma tabela no banco e salva os dados lidos

from database import db

def txt_to_db(diretorio):

    file = open(diretorio + "/DADOS/LOCAL_OFERTA.txt", "r")

    for linha in file.readlines():

        dic = {}

        dic['CO_LOCAL_OFERTA_IES'] = int(linha[0:8]) #transforma em int

        dic['CO_IES'] = int(linha[8:16])

        dic['CO_MUNICIPIO_LOCAL_OFERTA'] = int(linha[16:24])

        dic['NO_MUNICIPIO_LOCAL_OFERTA'] = linha[24:174].strip()

        dic['CO_UF_LOCAL_OFERTA'] = int(linha[174:182])

        dic['SGL_UF_LOCAL_OFERTA'] = linha[182:184]

        dic['IN_SEDE'] = linha[184:192] == '       1' #transforma em bool

        try:   #algumas linhas vem com o campo vazio
            dic['CO_CURSO_POLO'] = int(linha[192:200])
        except:
            dic['CO_CURSO_POLO'] = None

        dic['CO_CURSO'] = int(linha[200:208])

        dic['IN_LOCAL_OFERTA_NEAD'] = linha[208:216] == '       1'

        dic['IN_LOCAL_OFERTA_UAB'] = linha[216:224] == '       1'

        dic['IN_LOCAL_OFERTA_REITORIA'] = linha[224:232] == '       1'

        dic['IN_LOCAL_OFERTA_POLO'] = linha[232:240] == '       1'

        dic['IN_LOCAL_OFERTA_UNID_ACADEMICA'] = linha[240:248] == '       1'

    file.close()