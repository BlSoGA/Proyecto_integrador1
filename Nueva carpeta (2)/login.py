import tkinter as tk
import sqlite3

fondo_botones = '#F89EFA'
fondo_pantalla = '#FFFFFF'
fondo_entrada = '#C3BCBC'
def login(usuario_var, contraseña_var, ventana):
    usuario = usuario_var.get()
    contraseña = contraseña_var.get()

    con = sqlite3.connect('DBP1.db')
    cursor = con.cursor()

    cursor.execute("SELECT * FROM Usuario WHERE Nombre_usuario = ? AND contraseña = ?", (usuario, contraseña))
    resultado = cursor.fetchone()

    if resultado:
        print('bienvenido al sistema')
        ventana.withdraw()
        from ventana_principal import mostrar_ventana_principal
        mostrar_ventana_principal(ventana)
    else:
        print('Usuario o contraseña incorrectos')
        usuario_label = tk.Label(ventana, text="Usuario o contraseña incorrecto", font=('Arial', 16))
        usuario_label.pack()

def mostrar_login(ventana):
    usuario_label = tk.Label(ventana, text="Usuario", font=('Arial', 16))
    usuario_label.pack()
    usuario_label.place(x=60, y=150)
    usuario_var = tk.StringVar()
    usuario_entrada = tk.Entry(ventana, textvar=usuario_var, width=20, font=('Arial', 15), relief='flat', bg=fondo_entrada)
    usuario_entrada.pack()
    usuario_entrada.place(x=185, y=150)

    contraseña_label = tk.Label(ventana, text="Contraseña", font=('Arial', 16))
    contraseña_label.pack()
    contraseña_label.place(x=60, y=204)
    contraseña_var = tk.StringVar()
    contraseña_entrada = tk.Entry(ventana, show='*', textvar=contraseña_var, width=20, font=('Arial', 15), relief='flat', bg=fondo_entrada)
    contraseña_entrada.pack()
    contraseña_entrada.place(x=185, y=204)

    boton_login = tk.Button(ventana, text='Entrar', cursor='hand2', bg=fondo_botones, width=15, font=('Arial', 12, 'bold'), relief='flat', command=lambda: login(usuario_var, contraseña_var, ventana))
    boton_login.pack()
    boton_login.place(x=180, y=300)
