from flask import Flask, jsonify, request
from Agenda import OpcionesEjecutar, Tarea #importamos nuestro archivo

app = Flask(__name__)
opciones = OpcionesEjecutar()#lee los metodos

#Muestra las tareas
@app.route('/tareas', methods=['GET'])#definmos ruta
def ObtenerTareas():
    return jsonify([{'id': tarea.id, 'titulo': tarea.titulo, 'completada': tarea.completada} for tarea in opciones.tareas])#devuelve lista de tareas


#añadir tarea
@app.route('/tareas', methods=['POST'])
def NuevaTarea():
    datos = request.get_json()#obtiene la peticion
    nuevatarea = Tarea(len(opciones.tareas) + 1, data['titulo'])
    opciones.NuevaTarea(datos['titulo'])#se crea y añade la tarea
    return jsonify({'mensaje': 'Añadida', 'id': nuevatarea.id}), 201


