from tkinter import *


def calcular():
    if entry1.get().isnumeric():
        label3['text'] = float(entry1.get())*1.8+32




#criar a janela
janela = Tk()
janela.title('Windows Execute')
janela.geometry('400x200+100+500')#perguntar o porquê de ter +100 e +500 dps
janela.minsize(width=400, height=200)#definir tamanho minimo da janela
janela.maxsize(width=1200, height=600)#definir tamanho maximo da janela
janela.config(bg=('#810F5F'))#definir a cor de background da janela
#criar os widgets
label1 = Label(janela, text='C°:',font='Arial 16', background='#810F5F', foreground='yellow')
entry1 = Entry(janela,font='Arial 13')

btn3=Button(janela,text='Converte F°', font='Arial 10', command=calcular, background='light blue')
label3 = Label(janela, text='F°',font='Arial 16',background='#810F5F', foreground='yellow')
#organizar os widgets
label1.pack()
entry1.pack()
btn3.pack()
label3.pack()
janela.mainloop()