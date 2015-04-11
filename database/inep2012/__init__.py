# -*- coding: latin -*-

from database import db

def carrega(diretorio):
    db.query("CREATE SCHEMA IF NOT EXISTS INEP2012")
    from database.inep2012 import dados_localOferta as localOferta
    from database.inep2012 import dados_instituicao as ies
    from database.inep2012 import dados_curso as curso
    from database.inep2012 import dados_aluno as aluno
    from database.inep2012 import dados_docente as docente
    #ies.txt2db(diretorio)
    localOferta.txt2db(diretorio)
    '''
    curso nao pode NUNCA, em hipotese ALGUMA, ser inserido antes
        de local oferta
        Motivo: curso faz gambiarra pra reestruturar a base
        do governo que precisa de local oferta no lugar
    '''
    curso.txt2db(diretorio)
    #docente.txt2db(diretorio)
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
    
    
def getCursosComp():
    ret = ["FORMAÇÃO DE PROFESSOR DE COMPUTAÇÃO (INFORMÁTICA)",
                       "GESTÃO DA INFORMAÇÃO",
                       "GESTÃO DA SEGURANÇA",
                       "ADMINISTRAÇÃO DE REDES",
                       "BANCO DE DADOS",
                       "CIÊNCIA DA COMPUTAÇÃO",
                       "TECNOLOGIA DA INFORMAÇÃO",
                       "TECNOLOGIA EM DESENVOLVIMENTO DE SOFTWARES",
                       "ANÁLISE DE SISTEMAS",
                       "ANÁLISE E DESENVOLVIMENTO DE SISTEMAS (TECNÓLOGO)",
                       "SEGURANÇA DA INFORMAÇÃO",
                       "SISTEMAS DE INFORMAÇÃO",
                       "USO DA INTERNET",
                       "ENGENHARIA DA COMPUTAÇÃO",
                       "ENGENHARIA DE CONTROLE E AUTOMAÇÃO",
                       "ENGENHARIA DE REDES DE COMUNICAÇÃO",
                       "ENGENHARIA DE TELECOMUNICAÇÕES",
                       "ENGENHARIA ELETRÔNICA",
                       "ENGENHARIA MECATRÔNICA",
                       "TECNOLOGIA DIGITAL",
                       "TECNOLOGIA ELETRÔNICA",
                       "TECNOLOGIA MECATRÔNICA",
                       "TELECOMUNICAÇÕES",
                       "TECNOLOGIA EM GESTÃO DE TELECOMUNICAÇÕES"]
    '''
    for i, _ in enumerate(ret):
        ret[i] = ret[i].decode('utf-8')
       ''' 
    return ret
    