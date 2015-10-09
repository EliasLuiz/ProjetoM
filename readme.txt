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
        Eclipse 4.4.1:
        2.3.1 - Plugins Eclipse:
            PyDev

    2.4 - Controle de Versão:
        Git 1.9.1
        2.4.1 - Repositório Remoto:
            https://github.com/EliasLuiz/ProjetoM
            
    2.5 - Sistema Operacional:
    	Linux Mint 17.1 Rebecca
        Windows 10 Pro
    

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
                /caged
                    Pacote contendo os módulos de manipulacao da base de dados
                    do CAGED - Cadastro Geral de Empregados e Desempregados.
                    dados.py:
                        Contém as manipulações relativas aos arquivos
                        de dados mensais liberados pelo CAGED.
                    cbo2002.py:
                        Contém as manipulações relativas ao arquivo 
                        /cbo2002.txt usado na base de dados.
                    classe10.py:
                        Contém as manipulações relativas ao arquivo 
                        /classe10.txt usado na base de dados.
                    classe20.py:
                        Contém as manipulações relativas ao arquivo 
                        /classe20.txt usado na base de dados.
                    municipio.py:
                        Contém as manipulações relativas ao arquivo 
                        /municipio.txt usado na base de dados.
                    subclasse.py:
                        Contém as manipulações relativas ao arquivo 
                        /subclasse.txt usado na base de dados.
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
            
    3.3 - Valores de Saída do Programa:
        0 - O programa finalizou corretamente
        1 - Não foi possível conectar ao banco de dados