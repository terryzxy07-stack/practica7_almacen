from db import obtener_conexion

def registrar_usuario(nombre, correo, password_hash):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO usuarios_almacen (nombre, correo, password_hash) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nombre, correo, password_hash))
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            conexion.close()
    return False

def buscar_usuario_por_correo(correo):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            sql = "SELECT * FROM usuarios_almacen WHERE correo = %s"
            cursor.execute(sql, (correo,))
            usuario = cursor.fetchone()
            return usuario
        finally:
            cursor.close()
            conexion.close()
    return None

def registrar_producto(codigo_sku, nombre, descripcion, stock, precio, categoria):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            sql = """INSERT INTO productos_inventario 
                     (codigo_sku, nombre_producto, descripcion, stock, precio_unitario, categoria) 
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (codigo_sku, nombre, descripcion, stock, precio, categoria))
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            conexion.close()
    return False

def listar_productos():
    conexion = obtener_conexion()
    productos = []
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            sql = "SELECT * FROM productos_inventario"
            cursor.execute(sql)
            productos = cursor.fetchall()
        finally:
            cursor.close()
            conexion.close()
    return productos