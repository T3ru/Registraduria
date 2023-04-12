from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorPermiso import ControladorPermiso
from Controladores.ControladorRol import ControladorRol
from Controladores.ControladorPermisoRol import ControladorPermisoRol

app = Flask(__name__)
"""
Los cors permiten que se puedan hacer pruebas al 
servidor desde las misma máquina donde está corriendo.
"""
cors = CORS(app)

"""
Implementacion de los controladores
"""
miControladorPermiso= ControladorPermiso()
miControladorRol = ControladorRol()
miControladorPermisoRol= ControladorPermisoRol()

"""
Servicios que el servidor ofrecerá; se definen las rutas
y tipos de peticiones a las cuales el servidor responderá CRUD.
"""
#########################Servicios Permisos###################################
@app.route("/permisos", methods=['GET'])
def getPermiso():
    json = miControladorPermiso.index()
    return jsonify(json)


@app.route("/permisos", methods=['POST'])
def crearPermiso():
    data = request.get_json()
    json = miControladorPermiso.create(data)
    return jsonify(json)


@app.route("/permisos/<string:id>", methods=['GET'])
def getPermisos(id):
    json = miControladorPermiso.show(id)
    return jsonify(json)


@app.route("/permisos/<string:id>", methods=['PUT'])
def modificarPermiso(id):
    data = request.get_json()
    json = miControladorPermiso.update(id, data)
    return jsonify(json)


@app.route("/permisos/<string:id>", methods=['DELETE'])
def eliminarPermiso(id):
    json = miControladorPermiso.delete(id)
    return jsonify(json)

#########################Servicios Rol###################################
@app.route("/roles", methods=['GET'])
def getRoles():
    json = miControladorRol.index()
    return jsonify(json)


@app.route("/roles", methods=['POST'])
def crearRol():
    data = request.get_json()
    json = miControladorRol.create(data)
    return jsonify(json)


@app.route("/roles/<string:id>", methods=['GET'])
def getRol(id):
    json = miControladorRol.show(id)
    return jsonify(json)


@app.route("/roles/<string:id>", methods=['PUT'])
def modificarRol(id):
    data = request.get_json()
    json = miControladorRol.update(id, data)
    return jsonify(json)


@app.route("/roles/<string:id>", methods=['DELETE'])
def eliminarRol(id):
    json = miControladorRol.delete(id)
    return jsonify(json)

##############################################################################

#########################Servicios PermisoRol###################################
@app.route("/permisosRoles/<string:id>", methods=['GET'])
def getPermisoRol(id):
    json = miControladorPermisoRol.show(id)
    return jsonify(json)


@app.route("/permisosRoles/permiso/<string:id_permiso>/rol/<string:id_rol>", methods=['POST'])
def crearPermisoRol(id_permiso, id_rol):
    data = request.get_json()
    json = miControladorPermisoRol.create(data,id_permiso,id_rol)
    return jsonify(json)


@app.route("/permisosRoles/<string:id_permiso_rol>/permiso/<string:id_permiso>/rol/<string:id_rol>", methods=['PUT'])
def modificarInscripcion(id_permiso_rol, id_permiso, id_rol):
    data = request.get_json()
    json = miControladorPermisoRol.update(id_permiso_rol, data, id_permiso, id_rol)
    return jsonify(json)


@app.route("/permisosRoles/<string:id_permiso_rol>", methods=['DELETE'])
def eliminarPermisoRol(id_permiso_rol):
    json = miControladorPermisoRol.delete(id_permiso_rol)
    return jsonify(json)




##############################################################################
"""
Servicio que el servidor ofrecerá, y este consiste en retornar un JSON el cual
tiene un mensaje que dice que el servidor está corriendo.
"""


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


"""
Método leer el archivo de configuración del proyecto,
retornará un diccionario el cual posee la información dentro del
JSON y se podrá acceder a los atributos necesarios.
"""


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()  # Se asigna lo que retorna el metodo a la variable dataConfig
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    """
    Se crea la instancia del servidor con la url del backend y puerto especificado 
    en el archivo de configuración.
    """
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])