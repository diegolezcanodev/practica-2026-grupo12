"""Base de Datos SQL - Modificación"""

import datetime

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_04 import buscar_persona
import sqlite3

def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    """Implementar la funcion actualizar_persona, que actualiza un registro de
    una persona basado en su id. Devuelve un booleano en base a si encontro el
    registro y lo actualizo o no."""
    
    conexion = sqlite3.connect("tp_python.db")
    cursor = conexion.cursor()
    
    consulta = """
        UPDATE Persona
        SET Nombre = ?, FechaNacimiento = ?, DNI = ?, Altura = ?
        WHERE IdPersona = ?
    """
    cursor.execute(consulta, (nombre, nacimiento, dni, altura, id_persona))
    
    actualizado_exitoso = cursor.rowcount > 0
    
    conexion.commit()
    conexion.close()
    
    return actualizado_exitoso
    
    

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
