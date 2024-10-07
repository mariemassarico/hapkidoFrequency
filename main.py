from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkcalendar import Calendar,DateEntry
from datetime import date

from PIL import ImageTk, Image

#cores
co0 = "#2e2d2b" #preto
co1 = "#feffff" #branco
co2 = "#e5e5e5" #cinza
co3 = "#00a095" #verde 
co4 = "#403d3d" # 
co6 = "#003452" # 
co7 = "#ef5350" # 
co6e = "038cfc" # 
co8 = "#263238" # 
co9 = "#e9edf5" # 

#janela

janela = Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=FALSE,height=FALSE)

style = Style(janela)
style.theme_use("clam")

#dividir frames

frame_logo = Frame(janela, width=850,height=52,bg=co6)
frame_logo.grid(row=0,column=0,padx=0,pady=0,sticky=NSEW)

ttk.Separator(janela,orient=HORIZONTAL).grid(row=1,columnspan=1,ipadx=680)

frame_dados = Frame(janela, width=850,height=65,bg=co1)
frame_dados.grid(row=2,column=0,padx=0,pady=0,sticky=NSEW)

ttk.Separator(janela,orient=HORIZONTAL).grid(row=3,columnspan=1,ipadx=680)

frame_detalhes = Frame(janela, width=850,height=200,bg=co1)
frame_detalhes.grid(row=4,column=0,padx=10,pady=0,sticky=NSEW)

frame_tabela = Frame(janela, width=850,height=200,bg=co1)
frame_tabela.grid(row=5,column=0,padx=10,pady=0,sticky=NSEW)

# frame logo
caminho = 'icons/fighter.png'
app_lp = Image.open(caminho)
app_lp = app_lp.resize((50,50))
app_lp = ImageTk.PhotoImage(app_lp)
app_logo = Label(frame_logo,image=app_lp,text="Cadastro de Alunos", width=850, compound=LEFT,relief=RAISED,anchor=NW,font=('Ivy 15 bold'), bg = co6,fg = co1)
app_logo.place(x=0,y=0)

#funcoes
def alunos():
    #campos de entrada
    l_nome = Label(frame_detalhes, text = "Nome *", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_nome.place(x=4,y=10)
    e_nome = Entry(frame_detalhes, width=40,justify='left',relief='solid')
    e_nome.place(x=7,y=30)

    dataNasc = Label(frame_detalhes, text = "Data Nasc.", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    dataNasc.place(x=264,y=10)
    e_datanas = Entry(frame_detalhes, width=10,justify='left',relief='solid')
    e_datanas.place(x=267,y=30)

    dataNascimento = DateEntry(frame_detalhes,width = 10, background='darkblue',foreground = 'white', borderWidth = 2, year=2024)
    dataNascimento.place(x=267,y=30)

    l_sexo = Label(frame_detalhes, text = "Sexo", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_sexo.place(x=354,y=10)
    e_sexo = Entry(frame_detalhes, width=10,justify='left',relief='solid')
    e_sexo.place(x=357,y=30)

    #sexo

    sexos = ['Homem','Mulher']
    sexo = []

    for i in sexos:
        sexo.append(i)
    
    c_sexos = ttk.Combobox(frame_detalhes,width=10, font = ('Ivy 8 bold'))
    c_sexos['values'] = (sexo)
    c_sexos.place(x=357,y=30)

    l_nomeR = Label(frame_detalhes, text = "Responsável *", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_nomeR.place(x=4,y=55)
    e_nomeR = Entry(frame_detalhes, width=40,justify='left',relief='solid')
    e_nomeR.place(x=7,y=75)

    dataIn = Label(frame_detalhes, text = "Data Inicio", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    dataIn.place(x=264,y=55)
    e_datain = Entry(frame_detalhes, width=10,justify='left',relief='solid')
    e_datain.place(x=267,y=75)

    dataInicio = DateEntry(frame_detalhes,width = 10, background='darkblue',foreground = 'white', borderWidth = 2, year=2024)
    dataInicio.place(x=267,y=75)
    
    l_acad = Label(frame_detalhes, text = "Academia", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_acad.place(x=354,y=55)
    e_acad = Entry(frame_detalhes, width=10,justify='left',relief='solid')
    e_acad.place(x=357,y=75)
    
    Academias = ['Vila Aurora','Centro','Boituva']
    Academia = []

    for i in Academias:
        Academia.append(i)
    
    c_Academias = ttk.Combobox(frame_detalhes,width=10, font = ('Ivy 8 bold'))
    c_Academias['values'] = (Academia)
    c_Academias.place(x=357,y=75)

    l_endereco = Label(frame_detalhes, text = "Endereco", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_endereco.place(x=4,y=100)
    e_endereco = Entry(frame_detalhes, width=40,justify='left',relief='solid')
    e_endereco.place(x=7,y=120)

    l_cpf = Label(frame_detalhes, text = "CPF", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_cpf.place(x=264,y=100)
    e_cpf = Entry(frame_detalhes, width=10,justify='left',relief='solid')
    e_cpf.place(x=267,y=120)

    l_contato = Label(frame_detalhes, text = "Contato", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_contato.place(x=264,y=100)
    e_contato = Entry(frame_detalhes, width=10,justify='left',relief='solid')
    e_contato.place(x=267,y=120)

    l_faix = Label(frame_detalhes, text = "Faixa", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_faix.place(x=354,y=100)
    e_faix = Entry(frame_detalhes, width=10,justify='left',relief='solid')
    e_faix.place(x=357,y=120)
    
    Faixas = ['Branca','Amarela','Amarela Ponta Verde', 'Verde', 'Verde Ponta Azul', 'Azul', 'Azul 1 ponta', 'Azul 2 pontas', 'Azul 3 pontas', 'Vermelha', 'Vermelha 1 ponta', 'Vermelha 2 pontas', 'Vermelha 3 pontas', 'Preta','Preta 2ºDan', 'Preta 3ºDan', 'Preta 4ºDan', 'Preta 5ºDan', 'Preta 6ºDan', 'Preta 7ºDan', 'Preta 8ºDan', 'Preta 9ºDan']
    Faixa = []

    for i in Faixas:
        Faixa.append(i)
    
    c_Faixas = ttk.Combobox(frame_detalhes,width=10, font = ('Ivy 8 bold'))
    c_Faixas['values'] = (Faixa)
    c_Faixas.place(x=357,y=120)

    l_status = Label(frame_detalhes, text = "Status", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_status.place(x=4,y=140)
    e_status = Entry(frame_detalhes, width=10,justify='left',relief='solid')
    e_status.place(x=7,y=160)

    Status = ['Ativo','Inativo']
    Ativo = []

    for i in Status:
        Ativo.append(i)
    
    c_Status = ttk.Combobox(frame_detalhes,width=10, font = ('Ivy 8 bold'))
    c_Status['values'] = (Ativo)
    c_Status.place(x=7,y=160)

    l_bolsa = Label(frame_detalhes, text = "Bolsista", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_bolsa.place(x=124,y=140)
    e_bolsa = Entry(frame_detalhes, width=10,justify='left',relief='solid')
    e_bolsa.place(x=127,y=160)
    Bolsas = ['Sim','Não']
    Bolsa = []

    for i in Bolsas:
        Bolsa.append(i)
    
    c_Bolsas = ttk.Combobox(frame_detalhes,width=10, font = ('Ivy 8 bold'))
    c_Bolsas['values'] = (Bolsa)
    c_Bolsas.place(x=127,y=160)

    #funcao para escolher imagem
    #global imagem, imagem_string, l_imagem

    def escolher_imagem():
        global imagem, imagem_string, l_imagem

        imagem = fd.askopenfilename()
        imagem_string = imagem

        imagem = Image.open(imagem)
        imagem = imagem.resize((130,130))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(frame_detalhes,image=imagem, bg = co1,fg = co4)
        l_imagem.place(x=447,y=10)

        botao_carregar['text'] = 'Trocar de foto'

    botao_carregar = Button(frame_detalhes,command=escolher_imagem,text='Carregar Foto'.upper(), compound=CENTER,anchor=CENTER,overrelief=RIDGE,width=20, font=('Ivy 7'), bg=co1,fg=co0)
    botao_carregar.place(x = 447,y=160)

    #linha separadora
    l_linha = Label(frame_detalhes, relief=GROOVE, text = "h", height=100,width=1, anchor=NW, font=('Ivy 1'), bg = co0,fg=co0)
    l_linha.place(x=610,y=10)

    l_linha = Label(frame_detalhes, relief=GROOVE, text = "h", height=100,width=1, anchor=NW, font=('Ivy 1'), bg = co1,fg=co0)
    l_linha.place(x=608,y=10)

    l_nome = Label(frame_detalhes, text = "Procurar Aluno [Entra o nome]", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_nome.place(x=627,y=10)
    e_nome = Entry(frame_detalhes, width=17,justify='center',relief='solid', font=('Ivy 10'))
    e_nome.place(x=630,y=30)
    botao_procurar = Button(frame_detalhes,anchor='center',text='Procurar'.upper(),width=9,overrelief=RIDGE,font=('Ivy 7 bold'),bg = co1,fg=co4)
    botao_procurar.place(x = 757,y=30)

    botao_salvar = Button(frame_detalhes,anchor='center',text='Salvar'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7 bold'),bg = co3,fg=co1)
    botao_salvar.place(x = 627,y=110)

    botao_atualizar = Button(frame_detalhes,anchor='center',text='Atualizar'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7 bold'),bg = co6,fg=co1)
    botao_atualizar.place(x = 627,y=135)

    botao_deletar = Button(frame_detalhes,anchor='center',text='Deletar'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7 bold'),bg = co7,fg=co1)
    botao_deletar.place(x = 627,y=160)

    botao_ver = Button(frame_detalhes,anchor='center',text='Visualizar'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7 bold'),bg = co1,fg=co0)
    botao_ver.place(x = 727,y=160)
    
    #Tabela Alunos
    def mostrar_alunos():
        app_nome = Label(frame_tabela, text="Tabela de Alunos", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        #creating a treeview with dual scrollbars
        list_header = ['id','nome','data_nasc','sexo','responsavel','academia','data_inicio','CPF','endereco','contato','ativo','bolsista','faixa','imagem']

        df_list = []

        global tree_aluno

        tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

        tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_aluno.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","center","center","center","center","center","center"]
        h=[30,150,30,30,30,30,30,30,30]
        n=0

        for col in list_header:
            tree_aluno.heading(col, text=col.title(), anchor=NW)
            #adjust the column's width to the header string
            tree_aluno.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_aluno.insert('', 'end', values=item)

    mostrar_alunos()


def adicionar():
    frame_tabela_academia = Frame(frame_tabela,width=300,height=200,bg=co1)
    frame_tabela_academia.grid(row=0,column=0,padx=10,pady=0,sticky=NSEW)

    frame_tabela_linha = Frame(frame_tabela,width=30,height=200,bg=co1)
    frame_tabela_linha.grid(row=0,column=1,padx=10,pady=0,sticky=NSEW)        

    frame_tabela_turma = Frame(frame_tabela,width=300,height=200,bg=co1)
    frame_tabela_turma.grid(row=0,column=2,padx=10,pady=0,sticky=NSEW)

    l_nome = Label(frame_detalhes, text = "Academia", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_nome.place(x=4,y=10)
    e_nomeAcademia = Entry(frame_detalhes, width=35,justify='left',relief='solid')
    e_nomeAcademia.place(x=7,y=40)

    l_cidade = Label(frame_detalhes, text = "Cidade", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_cidade.place(x=4,y=70)
    e_cidade = Entry(frame_detalhes, width=20,justify='left',relief='solid')
    e_cidade.place(x=7,y=100)

    l_responsavel = Label(frame_detalhes, text = "Responsavel", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_responsavel.place(x=4,y=130)
    e_responsavel = Entry(frame_detalhes, width=35,justify='left',relief='solid')
    e_responsavel.place(x=7,y=160)

    botao_carregar = Button(frame_detalhes,anchor='center',text='Salvar'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7 bold'),bg = co3,fg=co1)
    botao_carregar.place(x = 107,y=180)

    botao_atualizar = Button(frame_detalhes,anchor='center',text='Atualizar'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7 bold'),bg = co3,fg=co1)
    botao_atualizar.place(x = 187,y=180)

    botao_deletar = Button(frame_detalhes,anchor='center',text='Deletar'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7 bold'),bg = co7,fg=co1)
    botao_deletar.place(x = 267,y=180)

    #Tabela Cursos
    def mostrar_cursos():
        app_nome = Label(frame_tabela_academia, text="Tabela de Cursos", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        #creating a treeview with dual scrollbars
        list_header = ['ID','nome','cidade','responsavel']

        df_list = []

        global tree_curso

        tree_curso = ttk.Treeview(frame_tabela_academia, selectmode="extended",columns=list_header, show="headings")

        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_academia, orient="vertical", command=tree_curso.yview)
        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_academia, orient="horizontal", command=tree_curso.xview)

        tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_curso.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_academia.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,150,80,60]
        n=0

        for col in list_header:
            tree_curso.heading(col, text=col.title(), anchor=NW)
                #adjust the column's width to the header string
            tree_curso.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_curso.insert('', 'end', values=item)

    mostrar_cursos()

    #linha separatoria

    l_linha = Label(frame_detalhes, relief=GROOVE, text = "h", height=100,width=1, anchor=NW, font=('Ivy 1'), bg = co0,fg=co0)
    l_linha.place(x=374,y=10)

    l_linha = Label(frame_detalhes, relief=GROOVE, text = "h", height=100,width=1, anchor=NW, font=('Ivy 1'), bg = co1,fg=co0)
    l_linha.place(x=372,y=10)

    l_linha = Label(frame_tabela_linha, relief=GROOVE, text = "h", height=140,width=1, anchor=NW, font=('Ivy 1'), bg = co0,fg=co0)
    l_linha.place(x=6,y=10)

    l_linha = Label(frame_tabela_linha, relief=GROOVE, text = "h", height=140,width=1, anchor=NW, font=('Ivy 1'), bg = co1,fg=co0)
    l_linha.place(x=4,y=10)


    #detalhes das turmas

    l_turma = Label(frame_detalhes, text = "Turma", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_turma.place(x=404,y=10)
    e_turmaAcademia = Entry(frame_detalhes, width=35,justify='left',relief='solid')
    e_turmaAcademia.place(x=407,y=40)

    #pegando as turmas

    turmas = ['turma1','turma2']
    turma = []

    for i in turmas:
        turma.append(i)
    
    t_turmas = ttk.Combobox(frame_detalhes,width=35, font = ('Ivy 8 bold'))
    t_turmas['values'] = (turma)
    t_turmas.place(x=407,y=40)

    l_tdia = Label(frame_detalhes, text = "Dia", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_tdia.place(x=404,y=70)
    e_tdia = Entry(frame_detalhes, width=20,justify='left',relief='solid')
    e_tdia.place(x=407,y=100)

    datatreino = DateEntry(frame_detalhes,width = 20, background='darkblue',foreground = 'white', borderWidth = 2, year=2024)
    datatreino.place(x=407,y=100)

    l_tresponsavel = Label(frame_detalhes, text = "Responsavel", height=1, anchor=NW, font=('Ivy 10'), bg = co1,fg=co4)
    l_tresponsavel.place(x=404,y=130)
    e_tresponsavel = Entry(frame_detalhes, width=35,justify='left',relief='solid')
    e_tresponsavel.place(x=407,y=160)

    responsaveis = ['reponsavel1','responsavel2']
    responsavel = []

    for i in responsaveis:
        responsavel.append(i)
    
    t_responsaveis = ttk.Combobox(frame_detalhes,width=35, font = ('Ivy 8 bold'))
    t_responsaveis['values'] = (responsavel)
    t_responsaveis.place(x=407,y=160)

    #Tabela Cursos
    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text="Tabela de Turmas", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        #creating a treeview with dual scrollbars
        list_header = ['ID','turma','dia','responsavel']

        df_list = []

        global tree_turma

        tree_turma = ttk.Treeview(frame_tabela_turma, selectmode="extended",columns=list_header, show="headings")

        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tree_turma.yview)
        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tree_turma.xview)

        tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_turma.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_turma.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","e","e"]
        h=[30,130,150,80]
        n=0

        for col in list_header:
            tree_turma.heading(col, text=col.title(), anchor=NW)
                #adjust the column's width to the header string
            tree_turma.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_turma.insert('', 'end', values=item)

    mostrar_turmas()


def salvar():
    print('salvar')



#funcao de controle

def control(i):
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        alunos()

    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        adicionar()

    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        salvar()

#botoes
app_img_cadastro = Image.open('icons/add.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados,command=lambda:control('cadastro'),image=app_img_cadastro,text="Cadastro", width=100, compound=LEFT,overrelief=RIDGE,font=('Ivy 11'), bg = co1,fg = co0)
app_cadastro.place(x=10,y=30)

app_img_adicionar = Image.open('icons/add.png')
app_img_adicionar = app_img_adicionar.resize((18,18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados,command=lambda:control('adicionar'),image=app_img_adicionar,text="Adicionar", width=100, compound=LEFT,overrelief=RIDGE,font=('Ivy 11'), bg = co1,fg = co0)
app_adicionar.place(x=123,y=30)

app_img_salvar = Image.open('icons/save.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados,command=lambda:control('salvar'),image=app_img_salvar,text="Salvar", width=100, compound=LEFT,overrelief=RIDGE,font=('Ivy 11'), bg = co1,fg = co0)
app_salvar.place(x=236,y=30)



janela.mainloop()
