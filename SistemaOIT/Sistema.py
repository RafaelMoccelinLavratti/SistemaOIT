from tkinter import*
from tkinter import Tk, ttk

#Janela principal
janela = Tk()
janela.title("Login")
janela.geometry("700x500")




#Label / Texto
label = Label (janela, text="Login")

#Posição da Label
label.place(x=260, y=190)

#Label / Texto
label = Label (janela, text= "Senha")


#Posição da Label
label.place(x=260, y=210)


#Botão Realizar Login
botao = Button(janela, text="Realizar Login")

#Posição do botão
botao.place(x=380, y=280)

#Botão Esqueci a senha
botao = Button(janela, text="Esqueci a senha")

#Posição do botão
botao.place(x=250, y=280)




janela.mainloop()