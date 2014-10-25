#!/usr/bin/python

# realiza a leitura do arquivo /DADOS/LOCAL_OFERTA.txt


'''
#funcao antiga otimizada (campos nao ficam divididos precisamente)

diretorio = raw_input("Pasta de LOCAL_OFERTA.txt: ")

file = open(diretorio + "/LOCAL_OFERTA.txt", "r")

for linha in file.readlines():
    
    lista=linha.split(' ')
        
    listaElementos = [item.replace('\r\n', '') for item in lista if item != '']
    
    print listaElementos
        
file.close()
'''

#diretorio = raw_input("Pasta de LOCAL_OFERTA.txt: ")
diretorio = '/media/elias/4DF85F7166976ABF/CEFET/Projeto Maurilio/microdados_educacao_superior_2012/DADOS' #usado para teste

file = open(diretorio + "/LOCAL_OFERTA.txt", "r")

for linha in file.readlines():
    
    dic = {}
    
    dic['CO_LOCAL_OFERTA_IES'] = linha[0:8]
    dic['CO_IES'] = linha[8:16]
    dic['CO_MUNICIPIO_LOCAL_OFERTA'] = linha[16:24]
    dic['NO_MUNICIPIO_LOCAL_OFERTA'] = linha[24:174]
    dic['CO_UF_LOCAL_OFERTA'] = linha[174:182]
    dic['SGL_UF_LOCAL_OFERTA'] = linha[182:184]
    dic['IN_SEDE'] = linha[184:192]
    dic['CO_CURSO_POLO'] = linha[192:200]
    dic['CO_CURSO'] = linha[200:208]
    dic['IN_LOCAL_OFERTA_NEAD'] = linha[208:216]
    dic['IN_LOCAL_OFERTA_UAB'] = linha[216:224]
    dic['IN_LOCAL_OFERTA_REITORIA'] = linha[224:232]
    dic['IN_LOCAL_OFERTA_POLO'] = linha[232:240]
    dic['IN_LOCAL_OFERTA_UNID_ACADEMICA'] = linha[240:248]
    
    
    
file.close()