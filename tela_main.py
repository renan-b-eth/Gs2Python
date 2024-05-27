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


conexao = conexao.ConexaoBanco.conexao_banco("RM553228", "130201") # conexão feita encapsulando

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

 
opcao1 = Menu(menu, tearoff=0)
opcao1.add_command(label= "ACESSAR LEITURA DE CVS", command= lambda: criarBotao2())

crud = Menu(menu, tearoff=0)
crud.add_command(label= "SELECT", command= lambda: quemSomos())
crud.add_command(label= "SELECT WHERE", command= lambda: quemSomos())
crud.add_command(label= "INSERT", command= lambda: quemSomos())
crud.add_command(label= "UPDATE", command= lambda: quemSomos())
crud.add_command(label= "DELETE", command= lambda: quemSomos())

opcao2 = Menu(menu, tearoff=0)
opcao2.add_command(label= "Acessar Camera Mouse", command= lambda: criarBotao())

opcao3 = Menu(menu, tearoff=0)
opcao3.add_command(label= "Acessar Teclado Virtual", command=lambda: acessarDiretorio('C:\\Windows\\System32\\osk.exe'))
 
sobrenos = Menu(menu, tearoff=0)
sobrenos.add_command(label= "Quem somos", command=quemSomos)
 
sair = Menu(menu, tearoff=0)
sair.add_command(label="Sair", command=exit)
 
 
menu.add_cascade(label = "ACESSAR LEITURA DE CVS      ", menu= opcao1)
menu.add_cascade(label = "CRUD      ", menu= crud)
menu.add_cascade(label = "Acessibilidade - Camera Mouse      ", menu= opcao2)
menu.add_cascade(label = "Acessibilidade - Teclado Virtual      ", menu= opcao3)
menu.add_cascade(label = "Quem somos      ", menu= sobrenos)
menu.add_cascade(label = "Sair", menu= sair)
 
 
root.mainloop()