import sqlite3

#criando conexao
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('conexão com o banco de dados realizado com sucesso!')
except sqlite3.Error as e:
    print('Erro ao conectar com o banco de dados:',e)

# Trabalhando com a tabela de cursos ----------

# Criar academias (Inserir C )

def criar_academias(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO academias (nome, cidade, responsavel) VALUES (?,?,?)"
        cur.execute(query,i)

#criar_academias(['Vila Aurora', 'Itapetininga', 'Marquinho'])

# ver todas as academias cadastradas (Selecionar)
def ver_academias():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM academias')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

#print(ver_academias())

def atualizar_academias(i):
    with con:
        cur = con.cursor()
        query = "UPDATE academias SET nome=?, cidade=?, responsavel=? WHERE id=?"
        cur.execute(query, i)

# Descompactando a tupla da lista
# l = [('Academia Central', 'Itapetininga', 'Marcos', 1)]
# for item in l:
#     atualizar_academias(item)  # Passando a tupla individualmente

#print(ver_academias())

#
def deletar_academias(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM academias WHERE id=?"
        cur.execute(query, i)

#deletar_academias([2])
#print(ver_academias())

# Trabalhando com a tabela de turmas ----------

# Criar Turmas 
def criar_turmas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO academias (turma, dia, responsavel) VALUES (?,?,?)"
        cur.execute(query,i)

def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM turmas')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

def atualizar_turmas(i):
    with con:
        cur = con.cursor()
        query = "UPDATE turmas SET turma=?, dia=?, responsavel=? WHERE id=?"
        cur.execute(query, i)

def deletar_turmas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM turmas WHERE id=?"
        cur.execute(query, i)
#print(ver_turmas())

# Trabalhando com a tabela de alunos ----------

# Criar Turmas 
def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO alunos (nome, data_nasc, sexo, responsavel, academia, data_inicio, CPF, endereco, contato, ativo, bolsista, faixa, imagem) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query,i)

def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM alunos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

def atualizar_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE alunos SET nome=?, data_nasc=?, sexo=?, responsavel=?, academia=?, data_inicio=?, CPF=?, endereco=?, contato=?, ativo=?, bolsista=?, faixa=?, imagem=? WHERE id=?"
        cur.execute(query, i)

def deletar_alunos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM alunos WHERE id=?"
        cur.execute(query, i)
#print(ver_turmas())