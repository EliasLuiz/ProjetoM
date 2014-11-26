from database import db

db.query("CREATE SCHEMA IF NOT EXISTS INEP2012")

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
    


    




