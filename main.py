from tkinter import ttk
from tkinter import *
import sqlite3


class Main:
    def __init__(self, window):
        self.wind = window
        self.wind.title('P1:G6: Proyecto Ruby')


if __name__ == '__main__':
    window = Tk()
    application = Main(window)
    window.mainloop()
