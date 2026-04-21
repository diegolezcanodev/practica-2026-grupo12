"""Base de Datos SQL - Creación de tablas auxiliares"""

from practico_04.ejercicio_01 import borrar_tabla, crear_tabla
import sqlite3

def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    
    conexion = sqlite3.connect("tp_python.db")
    cursor = conexion.cursor()
    
    #claves foraneas
    cursor.execute("PRAGMA foreign_keys = ON")
    
    consulta = """
        CREATE TABLE IF NOT EXISTS PersonaPeso (
            IdPersona INTEGER,
            Fecha DATE,
            Peso INTEGER,
            FOREIGN KEY (IdPersona) REFERENCES Persona (IdPersona)
        )
    """
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()
    print("Tabla PersonaPeso creada")
    


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    
    conexion = sqlite3.connect("tp_python.db")
    cursor = conexion.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS PersonaPeso")
    
    conexion.commit()
    conexion.close()
    print("Tabla PersonaPeso borrada")
    


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN

