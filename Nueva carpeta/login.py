import tkinter as tk
import sqlite3


# colores
fondo_botones = '#F89EFA'
fondo_pantalla = '#FFFFFF'
fondo_entrada = '#C3BCBC'

def login():
    usuario = usuario_var.get()
    contraseña = contraseña_var.get()

    con = sqlite3.connect('DBP1.db')
    cursor = con.cursor()

    cursor.execute("SELECT * FROM Usuario WHERE Nombre_usuario = ? AND contraseña = ?", (usuario, contraseña))
    resultado = cursor.fetchone()

    if resultado:
        print('bienvenido al sistema')
        correcta()
    else:
        print('Usuario o contraseña incorrectos')
        
def correcta():
    ventana.withdraw()
    window = tk.Toplevel()
    window.title('Bienvenido')
    window.attributes('-zoomed', 1)
    window.resizable(width=True, height=True)

ventana = tk.Tk()
ventana.title('Login')
ventana.geometry('500x500+500+100')
ventana.resizable(width=False, height=False)

# Entrada Usuario
usuario_label = tk.Label(ventana, text="Usuario", font=('Arial', 16))
usuario_label.pack()
usuario_label.place(x=60, y=150)
usuario_var = tk.StringVar()  # Create a StringVar
usuario_entrada = tk.Entry(ventana, textvar=usuario_var, width=20, font=('Arial', 15), relief='flat', bg=fondo_entrada)
usuario_entrada.pack()
usuario_entrada.place(x=185, y=150)

# Entrada Contraseña
contraseña_label = tk.Label(ventana, text="Contraseña", font=('Arial', 16))
contraseña_label.pack()
contraseña_label.place(x=60, y=204)
contraseña_var = tk.StringVar()  # Create a StringVar
contraseña_entrada = tk.Entry(ventana, show='*', textvar=contraseña_var, width=20, font=('Arial', 15), relief='flat', bg=fondo_entrada)
contraseña_entrada.pack()
contraseña_entrada.place(x=185, y=204)

# Login
# botones
boton_login = tk.Button(ventana, text='Entrar', cursor='hand2', bg=fondo_botones, width=15, font=('Arial', 12, 'bold'), relief='flat', command=login)
boton_login.pack()
boton_login.place(x=180, y=300)
ventana.mainloop()
