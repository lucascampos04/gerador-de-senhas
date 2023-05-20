from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import string


# CORES UTILIZADAS NA INTERFACE
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cinzenta
cor6 = "#3080f0"  # blue / azul

janela = Tk()
janela.title("")
janela.geometry("295x350")

# trabalhando no frame_top
style = ttk.Style(janela)
style.theme_use('clam')

# parte onde ficará o saldo e configurações do banco
frame_top = Frame(janela, width=310, height=70, bg=cor2, relief='flat')
frame_top.grid(row=0, column=0, sticky=NSEW)

# frame bottom
frame_bottom = Frame(janela, width=310, height=300, relief='flat')
frame_bottom.grid(row=1, column=0, sticky=NSEW)

# imagem
img = Image.open('senha.png')
img = img.resize((30, 30), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
app_logo = Label(frame_top, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor2)
app_logo.place(x=2, y=0)

app_nome = Label(frame_top, text='GERADOR DE SENHAS', height=5, width=20, padx=0, relief='flat', anchor='nw',
                 font=('Ivy 16 bold'), bg=cor2, fg=cor4)
app_nome.place(x=40, y=5)

app_nome = Label(frame_top, text='', height=3, width=300, padx=0, relief='flat', anchor='nw', font=('Ivy 1'),
                 bg=cor3, fg=cor1)
app_nome.place(x=1, y=45)


# FUNÇÕES
def gerar_senha():
    # Criar as condições para a geração da senha

    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = '123456789'
    simbolos = '[]{}()*/\;,._-'

    combinar = ""

    # CONDIÇÃO PARA MAIUSCULAS
    if estado1.get() == alfabeto_maior:
        combinar = alfabeto_maior

    # CONDIÇÃO PARA LETRAS MINUSCULAS
    if estado2.get() == alfabeto_menor:
        combinar += alfabeto_menor

    # CONDIÇÃO PARA NUMEROS
    if estado3.get() == numeros:
        combinar += numeros

    # CONDIÇÃO PARA ALFABETO
    if estado4.get() == simbolos:
        combinar += simbolos

    # Verificar se a variável combinar não está vazia antes de gerar a senha
    if combinar:
        comprimento = int(spin.get())
        senha = "".join(random.sample(combinar, comprimento))
        print(senha)
    else:
        print("Não foi possível gerar a senha, pois nenhuma opção foi selecionada.")

    app_senha['text'] = senha

    def copiar_senha():
        info = senha
        frame_bottom.clipboard_clear()
        frame_bottom.clipboard_append(info)

        messagebox.showinfo("sucesso", "A Senha foi copiada com sucesso")

    app_senha_copiar = Button(frame_bottom, text='Copiar', command=copiar_senha, height=2, width=7, relief='raised', anchor='center',
                  font=('Ivy 13 bold'), fg=cor1)
    app_senha_copiar.grid(row=0, column=0, columnspan=1, sticky=NSEW, pady=3)
    app_senha_copiar.place(x=210, y=0)

# TRABALHANDO NO FRAME BOTT OM
app_senha = Label(frame_bottom, text='- - - -', height=2, width=20, padx=0, relief='solid', anchor='center',
                  font=('Ivy 13 bold'), fg=cor1)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=1, pady=3)
app_senha.place(x=3, y=0)

app_info = Label(frame_bottom, text='Numero  total de caracteres na senha', height=1, padx=0, relief='flat', anchor='nw',
                  font=('Ivy 11 bold'), fg=cor1)
app_info.grid(row=1, column=0, columnspan=1, sticky=NSEW, padx=5, pady=1)
app_info.place(x=3, y=50)

var = IntVar()
var.set(8)
spin = Spinbox(frame_bottom, from_=0, to=20, width=20, textvariable=var)
spin.grid(row=2, column=0, columnspan=1, sticky=NSEW, padx=5, pady=8)
spin.place(x=3, y=80)

alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = '[]{}()*/\;,._-'

frame_carac = Frame(janela, width=310, height=70, bg=cor2, relief='flat')
frame_carac.grid(row=5, column=1, sticky=NSEW)

#  CHECKBOX DE LETRAS MAIUSUCLAS
estado1 = StringVar()
estado1.set(False)
check_1 = Checkbutton(janela, width=0, var=estado1, onvalue=alfabeto_maior, offvalue='off', relief='flat')
check_1.place(x=2, y=175)
app_info = Label(janela, text='Letras maiusculas', height=1, padx=0, relief='flat', anchor='nw',
                  font=('Ivy 11 bold'), fg=cor1)
app_info.grid(row=1, column=0, columnspan=1, sticky=NSEW)
app_info.place(x=30, y=175)

#  CHECKBOX DE LETRAS MINUSCULAS
estado2 = StringVar()
estado2.set(False)
check_2 = Checkbutton(janela, width=0, var=estado2, onvalue=alfabeto_menor, offvalue='off', relief='flat')
check_2.place(x=2, y=200)
app_info = Label(janela, text='Letras minusculas', height=1, padx=0, relief='flat', anchor='nw',
                  font=('Ivy 11 bold'), fg=cor1)
app_info.grid(row=1, column=0, columnspan=1, sticky=NSEW)
app_info.place(x=30, y=200)

# CHECKBOX DE NUMEROS
estado3 = StringVar()
estado3.set(False)
check_3 = Checkbutton(janela, width=0, var=estado3, onvalue=numeros, offvalue='off', relief='flat')
check_3.place(x=2, y=225)
app_info = Label(janela, text='Numeros', height=1, padx=0, relief='flat', anchor='nw',
                  font=('Ivy 11 bold'), fg=cor1)
app_info.grid(row=1, column=0, columnspan=1, sticky=NSEW)
app_info.place(x=30, y=225)

# CHECKBOX DE CARACTERES
estado4 = StringVar()
estado4.set(False)
check_4 = Checkbutton(janela, width=0, var=estado4, onvalue=simbolos, offvalue='off', relief='flat')
check_4.place(x=2, y=250)
app_info = Label(janela, text='Caracteres especiais', height=1, padx=0, relief='flat', anchor='nw',
                  font=('Ivy 11 bold'), fg=cor1)
app_info.grid(row=1, column=0, columnspan=1, sticky=NSEW)
app_info.place(x=30, y=250)

app_gerar_senha = Button(janela, text='Gerar Senha', width=20, command=gerar_senha, height=1, relief='flat', overrelief='solid', anchor='center',  font=('Ivy 10 bold'), bg=cor3, fg=cor2)
app_gerar_senha.grid(row=5, column=0, sticky=NSEW, columnspan=5)
app_gerar_senha.place(x=50, y=300)



janela.mainloop()
