from asyncore import read
import sqlite3

def insert_rows(list): #Función para insertar varios usuarios con una lista
    conn = sqlite3.connect('miscursos.db')
    cursor = conn.cursor()
    instruccion = f"INSERT INTO alumnos VALUES(?, ?, ?)"
    cursor.executemany(instruccion, list)
    datos = cursor.fetchall()
    print(datos)
    conn.commit()
    cursor.close()
    conn.close()

listaAlumnos = [
    (1, 'Ana', 'Perez'),
    (2, 'Eduardo', 'Colcha'),
    (3, 'Maria', 'Usuaria'),
    (4, 'Simon', 'Bolivar'),
    (5, 'Ernestina', 'Amiga'),
    (6, 'Claudio', 'Dominguez'),
    (7, 'Simonela', 'Truty'),
    (8, 'Elvira', 'Amateur'),
]

def search(): #Busca una fila de datos
    name = input('Nombre de alumno: ')
    conn = sqlite3.connect('miscursos.db')
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM alumnos WHERE nombre='{name}'"
    cursor.execute(instruccion)
    datos = cursor.fetchone()
    print(datos)
    conn.commit()
    cursor.close()
    conn.close()

#insert_rows(listaAlumnos)
search()