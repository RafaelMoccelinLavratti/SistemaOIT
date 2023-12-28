import tkinter as tk 
from tkinter import messagebox

#Janela
janela = tk.Tk()
#Define o tamanho da Janela
janela.geometry("600x600")







#Verificar se o login e senha são válidos
def login_funcao():
    #verifica se os campos login e senha estão preenchidos
    if login.get() == "" or senha.get() == "":
        tk.messagebox.showerror("Erro", "Preencha todos os campos.")
        return
    #Verifique se o login e a senha são válidos
    if login.get() == "admin" and senha.get() == "admin":
        tk.messagebox.showerror("Sucesso!", "Login bem sucessido")
        janela.destroy()
    else:
        tk.messagebox.showerror("Erro", "Login ou senha invalidos")
        
        #Botao de Login
botao_login = tk.Button(janela, text="Login", command=login_funcao)


#Campo de login e senha
login = tk.Entry(janela)
senha = tk.Entry(janela, show="*")

#Posições
login.grid(row=0, column=0)
senha.grid(row=1, column=0)
botao_login.grid(row=4, column=0)

janela.mainloop()