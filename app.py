from flask import Flask, request, jsonify
import servicio

app = Flask(__name__)

@app.route('/api/auth/registro', methods=['POST'])
def registro_usuario():
    datos = request.json
    if not datos or not all(k in datos for k in ("nombre", "correo", "password")):
        return jsonify({"error": "Faltan datos"}), 400
        
    exito = servicio.registrar_nuevo_usuario(datos['nombre'], datos['correo'], datos['password'])
    if exito:
        return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201
    else:
        return jsonify({"error": "No se pudo registrar (correo existente)"}), 400

@app.route('/api/auth/login', methods=['POST'])
def login_usuario():
    datos = request.json
    if not datos or not all(k in datos for k in ("correo", "password")):
        return jsonify({"error": "Faltan datos"}), 400
        
    usuario = servicio.validar_login(datos['correo'], datos['password'])
    if usuario:
        return jsonify({
            "mensaje": "Login exitoso",
            "usuario": {"id": usuario["id"], "nombre": usuario["nombre"]}
        }), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

@app.route('/api/almacen/productos', methods=['POST'])
def registrar_producto():
    datos = request.json
    campos_requeridos = ['codigo_sku', 'nombre_producto', 'descripcion', 'stock', 'precio_unitario', 'categoria']
    
    if not datos or not all(k in datos for k in campos_requeridos):
        return jsonify({"error": "Faltan campos obligatorios"}), 400
        
    exito, mensaje = servicio.agregar_producto(datos)
    if exito:
        return jsonify({"mensaje": mensaje}), 201
    else:
        return jsonify({"error": mensaje}), 400

@app.route('/api/almacen/productos', methods=['GET'])
def listar_inventario():
    productos = servicio.obtener_inventario()
    return jsonify({"productos": productos}), 200

if __name__ == '__main__':
    app.run(debug=True)