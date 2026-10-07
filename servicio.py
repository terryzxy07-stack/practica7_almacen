import bcrypt
import repositorio

def registrar_nuevo_usuario(nombre, correo, password):
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    return repositorio.registrar_usuario(nombre, correo, password_hash)

def validar_login(correo, password_plana):
    usuario = repositorio.buscar_usuario_por_correo(correo)
    if usuario:
        if bcrypt.checkpw(password_plana.encode('utf-8'), usuario['password_hash'].encode('utf-8')):
            return usuario
    return None

def agregar_producto(datos):
    stock = int(datos.get('stock', -1))
    precio = float(datos.get('precio_unitario', 0))
    
    # Validaciones obligatorias de almacén
    if stock < 0:
        return False, "El stock inicial no puede ser negativo."
    if precio <= 0:
        return False, "El precio unitario debe ser mayor a cero."
        
    exito = repositorio.registrar_producto(
        datos['codigo_sku'],
        datos['nombre_producto'],
        datos['descripcion'],
        stock,
        precio,
        datos['categoria']
    )
    
    if exito:
        return True, "Producto registrado con éxito."
    else:
        return False, "Error al registrar producto (¿SKU duplicado?)."

def obtener_inventario():
    return repositorio.listar_productos()