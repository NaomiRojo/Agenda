from flask import Flask, jsonify, request
from Agenda import OpcionesEjecutar, Tarea #importamos nuestro archivo

app = Flask(__name__)
opciones = OpcionesEjecutar()#lee los metodos

#Muestra las tareas
@app.route('/tareas', methods=['GET'])
def ObtenerTareas():
    return jsonify([{'id': tarea.id, 'titulo': tarea.titulo, 'completada': tarea.completada} for tarea in opciones.tareas])

