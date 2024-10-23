import json

# Clase para cada tarea 
class Tarea:
    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo
        self.completada = False

    # para marcar si la tarea fue completada
    def MarcarCompletada(self):
        self.completada = True

    # formato de texto
    def __repr__(self):
        return f"Tarea(id={self.id}, titulo='{self.titulo}', completada={self.completada})"
    
class OpcionesEjecutar:
    def __init__(self):
        self.tareas = self.VerTareas('tareas.txt')#carga las tareas del archivo txt


    #agregar nueva tarea
    def NuevaTarea(self,titulo):
        id_tarea = len(self.tareas) + 1
        nueva_tarea = Tarea(id_tarea, titulo)  
        self.tareas.append(nueva_tarea)  
        print(f"La tarea '{titulo}' fue agregada, ID: {id_tarea}")
        # se añade una nueva tarea

    #marcar si la tarea esta completada
    def TareasCompletadas(self, id):
        for tarea in self.tareas:#busca la tarea por su id
            if tarea.id == id:
                tarea.MarcarCompletada()#utiliza el metodo para marcar la tarea
                print(f"Tarea {id} completada")
                break
        

    #eliminar una tarea 
    def BorarTarea(self, id):
        for tarea in self.tareas:#busca la tarea
            if tarea.id == id:  
                self.tareas.remove(tarea)#la elimina si coincide
                print(f"Tarea {id} borrada")
            else : print(f"la tarea {id} no existe")
            
        

    #mostrar las tareas pendientes
    def TareasPendientes(self):
        pendientes = [tarea for tarea in self.tareas if not tarea.completada]#en una nueva lista se añaden las tareas pendientes definidas por completada
        print("\nTareas Pendientes")
        for tarea in pendientes:
            print(tarea)
       

    #guardar tareas 
    def GuardarTareas():
        

    #mostrar tareas
    def VerTareas():
    


