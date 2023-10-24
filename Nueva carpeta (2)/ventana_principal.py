import tkinter as tk
from ventana_inventario import mostrar_ventana_inventario
from ventana_pedidos import mostrar_ventana_pedidos


def mostrar_ventana_principal(ventana):
    ventana_principal.destroy()
    ventana_principal = tk.Toplevel(ventana)
    ventana_principal.title('Ventana Principal')
    ventana_principal.geometry('800x600')


ventana = tk.Tk()
ventana.title('Ventana Principal')
ventana.geometry('400x300')


# Agregar un botón para mostrar la ventana principal
boton_mostrar_inventario = tk.Button(ventana, text='Mostrar Ventana Inventario', command=lambda:mostrar_ventana_inventario(ventana))
boton_mostrar_inventario.pack()


boton_mostrar_pedidos = tk.Button(ventana, text='Mostrar Ventana Pedidos', command=lambda: mostrar_ventana_pedidos(ventana))
boton_mostrar_pedidos.pack()

ventana.mainloop()
