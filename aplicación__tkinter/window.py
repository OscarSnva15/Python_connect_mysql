#crear la ventana
from tkinter import *


#definir ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto Tkinter - Master in pyhton")
ventana.resizable(0,0)

#crear texto
text = Text(ventana, width=40, height=10)
text.insert('1.0', 'here is my\ntext to insert')

#cargar ventana
ventana.mainloop()
