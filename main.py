import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

iniciais = []
vendas = []
sobras = []


def abrirIniciais():
    arquivo = filedialog.askopenfile(
        filetypes=(('Text file', '*.txt'),))
    texto = arquivo.read()
    lista = texto.split('\n')
    for i in lista:
        iniciais.append(i)


def abrirVendas():
    arquivo = filedialog.askopenfile(
        filetypes=(('Text file', '*.txt'),))
    texto = arquivo.read()
    lista = texto.split('\n')
    for i in lista:
        vendas.append(i)


def abrirFinais():
    arquivo = filedialog.askopenfile(
        filetypes=(('Text file', '*.txt'),))
    texto = arquivo.read()
    lista = texto.split('\n')
    for i in lista:
        sobras.append(i)


def conferir():
    vendidos = 0
    sobraram = 0
    faltando = 0
    for iccid in iniciais:
        if iccid in vendas:
            print(f'{iccid}: vendido')
            vendidos += 1
        elif iccid not in vendas:
            if iccid not in sobras:
                print(f'{iccid}: faltando')
                faltando += 1
            else:
                print(f'{iccid}: sobrou')
                sobraram += 1

    for sobra in sobras:
        if sobra not in iniciais:
            print(f'{sobra}: não estava no bipe inicial')

    print('------------------------------\n'
          f'Foram vendidos: {vendidos}\n'
          f'Sobraram: {sobraram}\n'
          f'Faltando: {faltando}')


window = tk.Tk()
window.title('Conferência de chips')
window.geometry('400x250')

titulo_label = ttk.Label(window, text='Conferência dos Chips',
                         font='Calibri 20 bold')
titulo_label.pack()

input_frame1 = ttk.Frame(window)
botao_ini_label = ttk.Label(input_frame1, text='Iniciais: ')
botao_iniciais = ttk.Button(input_frame1, text='Escolher arquivo',
                            command=abrirIniciais)

input_frame2 = ttk.Frame(window)
botao_vend_label = ttk.Label(input_frame2, text='Vendas: ')
botao_vendas = ttk.Button(input_frame2, text='Escolher arquivo',
                          command=abrirVendas)

input_frame3 = ttk.Frame(window)
botao_fin_label = ttk.Label(input_frame3, text='Finais: ')
botao_finais = ttk.Button(input_frame3, text='Escolher arquivo',
                          command=abrirFinais)

input_frame4 = ttk.Frame(window)
botao_conferir = ttk.Button(input_frame4, text='Conferir',
                            command=conferir)

botao_ini_label.pack(side='left')
botao_iniciais.pack(side='left')
botao_vend_label.pack(side='left')
botao_vendas.pack(side='left')
botao_fin_label.pack(side='left')
botao_finais.pack(side='left')
botao_conferir.pack()
input_frame1.pack(pady=5)
input_frame2.pack(pady=5)
input_frame3.pack(pady=5)
input_frame4.pack(pady=6)

window.mainloop()
