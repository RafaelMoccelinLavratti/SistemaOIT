from tkinter import*
from tkinter import Tk, ttk

#Janela principal
janela = Tk()
janela.title("Login")
janela.geometry("700x500")

#Frame do Login
frameL = Frame(janela, width=450, height=350, bg="#A9A9A9")
frameL.place(x=130, y=90)

#Imagem do Frame
img = PhotoImage(file="img/usuario.png")


#Colocar imagem no Frame
label_img = Label (janela, image= img)
label_img.place(x=210, y=140)


#Entradas de texto

login = Entry(janela, width=10)
login.place(x=400, y=180, width=150, height=40)


#Label / Texto
label = Label (janela, text= "Senha")


#Posição da Label
label.place(x=260, y=210)


#Botão Realizar Login
botao = Button(frameL, text="Realizar Login")

#Posição do botão
botao.place(x=230, y=280, width=150, height=40)

#Botão Esqueci a senha
botao = Button(frameL, text="Esqueci a senha")

#Posição do botão
botao.place(x=50, y=280, width=150, height=40)



janela.mainloop()