#PROYECTO FINAL DE PYTHON
#Loriel Ramirez Sanchez
import sqlite3
class Person:
    def __init__(self, Nombre, Numero):
        self.Nombre = Nombre
        self.Numero = Numero
 
def crear_conexion(base_datos):
    try:
        con = sqlite3.connect("base_datos")
        return con
    except sqlite3.error as error:
        print("Se ha producido un error en crear la conexion", error)

def crear_tabla(con, definicion):
    cursor = con.cursor()
    cursor.execute(definicion)
    con.commit()

con = crear_conexion('contactos.db')
 
sql = """ 
CREATE TABLE  IF NOT EXISTS Contacto (
    contactId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    contactName VARCHAR (50) NOT NULL,
    contactNumber INTEGER NOT NULL
    );
"""
crear_tabla(con, sql)

 
def insertar(p):
    con = sqlite3.connect("base_datos")
    cursor = con.cursor()
    cursor.execute(""" INSERT INTO Contacto VALUES (NULL,?,?) """, (p.Nombre, p.Numero))
    print ("Usted ha agregado este contacto nuevo " + p.Nombre, p.Numero)
 
 
def mostrar():
    con = sqlite3.connect("base_datos")
    cursor = con.cursor()
    cursor.execute(""" SELECT * FROM Contacto """)
    resultado = cursor.fetchall()
    print(resultado)
 
 
def buscar(a3):
    con = sqlite3.connect("base_datos")
    cursor = con.cursor()
    cursor.execute(""" SELECT * FROM Contacto WHERE contactId = ? """, (a3,))
    resultado = cursor.fetchall()
    print(resultado)
 
def actualizar(a4,a5):
    con = sqlite3.connect("base_datos")
    cursor = con.cursor()
    cursor.execute(""" UPDATE Contacto SET contactNumber = ? WHERE contactId = ? """, (a5, a4))
 
 
def eliminar(a6):
    con = sqlite3.connect("base_datos")
    cursor = con.cursor()
    cursor.execute(""" DELETE FROM Contacto WHERE contactId = ? """, (a6,))
 
 
c = 0
def imprimir_texto():
    print ("1. Agregar contacto nuevo, 2. Ver lista de contactos, 3.Buscar contacto, 4. Actualizar contacto, 5. Borrar contacto, 6.Salir: ")
    global c
    c = int(input())
    print ("Su ultima elección fue: " + str(c))
 
 
imprimir_texto()
def menu():
    #print ("1. Agregar contacto nuevo, 2. Ver lista de contactos, 3.Buscar contacto, 4. Actualizar contacto, 5. Borrar contacto, 6.Salir: ")
    #imprimir_texto()
    global c
    if c == 1:
        a1 = input("Escriba el nombre: ")
        a2 = int(input("Escriba el numero: "))
        p = Person(a1,a2)
        insertar(p)
        imprimir_texto()
    elif c == 2:
        mostrar()
        imprimir_texto()
    elif c == 3:
        a3 = int(input("Ingrese el Id del contacto: "))
        buscar(a3)
        imprimir_texto()
    elif c == 4:
        a4 = int(input("Ingrese el Id del contacto: "))
        a5 = int(input("Ingrese el nuevo numero del contacto: "))
        actualizar(a4,a5)
        imprimir_texto()
    elif c == 5:
        a6 = int(input("Ingrese el Id del contacto: "))
        eliminar(a6)
        imprimir_texto()
    elif c == 6:
        print ("Usted ha salido de la agenda")
 
 
 
 
while c != 6:
    menu()
 
 
con.commit()

if con:
    con.close()