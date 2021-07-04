from tkinter import ttk
from tkinter import *
import tkinter.scrolledtext as scrolledtext
import sqlite3
import Analizador_Sintactico as analizer
# aqui hizo marcos
class Main:
    def __init__(self, window):
        self.wind = window
        self.wind.title('P1:G6: Project Ruby')

        # Componentes
        # titulo = Label(self.wind, text='Ruby Lex', bg= "red")
        # titulo.pack(fill= BOTH, expand = True)
        # frame = LabelFrame(self.wind, text = 'Ruby Lex')
        # frame.grid(row=0, column=0, columnspan=3, pady=20)
        txtEntry = scrolledtext.ScrolledText(self.wind, undo=True, height=5)
        txtEntry.pack()

        botonAnalizar = Button(self.wind, text="Analyze", command=lambda: self.evaluar(txtEntrada= txtEntry, txtSalida= txtOutput))
        botonAnalizar.pack()

        txtOutput = scrolledtext.ScrolledText(self.wind, undo=True, height=5)
        txtOutput.pack()

    def evaluar(self, txtEntrada: scrolledtext.ScrolledText, txtSalida: scrolledtext.ScrolledText):
        entrada = txtEntrada.get("1.0", END)
        salida = analizer.evaluar(entrada)
        txtSalida.delete('0.0', END)

        mensaje = 'Works...'
        if salida:
            mensaje =str(salida)
        txtSalida.insert(END, mensaje)




if __name__ == '__main__':
    window = Tk()
    application = Main(window)
    window.mainloop()

#aqui finalizo marcos