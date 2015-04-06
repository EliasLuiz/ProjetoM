# -*- coding: latin -*-

from database import db

db.query("CREATE SCHEMA IF NOT EXISTS INEP2012")

def carrega(diretorio):
    from database.inep2012 import dados_localOferta as localOferta
    from database.inep2012 import dados_instituicao as ies
    from database.inep2012 import dados_curso as curso
    from database.inep2012 import dados_aluno as aluno
    from database.inep2012 import dados_docente as docente
    ies.txt2db(diretorio)
    localOferta.txt2db(diretorio)
    '''
    curso nao pode NUNCA, em hipotese ALGUMA, ser inserido antes
        de local oferta
        Motivo: curso faz gambiarra pra reestruturar a base
        do governo que precisa de local oferta no lugar
    '''
    curso.txt2db(diretorio)
    docente.txt2db(diretorio)
    #aluno.txt2db(diretorio)

def carregaCombobox():
    '''
    carrega os campos usados nos combobox de interface grafica
    gera listas globais cujos conteudos sao tuplas associando o codigo com o valor
    '''
    
    
    ### ALUNO ###
    global alunoRaca
    alunoRaca = [(1, "Branca"),(2, "Preta"),(3, "Parda"),(4, "Amarela"),
        (5, "Indígena"), (6, "Não dispõe da informação"),(0, "Não declarado")]
    global alunoSexo
    alunoSexo = [(1,"Feminino"),(0,"Masculino")]
    global alunoCidadeNasc
    alunoCidadeNasc = db.query("""SELECT DISTINCT(co_municipio_nascimento), ds_municipio_nascimento
        FROM INEP2012.ALUNO""")
    global alunoFormaIngresso
    alunoFormaIngresso = ["Vestibular", "ENEM", "Outra Forma"]
    global alunoSituacao
    alunoSituacao = [(2, "Cursando"),(3, "Matrícula trancada"),(4, "Desvinculado do curso"),
        (5, "Transferido para outro curso da mesma IES"),(6, "Formado"),(7, "Falecido")]
    global alunoPublica
    alunoPublica = [(0, "Não"),(1, "Sim"),(2, "não dispõe da informação")]
    
    
    ### CURSO ###
    global cursoCursosComp
    cursoCursosComp = [("FORMAÇÃO DE PROFESSOR DE COMPUTAÇÃO (INFORMÁTICA)",
                        "Formação de professor de computação (informática)"),
                       ("GESTÃO DA INFORMAÇÃO",
                        "Gestão da informação"),
                       ("GESTÃO DA SEGURANÇA",
                        "Gestão da segurança"),
                       ("ADMINISTRAÇÃO DE REDES",
                        "Administração de redes"),
                       ("BANCO DE DADOS",
                        "Banco de dados"),
                       ("CIÊNCIA DA COMPUTAÇÃO",
                        "Ciência da computação"),
                       ("TECNOLOGIA DA INFORMAÇÃO",
                        "Tecnologia da informação"),
                       ("TECNOLOGIA EM DESENVOLVIMENTO DE SOFTWARES",
                        "Tecnologia em desenvolvimento de softwares"),
                       ("ANÁLISE DE SISTEMAS",
                        "Análise de sistemas"),
                       ("ANÁLISE E DESENVOLVIMENTO DE SISTEMAS (TECNÓLOGO)",
                        "Análise e Desenvolvimento de Sistemas (Tecnólogo)"),
                       ("SEGURANÇA DA INFORMAÇÃO",
                        "Segurança da informação"),
                       ("SISTEMAS DE INFORMAÇÃO",
                        "Sistemas de informação"),
                       ("USO DA INTERNET",
                        "Uso da internet"),
                       ("ENGENHARIA D_ COMPUTAÇÃO",
                        "Engenharia de computação"),
                       ("ENGENHARIA DE CONTROLE E AUTOMAÇÃO",
                        "Engenharia de controle e automação"),
                       ("ENGENHARIA DE REDES DE COMUNICAÇÃO",
                        "Engenharia de redes de comunicação"),
                       ("ENGENHARIA DE TELECOMUNICAÇÕES",
                        "Engenharia de telecomunicações"),
                       ("ENGENHARIA ELETRÔNICA",
                        "Engenharia eletrônica"),
                       ("ENGENHARIA MECATRÔNICA",
                        "Engenharia mecatrônica"),
                       ("TECNOLOGIA DIGITAL",
                        "Tecnologia digital"),
                       ("TECNOLOGIA ELETRÔNICA",
                        "Tecnologia eletrônica"),
                       ("TECNOLOGIA MECATRÔNICA",
                        "Tecnologia mecatrônica"),
                       ("TELECOMUNICAÇÕES",
                        "Telecomunicações"),
                       ("TECNOLOGIA EM GESTÃO DE TELECOMUNICAÇÕES",
                        "Tecnologia em gestão de telecomunicações"),]        
    