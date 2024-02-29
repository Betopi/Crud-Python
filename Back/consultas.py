from Database.conexion  import conectar #importamos la funcion conectar desde el documento de conexion
import mysql.connector #Libreria de conexión
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox
# Obteniendo la funcion de conectar (La conexion como tal) mediante un objeto llamado conexion
conexion = conectar()

#Funcion para mostrar todos los registros en la tabla
def mostrarAll(tabla):
    try:
        cursor = conexion.cursor()
        cursor.callproc('select_todos') #Aqui se usa el proceso almacenado
        for result in cursor.stored_results():
            for row in result.fetchall():
                tabla.insert("", "end", values=row)
    except mysql.connector.Error as e:
        print("Error al mostrar todos los usuarios:", e)
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

#Funcion para eliminar el registro por medio de ID
def eliminar(id_usuario):
    try:
        cursor = conexion.cursor()
        cursor.callproc('delete_id', (id_usuario,))
        conexion.commit()
        print("Usuario con ID {} eliminado exitosamente".format(id_usuario))
    except mysql.connector.Error as e:
        print("Error al eliminar usuario:", e)
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

#Funcion para insertar 
def insertar(username, email, password):
    try: 
        cursor = conexion.cursor()
        cursor.callproc('insert_usuario', (username, email, password))
        conexion.commit()
        print("Usuario insertado exitosamente")
    except mysql.connector.Error as e:
        print("Error al insertar usuario:", e)
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

#Funcion para actualizar por id
def actualizar(id_usuario, username, email, password):
    try:
        cursor = conexion.cursor()
        cursor.callproc('update_id', (id_usuario, username, email, password))
        conexion.commit()
        print("Usuario con ID {} actualizado exitosamente".format(id_usuario))
    except mysql.connector.Error as e:
        print("Error al actualizar usuario:", e)
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

# Funcion para consultar por id
def consultar_id(id_usuario):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        query = "SELECT * FROM usuario WHERE id = %s;"
        cursor.execute(query, (id_usuario,))
        resultado = cursor.fetchone()
        return resultado
    except Exception as e:
        print("Error al seleccionar usuario por ID:", e)
        return None
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def eliminarTodo():
    try:
        cursor = conexion.cursor()
        cursor.callproc('deleteALL')  # Llama al procedimiento almacenado para eliminar todos los registros
        conexion.commit()
        print("Todos los usuarios han sido eliminados exitosamente")
    except mysql.connector.Error as e:
        print("Error al eliminar todos los usuarios:", e)
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()



