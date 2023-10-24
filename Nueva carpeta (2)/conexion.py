import sqlite3

class Conexion():
    def __init__(self):
        self.conexion = sqlite3.connect('DBP1.db')
