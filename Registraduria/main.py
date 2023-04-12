from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPermiso import ControladorPermiso
from Controladores.ControladorResultado import ControladorResultado

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
miControladorCandidato = ControladorCandidato()
miControladorMesa = ControladorMesa()
miControladorResultado = ControladorResultado()



"""
Servicios que el servidor ofrecerá; se definen las rutas
y tipos de peticiones a las cuales el servidor responderá CRUD.
"""
#########################Servicios Permisos###################################
@app.route("/Permisos", methods=['GET'])
def getPermisos():
    json = miControladorPermiso.index()
    return jsonify(json)


@app.route("/Permisos", methods=['POST'])
def crearPermiso():
    data = request.get_json()
    json = miControladorPermiso.create(data)
    return jsonify(json)


@app.route("/Permisos/<string:id>", methods=['GET'])
def getPermiso(id):
    json = miControladorPermiso.show(id)
    return jsonify(json)


@app.route("/Permisos/<string:id>", methods=['PUT'])
def modificarPermiso(id):
    data = request.get_json()
    json = miControladorPermiso.update(id, data)
    return jsonify(json)


@app.route("/Permisos/<string:id>", methods=['DELETE'])
def eliminarPermiso(id):
    json = miControladorPermiso.delete(id)
    return jsonify(json)


"""

"""
""" 
MESA 
"""


@app.route("/mesas", methods=['GET'])
def getMesas():
   json = miControladorMesa.index()
   return jsonify(json)


@app.route("/mesas", methods=['POST'])
def crearMesa():
   data = request.get_json()
   json = miControladorMesa.create(data)
   return jsonify(json)


@app.route("/mesas/<string:id>", methods=['GET'])
def getMesa(id):
   json = miControladorMesa.show(id)
   return jsonify(json)


@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesas(id):
   data = request.get_json()
   json = miControladorMesa.update(id, data)
   return jsonify(json)


@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
   json = miControladorMesa.delete(id)
   return jsonify(json)


@app.route("/", methods=['GET'])
def test():
   json = {}
   json["message"] = "Server running ..."
   return jsonify(json)


##########################Servicios Inscripcion###############################

@app.route("/resultados", methods=['GET'])
def getResultados():
    json = miControladorResultado.index()
    return jsonify(json)


@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)


@app.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=['POST'])
def crearResultado(id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.create(data, id_mesa, id_candidato)
    return jsonify(json)


@app.route("/resultados/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=['PUT'])
def modificarCandidato(id_resultado, id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.update(id_resultado, data, id_mesa, id_candidato)
    return jsonify(json)


@app.route("/resultados/<string:id_resultado>", methods=['DELETE'])
def eliminarResultado(id_resultado):
    json = miControladorResultado.delete(id_resultado)
    return jsonify(json)



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
