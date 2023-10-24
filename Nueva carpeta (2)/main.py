import tkinter as tk
from login import mostrar_login

ventana = tk.Tk()
ventana.title('Sistema de Inventario')
ventana.geometry('500x500+500+100')
ventana.resizable(width=False, height=False)

mostrar_login(ventana)

ventana.mainloop()