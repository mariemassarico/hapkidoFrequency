# importando SQLit3
import sqlite3

#criando conexao
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('conexão com o banco de dados realizado com sucesso!')
except sqlite3.Error as e:
    print('Erro ao conectar com o banco de dados:',e)

# Criando tabela de Academias
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS academias(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cidade TEXT,
            responsavel TEXT
        )""")
        print('Tabela de Academias criada com sucesso!')
except sqlite3.Error as e:
    print('Erro ao criar a tabela Academias',e)

# Criando tabela de Turmas
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turma TEXT,
            dia DATE,
            responsavel TEXT,
            FOREIGN KEY (turma) REFERENCES academias (nome) ON UPDATE CASCADE ON DELETE CASCADE
        )""")
        print('Tabela de Turmas criada com sucesso!')
except sqlite3.Error as e:
    print('Erro ao criar a tabela Turmas',e)

# Criando tabela de Alunos
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            data_nasc DATE,
            sexo TEXT,
            responsavel TEXT,
            academia TEXT,
            data_inicio DATE,
            CPF TEXT,
            endereco TEXT,
            contato TEXT,
            ativo TEXT,
            bolsista TEXT,
            faixa TEXT,
            imagem TEXT,
            FOREIGN KEY (academia) REFERENCES academias (nome) ON UPDATE CASCADE ON DELETE CASCADE
        )""")
        print('Tabela de Alunos criada com sucesso!')
except sqlite3.Error as e:
    print('Erro ao criar a tabela Alunos',e)