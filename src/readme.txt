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
                qt
                pyqt4
                
    2.3 - IDE:
        Netbeans 8.0
        2.3.1 - Plugins:
            plugin Python

    2.4 - Controle de Versão:
        Git
        2.4.1 - Repositório Remoto:
            https://github.com/EliasLuiz/ProjetoM
    

3 - Padrões Adotados:

    3.1 - Hierarquia de Arquivos:
        /
            Pasta raiz da aplicação.
            main.py:
                Módulo inicial do programa
            readme.txt:
                Arquivo contendo os objetivos, tecnologias usadas e padrões
                adotados na aplicação.
            /database
                Pacote contendo os módulos de manipulacao do banco de dados.
                db.py:
                    Arquivo de interface com a biblioteca de banco de dados.
                    Caso seja necessário mudar de banco somente este arquivo
                    será alterado.
                /database/inep2012
                    Pacote contendo os módulos de manipulacao da base de dados
                    do INEP - Censo da Educação Superior 2012.
                    dados_localOferta.py:
                        Contém as manipulações relativas ao arquivo 
                        /DADOS/LOCAL_OFERTA.txt da base de dados.
            /gui
                Pacote contendo os módulos de criação de interface gráfica.

    3.2 - Nomeclaturas de Estruturas:

    3.3 - Nomeclaturas de Banco de Dados: