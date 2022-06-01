from tkinter import *


def calcular():
    label3['text'] = float(entry2.get()) / (float(entry1.get())*float(entry1.get()))
    a1 = float(entry2.get()) / (float(entry1.get()) * float(entry1.get()))
    if a1 < 18.5:
        label4['text'] = 'MAGREZA'
    if a1 >= 18.5 and a1 <= 24.9:
        label4['text'] = 'PESO IDEAL'
    if a1 > 24.9 and a1 <= 29.9:
        label4['text'] = 'SOBREPESO'
    if a1 > 29.9 and a1 <= 39.9:
        label4['text'] = 'OBESIDADE'
    if a1 > 39.9:
        label['text'] = 'OBESIDADE GRAVE'




#criar a janela
janela = Tk()
janela.title('Windows Execute')
janela.geometry('400x200+100+500')#perguntar o porquê de ter +100 e +500 dps
janela.minsize(width=400, height=200)#definir tamanho minimo da janela
janela.maxsize(width=1200, height=600)#definir tamanho maximo da janela
janela.config(bg=('#810F5F'))#definir a cor de background da janela
#criar os widgets
label1 = Label(janela, text='Altura:',font='Arial 16', background='#810F5F', foreground='yellow')
entry1 = Entry(janela,font='Arial 13')

label2 = Label(janela, text='Peso:',font='Arial 16',background='#810F5F', foreground='yellow')
entry2 = Entry(janela,font='Arial 13')

btn3=Button(janela,text='IMC', font='Arial 10', command=calcular, background='light blue')
label3 = Label(janela, text='',font='Arial 16',background='#810F5F', foreground='yellow')
label4 = Label(janela, text='',font='Arial 16',background='#810F5F', foreground='yellow')
#organizar os widgets
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
btn3.grid(column=1)
label3.grid(column=1)
label4.grid(column=1)
#executar a janelaa
janela.mainloop()