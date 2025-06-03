from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola, soy Victor!!").pack(anchor=W)

imagen = Image.open('./21-tkinter/imagenes/metroid_dread.jpeg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=E)

ventana.mainloop()