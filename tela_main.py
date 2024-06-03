from tkinter import *
from tkinter import messagebox
import tkinter as tk
import webbrowser
import os
import conexao
import oracledb
import pandas as pd 
from tkinter.simpledialog import askstring
import datetime
import random
import re


conexao = conexao.ConexaoBanco.conexao_banco("RM553228", "130201") # conexão feita encapsulando

dsnStr = oracledb.makedsn("oracle.fiap.com.br", 1521, "ORCL")
connection = oracledb.connect(user="RM553228", password="130201", dsn=dsnStr)

root = tk.Tk()


#criacao menu
menu= Menu(root)

#instanciando a conexao

root.config(menu=menu)
root.title("MENU GS SEMESTRE 2")
root.geometry("900x500")
titulo = tk.Label(root, text="MENU GS SEMESTRE", font=("Arial", 24, "bold"))
titulo.config(background="white", foreground="#1163F0", justify=tk.CENTER, padx=20, pady=20)

titulo.grid(row=0, column=0, columnspan=2)
#fundo = PhotoImage(file="logo8.png")
#fundo1 = Label(root, image=fundo).place(x=1, y=1, relheight=1, relwidth=1)
#valor_inicial = 0
texto2 = tk.Label(root, text="LEITURA DOS DATAFRAME", font=("Arial", 15, "bold"))
texto2.config(background="white", foreground="#1163F0", justify=tk.CENTER, padx=50, pady=50)
texto2.grid(row=2, column=1, columnspan=3)

texto3 = tk.Label(root, text="VAZIO", font=("Arial", 10, "bold"))
texto3.config(background="white", foreground="#1163F0", justify=tk.CENTER, padx=50, pady=50)
texto3.grid(row=3, column=1, columnspan=3)

root.resizable(False, False)

def ler_cvs(cvs, tamanho):
    df = pd.read_csv(cvs)
    df_sem_nan = df.dropna() # remove os nan
    linha_aleatoria = random.randint(0, tamanho)
    cidade = df_sem_nan.loc[linha_aleatoria, 'Cidade']
    regiao = df_sem_nan.loc[linha_aleatoria,' Regiao'] # precisa do espaço se não, da erro
    qa = df_sem_nan.loc[linha_aleatoria,' Qualidade do Ar']
    pa = df_sem_nan.loc[linha_aleatoria,' Poluição da Água']
    
    lista = []

    lista.append(cidade)
    lista.append(regiao)
    lista.append(qa)
    lista.append(pa)
    
    return lista

def ler_cvs2(cvs):
    df = pd.read_csv(cvs)
    df_sem_nan = df.dropna() # remove os nan
    linha_aleatoria = random.randint(0, 100)

    entidade = df_sem_nan.iloc[linha_aleatoria]['Entidade']
    codigo = df_sem_nan.iloc[linha_aleatoria][' Codigo']
    ano = df_sem_nan.iloc[linha_aleatoria][' Ano']
    pc = df_sem_nan.iloc[linha_aleatoria][' Participacao da reciclagem do lixo total regional']
    pq = df_sem_nan.iloc[linha_aleatoria][' Participacao da queima do lixo total regional']
    pl = df_sem_nan.iloc[linha_aleatoria][' Participacao do lixo descartado e mal gerido do total regional']
    #codigo = df_sem_nan.loc[linha_aleatoria,' Código'] # precisa do espaço se não, da erro
    #ano = df_sem_nan.loc[linha_aleatoria,' Ano']
    
    
    lista = []

    lista.append(entidade)
    lista.append(codigo)
    lista.append(ano)
    lista.append(pc)
    lista.append(pq)
    lista.append(pl)
    #lista.append(codigo)
    #lista.append(ano)

    
    return lista

def select(tabela):
    # Cria um cursor
    cursor = connection.cursor()
    try:
    # Executa uma instrução SELECT
        cursor.execute(f"SELECT * FROM {tabela}")
        rows = cursor.fetchall()
        texto3.config(text=rows)
        for row in rows:
            dic = [] 
            dic.append(rows) # coloca todas as linhas num dicionario
        print(dic)
        # Exibindo a caixa de mensagem
        messagebox.showinfo("DIC", dic)
        #print(df)
        #print("FINAL")
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"ERRO: {error.code} - {error.message}")
    finally:
        cursor.close()


# UPDATE E DELETE não precisa.
def insert_1():
    id = random.randint(10,10000)
    #cidade = input_usuario("Cidade", "Insira a cidade:")
    #regiao = input_usuario("Regiao", "Insira a Regiao")
    #qa_ar =  input_usuario("Qualidade ar", "Insira a qualidade do ar")
    #poluicao_agua = input_usuario("Poluicao", "Insira a poluição ar:")

    leitura = ler_cvs("poluicao-agua-cidades.csv", 10)

    cidade = leitura[0] # pega o valor cidade
    regiao = leitura[1] # pega o valor regiao
    qa_ar = leitura[2] # pega o valor qa
    poluicao_agua = leitura[3] # pega o pa

    cursor = connection.cursor()

    cursor.execute(
        f"INSERT INTO BL_IA2 (id_ia2, cidade_ia2, regiao_ia2, ent_qa_ar_ia2, pol_agua_ia2) VALUES (:id, :cidade, :regiao, :qualidade_ar, :poluicao_agua)",
        { 
            ":id": id,
            ":cidade": cidade,
            ":regiao": regiao,
            ":qualidade_ar": qa_ar,
            ":poluicao_agua": poluicao_agua, 
        },
    )
    mensagem("INSERT IA_2 OK", f"DADOS IA_2 INSERIDO COM SUCESSO !{cidade, regiao, qa_ar, poluicao_agua}")
    connection.commit()

def insert_2():
    id = random.randint(10,10000)
    #cidade = input_usuario("Cidade", "Insira a cidade:")
    #regiao = input_usuario("Regiao", "Insira a Regiao")
    #qa_ar =  input_usuario("Qualidade ar", "Insira a qualidade do ar")
    #poluicao_agua = input_usuario("Poluicao", "Insira a poluição ar:")
    leitura3 = ler_cvs2("destino-plastico.csv")
    entidade = leitura3[0]
    codigo = leitura3[1]
    ano = int(leitura3[2])
    pr = leitura3[3]
    pq = leitura3[4]
    pl = leitura3[5]
    #leitura2 = ler_cvs2("destino-plastico.csv")
    print()
    cursor = connection.cursor()

    cursor.execute(
        f"INSERT INTO BL_IA (id_ia, entidade_ia, codigo_ia, ano_ia, PART_REGM_LX_TOTAL_IA, PART_QMA_LX_TOTAL_IA, PART_LX_DESC_TOTAL_IA) VALUES (:id, :entidade, :codigo, :ano, :pr, :pq, :pl)",
        { 
            ":id": id,
            ":entidade": entidade,
            ":codigo": codigo,
            ":ano": ano,
            ":pr": pr,
            ":pq": pq,
            ":pl": pl,
        },
    )
    mensagem("INSERT IA OK",f"DADOS IA INSERIDO COM SUCESSO ! {entidade, codigo, ano, pr, pq, pl}")
    connection.commit()
    
    return 

def retornar_hora_atual():
    data = datetime.datetime.now()
    data_formato_oracle = data.strftime("%Y-%m-%d %H:%M:%S") # DEIXA NO FORMATO ORACLE DA DATA
    return data_formato_oracle


def input_usuario(titulo, texto):
    root = Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    input = askstring(titulo, texto)
    return input

def criarBotao():
    btnMoverMouse = Button(root, text = 'Mover Camera',
                       command = lambda:acessarSiteProdutos("www.salesforce.com.br"))                  
    btnMoverMouse.place(x=450, y=300, anchor=CENTER)
    btnMoverMouse.configure(height=5, width=15, bg="#CADFEE")

def criarBotao2():
    btnMoverMouse = Button(root, text = 'REALIZAR LEITURA ARQUIVO CVS',
                       command = print("leitura feita"))                  
    btnMoverMouse.place(x=450, y=300, anchor=CENTER)
    btnMoverMouse.configure(height=5, width=35, bg="#CADFEE")
   
 
def acessarSiteProdutos(url):
    return webbrowser.open(url)
 
def mensagem(titulo,mgs):
    return messagebox.showinfo(titulo,mgs)
 
def quemSomos():
    messagebox.showinfo("Quem Somos?", "Lucas Alcântara Carvalho - 95111\nRenan Bezerra dos Santos - 553228")
 
def acessarDiretorio(diretorio):
   return os.startfile(diretorio)

crud = Menu(menu, tearoff=0)
crud.add_command(label= "SELECT IA1", command= lambda: select("BL_IA"))
crud.add_command(label= "SELECT IA2", command= lambda: select("BL_IA2"))
crud.add_command(label= "INSERT IA1", command= lambda: insert_1())
crud.add_command(label= "INSERT IA2", command= lambda: insert_2())

sobrenos = Menu(menu, tearoff=0)
sobrenos.add_command(label= "Quem somos", command=quemSomos)
 
sair = Menu(menu, tearoff=0)
sair.add_command(label="Sair", command=exit)
 
menu.add_cascade(label = "CRUD      ", menu= crud)
menu.add_cascade(label = "Quem somos      ", menu= sobrenos)
menu.add_cascade(label = "Sair", menu= sair)
 
 
root.mainloop()