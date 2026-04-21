"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime

from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_06 import reset_tabla
from practico_04.ejercicio_04 import buscar_persona

import sqlite3

def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""

    # buscar persona
    if not buscar_persona(id_persona):
        return False

    conexion = sqlite3.connect("tp_python.db")
    cursor = conexion.cursor()
    
    # buscar fecha mas reciente
    cursor.execute("""
        SELECT Fecha FROM PersonaPeso 
        WHERE IdPersona = ? 
        ORDER BY Fecha DESC LIMIT 1
    """, (id_persona,))
    
    ultimo_registro = cursor.fetchone()
    
    if ultimo_registro:
        fecha_ultimo = datetime.datetime.strptime(ultimo_registro[0].split(".")[0], '%Y-%m-%d %H:%M:%S')
        if fecha > fecha_ultimo:
            pass 
        else:
            conexion.close()
            return False # la fecha ingresada es vieja o igual a la última
            
    
    cursor.execute("""
        INSERT INTO PersonaPeso (IdPersona, Fecha, Peso)
        VALUES (?, ?, ?)
    """, (id_persona, fecha, peso))
    
    
    id_generado = cursor.lastrowid
    
    conexion.commit()
    conexion.close()
    
    return id_generado


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
