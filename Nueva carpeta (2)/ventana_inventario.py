import tkinter as tk
import sqlite3
import tkinter as ttk
def mostrar_ventana_inventario(ventana):
    ventana.withdraw()
    ventana_inventario = tk.Toplevel(ventana)
    ventana_inventario.title('Ventana inventario')
    ventana_inventario.geometry('800x600')

    label = tk.Label(ventana_inventario, text="Inventario", font=('Arial',25, 'bold'))
    label.pack() 
    boton_mostrar_pedidos = tk.Button(ventana_inventario, text='Mostrar Ventana Pedidos', command=lambda:mostrar_ventana_principal)
    boton_mostrar_pedidos.pack()
    
    
    
    
    
   
    
    



