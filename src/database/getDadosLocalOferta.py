#!/usr/bin/python

# realiza a leitura do arquivo /DADOS/LOCAL_OFERTA.txt

import sys
import re
import math

# Open a file

diretorio = raw_input("Pasta de LOCAL_OFERTA.txt")
file = open(diretorio + "/LOCAL_OFERTA.txt", "r")

for linha in file.readlines():
        lista=linha.split(" ");
        listaElementos2= [item.strip() for item in lista]
        lista_valida = []
        for elem in listaElementos2:
            if elem.isalnum():
                lista_valida.append(elem)
        listaElementos=lista_valida
        
        #INSERIR listaElementos[0] em CO_LOCAL_OFERTA_IES
        print("CO_LOCAL_OFERTA_IES= %s" %listaElementos[0])
        CO_LOCAL_OFERTA_IES=listaElementos[0]
        
        #INSERIR listaElementos[1] em CO_IES
        print("CO_IES= %s" %listaElementos[1])
        CO_IES=listaElementos[1]

        listaCodNomeMunicipio=re.split('(\d+)',listaElementos[2])
        #INSERIR listaCodNomeMunicipio[0] em CO_MUNICIPIO_LOCAL_OFERTA
        print("CO_MUNICIPIO_LOCAL_OFERTA= %s" %listaCodNomeMunicipio[1])
        CO_MUNICIPIO_LOCAL_OFERTA=listaCodNomeMunicipio[1]
        
        #INSERIR listaCodNomeMunicipio[1] em NO_MUNICIPIO_LOCAL_OFERTA
        NO_MUNICIPIO_LOCAL_OFERTA=listaCodNomeMunicipio[2]  
        
        listaCodUF=re.split('(\d+)',listaElementos[3])
        while(len(listaCodUF)==1):
                NO_MUNICIPIO_LOCAL_OFERTA=NO_MUNICIPIO_LOCAL_OFERTA+" "+listaCodUF[0]
                listaElementos.pop(3)
                listaCodUF=re.split('(\d+)',listaElementos[3])

        print("NO_MUNICIPIO_LOCAL_OFERTA= %s" %NO_MUNICIPIO_LOCAL_OFERTA)

        #INSERIR listaCodUF[0] em CO_UF_LOCAL_OFERTA
        CO_UF_LOCAL_OFERTA=listaCodUF[1]
        print("CO_UF_LOCAL_OFERTA= %s" %listaCodUF[1])
        
        #INSERIR listaCodUF[1] em SGL_UF_LOCAL_OFERTA
        SGL_UF_LOCAL_OFERTA= listaCodUF[2]
        print("SGL_UF_LOCAL_OFERTA= %s" %listaCodUF[2])
        
        #INSERIR listaCodNomeMunicipio[4] em IN_SEDE
        IN_SEDE= listaElementos[4]
        print("IN_SEDE= %s" %listaElementos[4])

        if(len(listaElementos)==12):
                #INSERIR listaCodNomeMunicipio[5] em CO_CURSO_POLO
                CO_CURSO_POLO= listaElementos[len(listaElementos)-7]
                print("CO_CURSO_POLO= %s" %listaElementos[len(listaElementos)-7])
        
        #INSERIR listaCodNomeMunicipio[6] em CO_CURSO
        CO_CURSO= listaElementos[len(listaElementos)-6]
        print("CO_CURSO= %s" %listaElementos[len(listaElementos)-6])
        
        #INSERIR listaCodNomeMunicipio[7] em IN_LOCAL_OFERTA_NEAD
        IN_LOCAL_OFERTA_NEAD=listaElementos[len(listaElementos)-5]
        print("IN_LOCAL_OFERTA_NEAD= %s" %listaElementos[len(listaElementos)-5])
        
        #INSERIR listaCodNomeMunicipio[8] em IN_LOCAL_OFERTA_UAB
        IN_LOCAL_OFERTA_UAB= listaElementos[len(listaElementos)-4]
        print("IN_LOCAL_OFERTA_UAB= %s" %listaElementos[len(listaElementos)-4])
        
        #INSERIR listaCodNomeMunicipio[9] em IN_LOCAL_OFERTA_REITORIA
        IN_LOCAL_OFERTA_REITORIA=listaElementos[len(listaElementos)-3]
        print("IN_LOCAL_OFERTA_REITORIA= %s" %listaElementos[len(listaElementos)-3])
        
        #INSERIR listaCodNomeMunicipio[10] em IN_LOCAL_OFERTA_POLO
        IN_LOCAL_OFERTA_POLO= listaElementos[len(listaElementos)-2]
        print("IN_LOCAL_OFERTA_POLO= %s" %listaElementos[len(listaElementos)-2])
        
        #INSERIR listaCodNomeMunicipio[11] em IN_LOCAL_OFERTA_UNID_ACADEMICA
        IN_LOCAL_OFERTA_UNID_ACADEMICA= listaElementos[len(listaElementos)-1]
        print("IN_LOCAL_OFERTA_UNID_ACADEMICA= %s" %listaElementos[len(listaElementos)-1])
    
        

# Close opend file
fo.close()
