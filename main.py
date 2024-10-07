from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

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
    print('aluno')

def adicionar():
    frame_tabela_academia = Frame(frame_tabela,width=300,height=200,bg=co1)
    frame_tabela_academia.grid(row=0,column=0,padx=0,pady=0,sticky=NSEW)

    frame_tabela_linha = Frame(frame_tabela,width=30,height=200,bg=co3)
    frame_tabela_linha.grid(row=0,column=1,padx=10,pady=0,sticky=NSEW)        

    frame_tabela_turma = Frame(frame_tabela,width=300,height=200,bg=co4)
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
