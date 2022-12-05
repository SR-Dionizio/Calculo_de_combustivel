from tkinter import *
from tkinter import ttk

#cores
cinza = "#778899"
preto = "#111111"
branco = "#f7f5f5"


#funções
def calcular():
    preco_do_combustivel = float  (input_preco_combustivel.get())
    quilometro_por_litro =  float (input_kml.get())
    quilometros_percorridos = float (input_km_percorrido.get())

    resultado = round((preco_do_combustivel/quilometro_por_litro)*quilometros_percorridos, 2)
    display_resultado.set(f'R${resultado}')

#criando a janela
janela = Tk()
janela.title("Quanto vai custar a sua viagem?")
janela.geometry("600x500")
janela.config(bg= cinza)

#separando os frames
frame_dos_inputs = Frame(janela, width=600, height=350, bg=cinza)
frame_dos_inputs.grid(row=0, column=0)

frame_do_resultado = Frame(janela, width=600, height=150, bg=cinza)
frame_do_resultado.grid(row=1 ,column=0)

#criando o label
titulo_1 = Label(frame_dos_inputs, text= "Bem vindo ao calculador de combustível", width=50, height=3, padx=1, relief="flat", justify=CENTER, anchor="center", font=('Ivy 10 bold'), bg=cinza, fg=branco)
titulo_1.place(y=0, x=95)

titulo_valor_do_combustiel = Label(frame_dos_inputs, text="Digite quanto está o combustível:", width=50, height=3, padx=1, relief="flat", justify=CENTER, anchor="center", font=('Ivy 10 bold'), bg=cinza, fg=branco)
titulo_valor_do_combustiel.place(y=40, x=95)

input_preco_combustivel= Entry(frame_dos_inputs, width=70)
input_preco_combustivel.grid(column=0, row=0)
input_preco_combustivel.place(y=80, x=88)

titulo_kml = Label(frame_dos_inputs, text="Digite quantos km por litro faz o seu carro:", width=50, height=3, padx=1, relief="flat", justify=CENTER, anchor="center", font=('Ivy 10 bold'), bg=cinza, fg=branco)
titulo_kml.place(y=120, x=95)

input_kml= Entry(frame_dos_inputs, width=70)
input_kml.grid(column=0, row=0)
input_kml.place(y=160, x=88)

titulo_km_percorrido = Label(frame_dos_inputs, text="Digite quantos km você vai percorrer:", width=50, height=3, padx=1, relief="flat", justify=CENTER, anchor="center", font=('Ivy 10 bold'), bg=cinza, fg=branco)
titulo_km_percorrido.place(y=210, x=95)

input_km_percorrido= Entry(frame_dos_inputs, width=70)
input_km_percorrido.grid(column=0, row=0)
input_km_percorrido.place(y=250, x=88)

titulo_resultado = Label(frame_do_resultado, text="Você vai gastar:", width=50, height=3, padx=1, relief="flat", justify=CENTER, anchor="center", font=('Ivy 10 bold'), bg=cinza, fg=branco)
titulo_resultado.place(y=0, x=95)

display_resultado = StringVar()
resultado = Label(frame_do_resultado, textvariable= display_resultado, width=50, height=3, padx=1, relief="flat", justify=CENTER, anchor="center", font=('Ivy 10 bold'), bg=cinza, fg=branco)
resultado.place(y=40, x=80)

botao_calcular= Button(frame_dos_inputs, text="Calcular", command=lambda: calcular())
botao_calcular.place(y=280, x=270)

janela.mainloop()