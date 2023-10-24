import tkinter as tk

def mostrar_ventana_pedidos(ventana):
    ventana.destroy()
    ventana_principal = tk.Toplevel(ventana)
    ventana_principal.title('Ventana Pedidos')
    ventana_principal.geometry('800x600')
