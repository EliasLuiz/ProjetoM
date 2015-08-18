1 - Objetivos:

    1.1 - Transformar as bases de dados sobre os cursos de graduação e sobre o
    mercado de trabalho em bancos de dados para facilitar sua manipulação.

    1.2 - Correlacionar as bases de dados de forma a perceber padrões sobre
    a preparação dada pelos cursos de graduação do país com as demandas do 
    mercado de trabalho.

    1.3 - Permitir que o usuário manipule as bases de dados de forma interativa
    através de uma interface gráfica.



2 - Tecnologias Utilizadas:

    2.1 - Banco de Dados
        PostgreSQL

    2.2 - Linguagem de Programação:
        Python
        2.2.1 - Interpretador:
            CPython 2.7.8
        2.2.2 - Bibliotecas:
            2.2.2.1 - Integração com Banco de Dados:
                psycopg2
            2.2.2.2 - Interface Gráfica:
                Qt
                PyQt4
                
    2.3 - IDE:
        Netbeans 8.0.1:
        2.3.1 - Plugins Netbeans:
            Python
        Eclipse 4.4.1:
        2.3.2 - Plugins Eclipse:
            PyDev

    2.4 - Controle de Versão:
        Git 1.9.1
        2.4.1 - Repositório Remoto:
            https://github.com/EliasLuiz/ProjetoM
            
    2.5 - Sistema Operacional:
    	Linux Mint 17.1 Rebecca
    

3 - Padrões Adotados:

    3.1 - Hierarquia de Arquivos:
        /
            Pasta raiz da aplicação.
            main.py:
                Módulo inicial do programa
                Cria uma janela MainWindow
            readme.txt:
                Arquivo contendo os objetivos, tecnologias usadas e padrões
                adotados na aplicação.
            /database
                Pacote contendo os módulos de manipulacao do banco de dados.
                db.py:
                    Arquivo de interface com a biblioteca de banco de dados.
                    Caso seja necessário mudar de banco somente este arquivo
                    será alterado.
                grafo.py:
                	Arquivo contendo uma estrutura de dados do tipo grafo adaptada
                	para o problema. Utilizada para armazenar as ligações entre as
                	tabelas e determinar a melhor ligação entre as tabelas.
                /inep2012
                    Pacote contendo os módulos de manipulacao da base de dados
                    do INEP - Censo da Educação Superior 2012.
                    dados_aluno.py:
                        Contém as manipulações relativas ao arquivo 
                        /DADOS/ALUNO.txt da base de dados.
                    dados_curso.py:
                        Contém as manipulações relativas ao arquivo 
                        /DADOS/CURSO.txt da base de dados.
                    dados_docente.py:
                        Contém as manipulações relativas ao arquivo 
                        /DADOS/DOCENTE.txt da base de dados.
                    dados_instituicao.py:
                        Contém as manipulações relativas ao arquivo 
                        /DADOS/INSTITUICAO.txt da base de dados.
                    dados_localOferta.py:
                        Contém as manipulações relativas ao arquivo 
                        /DADOS/LOCAL_OFERTA.txt da base de dados.
            /gui
                Pacote contendo os módulos de criação de interface gráfica.
                mainWindow.py:
                    Janela principal do programa
                inputWindow.py:
                    Janela de geração do SQL para um determinado schema
                dataGridView.py:
                    Janela para exibir os resultados do SQL gerado pela
                    inputWindow em formato tabular 
                fileDialog.py:
                    Modulo para seleção de arquivos e diretórios
                
                
        3.2 - Nomeclaturas de Banco de Dados:
        Cada base de dados deverá possuir seu próprio schema.
        As tabelas seram criadas de acordo com a conveniencia para execução de selects,
        mantendo nomes no mesmo padrão utilizado na base de dados.
        As colunas manteram o mesmo nome informado no dicionário da base de dados.
        INEP2012
            MUNICIPIO
                CO_MUNICIPIO INT,
                NO_MUNICIPIO VARCHAR(150),
                CO_UF INT,
                SGL_UF CHAR(2),
                NO_REGIAO VARCHAR(30), 
                IN_CAPITAL BOOLEAN
            LOCAL_OFERTA
                CO_LOCAL_OFERTA INT,
                CO_IES INT,
                CO_MUNICIPIO INT,
                IN_SEDE BOOLEAN,
                IN_LOCAL_OFERTA_NEAD BOOLEAN,
                IN_LOCAL_OFERTA_UAB BOOLEAN,
                IN_LOCAL_OFERTA_REITORIA BOOLEAN,
                IN_LOCAL_OFERTA_POLO BOOLEAN,
                IN_LOCAL_OFERTA_UNID_ACADEMICA BOOLEAN
            IES
                CO_IES INT, 
                NO_IES VARCHAR(200), 
                CO_MANTENEDORA INT, 
                CO_CATEGORIA_ADMINISTRATIVA INT, 
                DS_CATEGORIA_ADMINISTRATIVA VARCHAR(100), 
                CO_ORGANIZACAO_ACADEMICA INT, 
                DS_ORGANIZACAO_ACADEMICA VARCHAR(100), 
                CO_MUNICIPIO_IES INT, 
                QT_TEC_TOTAL INT, 
                QT_TEC_FUND_INCOMP_MASC INT, 
                QT_TEC_FUND_INCOMP_FEM INT, 
                QT_TEC_FUND_COMP_MASC INT, 
                QT_TEC_FUND_COMP_FEM INT, 
                QT_TEC_MEDIO_MASC INT, 
                QT_TEC_MEDIO_FEM INT, 
                QT_TEC_SUPERIOR_MASC INT, 
                QT_TEC_SUPERIOR_FEM INT, 
                QT_TEC_ESPECIALIZACAO_MASC INT, 
                QT_TEC_ESPECIALIZACAO_FEM INT, 
                QT_TEC_MESTRADO_MASC INT, 
                QT_TEC_MESTRADO_FEM INT, 
                QT_TEC_DOUTORADO_MASC INT, 
                QT_TEC_DOUTORADO_FEM INT, 
                IN_ACESSO_PORTAL_CAPES BOOLEAN, 
                IN_ACESSO_OUTRAS_BASES BOOLEAN, 
                IN_REFERENTE INT, 
                VL_RECEITA_PROPRIA DECIMAL(14,2), 
                VL_TRANSFERENCIA DECIMAL(14,2), 
                VL_OUTRA_RECEITA DECIMAL(14,2), 
                VL_DES_PESSOAL_REM_DOCENTE DECIMAL(14,2), 
                VL_DES_PESSOAL_REM_TECNICO DECIMAL(14,2), 
                VL_DES_PESSOAL_ENCARGO DECIMAL(14,2), 
                VL_DES_CUSTEIO DECIMAL(14,2), 
                VL_DES_INVESTIMENTO DECIMAL(14,2), 
                VL_DES_PESQUISA DECIMAL(14,2), 
                VL_DES_OUTRAS DECIMAL(14,2)
            CURSO
                CO_CURSO INT,
                CO_IES INT,
                CO_LOCAL_OFERTA INT,
                NO_CURSO VARCHAR(200),
                CO_OCDE VARCHAR(12),
                NO_OCDE VARCHAR(120),
                CO_OCDE_AREA_GERAL VARCHAR(12),
                NO_OCDE_AREA_GERAL VARCHAR(120),
                CO_OCDE_AREA_ESPECIFICA VARCHAR(12),
                NO_OCDE_AREA_ESPECIFICA VARCHAR(120),
                CO_OCDE_AREA_DETALHADA VARCHAR(12),
                NO_OCDE_AREA_DETALHADA VARCHAR(120),
                CO_GRAU_ACADEMICO INT,
                DS_GRAU_ACADEMICO VARCHAR(12),
                CO_MODALIDADE_ENSINO INT,
                DS_MODALIDADE_ENSINO VARCHAR(11),
                CO_NIVEL_ACADEMICO INT,
                DS_NIVEL_ACADEMICO VARCHAR(33),
                IN_GRATUITO BOOLEAN,
                TP_ATRIBUTO_INGRESSO INT,
                CO_LOCAL_OFERTA INT,
                NU_CARGA_HORARIA INT,
                DT_INICIO_FUNCIONAMENTO VARCHAR(38),
                DT_AUTORIZACAO_CURSO VARCHAR(38),
                IN_AJUDA_DEFICIENTE BOOLEAN,
                IN_MATERIAL_DIGITAL BOOLEAN,
                IN_MATERIAL_AMPLIADO BOOLEAN,
                IN_MATERIAL_TATIL BOOLEAN,
                IN_MATERIAL_IMPRESSO BOOLEAN,
                IN_MATERIAL_AUDIO BOOLEAN,
                IN_MATERIAL_BRAILLE BOOLEAN,
                IN_DISCIPLINA_LIBRAS BOOLEAN,
                IN_GUIA_INTERPRETE BOOLEAN,
                IN_MATERIAL_LIBRAS BOOLEAN,
                IN_RECURSOS_COMUNICACAO BOOLEAN,
                IN_RECURSOS_INFORMATICA BOOLEAN,
                IN_TRADUTOR_LIBRAS BOOLEAN,
                IN_INTEGRAL_CURSO BOOLEAN,
                IN_MATUTINO_CURSO BOOLEAN,
                IN_NOTURNO_CURSO BOOLEAN,
                IN_VESPERTINO_CURSO BOOLEAN,
                NU_PERC_CARGA_HOR_DISTANCIA DECIMAL(8,4),
                NU_INTEGRALIZACAO_MATUTINO DECIMAL(8,1),
                NU_INTEGRALIZACAO_VESPERTINO DECIMAL(8,1),
                NU_INTEGRALIZACAO_NOTURNO DECIMAL(8,1),
                NU_INTEGRALIZACAO_INTEGRAL DECIMAL(8,1),
                NU_INTEGRALIZACAO_EAD DECIMAL(8,1),
                QT_INSCRITOS_ANO_EAD INT,
                QT_VAGAS_ANUAL_EAD INT,
                QT_VAGAS_INTEGRAL_PRES INT,
                QT_VAGAS_MATUTINO_PRES INT,
                QT_VAGAS_VESPERTINO_PRES INT,
                QT_VAGAS_NOTURNO_PRES INT,
                QT_INSCRITOS_MATUTINO_PRES INT,
                QT_INSCRITOS_VESPERTINO_PRES INT,
                QT_INSCRITOS_NOTURNO_PRES INT,
                QT_INSCRITOS_INTEGRAL_PRES INT,
                QT_MATRICULA_CURSO INT,
                QT_CONCLUINTE_CURSO INT,
                QT_INGRESSO_CURSO INT,
                QT_INGRESSO_PROCESSO_SELETIVO INT,
                QT_INGRESSO_OUTRA_FORMA INT
            DOCENTE
                CO_IES INT,
                CO_DOCENTE_IES INT,
                CO_DOCENTE BIGINT,
                CO_SITUACAO_DOCENTE INT,
                DS_SITUACAO_DOCENTE VARCHAR(100),
                CO_ESCOLARIDADE_DOCENTE INT,
                DS_ESCOLARIDADE_DOCENTE VARCHAR(14),
                CO_REGIME_TRABALHO INT,
                DS_REGIME_TRABALHO VARCHAR(38),
                IN_SEXO_DOCENTE BOOLEAN,
                DS_SEXO_DOCENTE VARCHAR(9),
                NU_ANO_DOCENTE_NASC INT,
                NU_MES_DOCENTE_NASC INT,
                NU_DIA_DOCENTE_NASC INT,
                NU_IDADE_DOCENTE INT,
                CO_COR_RACA_DOCENTE INT,
                DS_COR_RACA_DOCENTE VARCHAR(24),
                CO_PAIS_DOCENTE INT,
                CO_NACIONALIDADE_DOCENTE INT,
                CO_MUNICIPIO_NASCIMENTO INT,
                IN_DOCENTE_DEFICIENCIA BOOLEAN,
                IN_CEGUEIRA BOOLEAN,
                IN_BAIXA_VISAO BOOLEAN,
                IN_SURDEZ BOOLEAN,
                IN_DEFICIENCIA_AUDITIVA BOOLEAN,
                IN_DEFICIENCIA_FISICA BOOLEAN,
                IN_SURDOCEGUEIRA BOOLEAN,
                IN_DEFICIENCIA_MULTIPLA BOOLEAN,
                IN_DEFICIENCIA_INTELECTUAL BOOLEAN,
                IN_ATU_EAD BOOLEAN,
                IN_ATU_EXTENSAO BOOLEAN,
                IN_ATU_GESTAO BOOLEAN,
                IN_ATU_GRAD_PRESENCIAL BOOLEAN,
                IN_ATU_POS_EAD BOOLEAN,
                IN_ATU_POS_PRESENCIAL BOOLEAN,
                IN_ATU_SEQUENCIAL BOOLEAN,
                IN_ATU_PESQUISA BOOLEAN,
                IN_BOLSA_PESQUISA BOOLEAN,
                IN_SUBSTITUTO BOOLEAN,
                IN_EXERCICIO_DT_REF BOOLEAN,
                IN_VISITANTE BOOLEAN,
                IN_VISITANTE_IFES_VINCULO INT
            ALUNO
                CO_ALUNO BIGINT,
                CO_CURSO INT,
                CO_ALUNO_CURSO INT,
                CO_COR_RACA_ALUNO INT,
                DS_COR_RACA_ALUNO VARCHAR(24),
                IN_SEXO_ALUNO SMALLINT,
                DS_SEXO_ALUNO VARCHAR(9), 
                NU_ANO_ALUNO_NASC INT, 
                NU_MES_ALUNO_NASC INT,
                NU_DIA_ALUNO_NASC INT,
                NU_IDADE_ALUNO INT, 
                CO_NACIONALIDADE_ALUNO INT, 
                DS_NACIONALIDADE_ALUNO VARCHAR(48),
                CO_PAIS_ORIGEM_ALUNO INT, 
                DS_PAIS_ORIGEM_ALUNO VARCHAR(80), 
                CO_MUNICIPIO_NASCIMENTO INT, 
                DS_MUNICIPIO_NASCIMENTO VARCHAR(150),
                CO_ALUNO_SITUACAO INT, 
                DS_ALUNO_SITUACAO VARCHAR(41), 
                IN_ALUNO_DEF_TGD_SUPER BOOLEAN,
                IN_DEF_AUDITIVA BOOLEAN, 
                IN_DEF_FISICA BOOLEAN, 
                IN_DEF_INTELECTUAL BOOLEAN, 
                IN_DEF_MULTIPLA BOOLEAN, 
                IN_DEF_SURDEZ BOOLEAN,
                IN_DEF_SURDOCEGUEIRA BOOLEAN, 
                IN_DEF_BAIXA_VISAO BOOLEAN, 
                IN_DEF_SUPERDOTACAO BOOLEAN, 
                IN_TGD_AUTISMO_INFANTIL BOOLEAN,
                IN_TGD_SINDROME_ASPERGER BOOLEAN, 
                IN_TGD_SINDROME_RETT BOOLEAN, 
                IN_TGD_TRANSTOR_DESINTEGRATIVO BOOLEAN,
                DT_INGRESSO_CURSO VARCHAR(38), 
                IN_RESERVA_VAGAS BOOLEAN, 
                IN_FINANC_ESTUDANTIL BOOLEAN, 
                IN_ING_VESTIBULAR BOOLEAN,
                IN_ING_ENEM BOOLEAN, 
                IN_ING_OUTRO_TIPO_SELECAO BOOLEAN, 
                IN_ING_CONVENIO_PEC_G BOOLEAN, 
                IN_ING_OUTRA_FORMA BOOLEAN,
                IN_RESERVA_ETNICO BOOLEAN, 
                IN_RESERVA_DEFICIENCIA BOOLEAN, 
                IN_RES_RENDA_FAMILIAR BOOLEAN, 
                IN_RESERVA_OUTROS BOOLEAN,
                IN_FIN_REEMB_FIES BOOLEAN,
                IN_FIN_REEMB_ESTADUAL BOOLEAN, 
                IN_FIN_REEMB_MUNICIPAL BOOLEAN, 
                IN_FIN_REEMB_PROG_IES BOOLEAN,
                IN_FIN_REEMB_ENT_EXTERNA BOOLEAN, 
                IN_FIN_REEMB_OUTRA BOOLEAN, 
                IN_FIN_NAOREEMB_PROUNI_INTEGR BOOLEAN,
                IN_FIN_NAOREEMB_PROUNI_PARCIAL BOOLEAN, 
                IN_FIN_NAOREEMB_ESTADUAL BOOLEAN, 
                IN_FIN_NAOREEMB_MUNICIPAL BOOLEAN,
                IN_FIN_NAOREEMB_PROG_IES BOOLEAN, 
                IN_FIN_NAOREEMB_ENT_EXTERNA BOOLEAN, 
                IN_FIN_NAOREEMB_OUTRA BOOLEAN, 
                IN_APOIO_SOCIAL BOOLEAN,
                IN_APOIO_ALIMENTACAO BOOLEAN, 
                IN_APOIO_BOLSA_PERMANENCIA BOOLEAN, 
                IN_APOIO_BOLSA_TRABALHO BOOLEAN,
                IN_APOIO_MATERIAL_DIDATICO BOOLEAN, 
                IN_APOIO_MORADIA BOOLEAN, 
                IN_APOIO_TRANSPORTE BOOLEAN,
                IN_ATIVIDADE_EXTRACURRICULAR BOOLEAN, 
                IN_COMPL_ESTAGIO BOOLEAN, 
                IN_COMPL_EXTENSAO BOOLEAN, 
                IN_COMPL_MONITORIA BOOLEAN,
                IN_COMPL_PESQUISA BOOLEAN, 
                IN_BOLSA_ESTAGIO BOOLEAN, 
                IN_BOLSA_EXTENSAO BOOLEAN, 
                IN_BOLSA_MONITORIA BOOLEAN,
                IN_BOLSA_PESQUISA BOOLEAN, 
                TP_PROCEDE_EDUC_PUBLICA INT, 
                NU_SEMESTRE_CONCLUSAO INT, 
                IN_ALUNO_PARFOR BOOLEAN,
                IN_MATRICULA BOOLEAN, 
                IN_CONCLUINTE BOOLEAN, 
                IN_INGRESSO_TOTAL BOOLEAN, 
                IN_INGRESSO_PROCESSO_SELETIVO BOOLEAN,
                IN_INGRESSO_OUTRAS_FORMAS BOOLEAN, 
                ANO_INGRESSO INT
            
    3.3 - Valores de Saída do Programa:
        0 - O programa finalizou corretamente
        1 - Não foi possível conectar ao banco de dados