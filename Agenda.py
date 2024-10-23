import json

# Clase para cada tarea 
class Tarea:
    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo
        self.completada = False

    # para marcar si la tarea fue completada
    def marcar_completada(self):
        self.completada = True

    # formato de texto
    def __repr__(self):
        return f"Tarea(id={self.id}, titulo='{self.titulo}', completada={self.completada})"
    
class OpcionesEjecutar:
    def __init__(self):
        self.tareas = []


    #agregar nueva tarea
    def agregar_tarea():
        

    #marcar si la tarea esta completada
    def marcar_completada():
        

    #eliminar una tarea 
    def eliminar_tarea():
        

    #mostrar las tareas pendientes
    def listar_tareas_pendientes():

    #guardar tareas 
    def guardar_tareas():
        

    #mostrar tareas
    def cargar_tareas():
    


