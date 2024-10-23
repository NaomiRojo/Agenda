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
    def GuardarTareas(self):
        # en un archivo txt guarda las tareas en formato json
        with open('tareas.txt', 'w') as t:#el archivo se llama tareas
            for tarea in self.tareas:
                tar = {#por cada tarea un diccionario
                    'id': tarea.id,
                    'titulo': tarea.titulo,
                    'completada': tarea.completada
                }
                t.write(json.dumps(tar) + '\n')#le da el formato como json
        print("Guardado")

        

    #mostrar tareas
    def VerTareas(self, archivo):
        #todo sera en formato json
        tareas = []#se guardaran las tareas
    #leera el txt
        with open(archivo, 'r') as f:
            # Lee todas las líneas del archivo
            for line in f:
                tarea_data = json.loads(line)#de json a diccionario
                tarea = Tarea(tarea_data['id'], tarea_data['titulo'])#crea ya añade la tarea
                tarea.completada = tarea_data['completada']#completada s/n
                tareas.append(tarea)#la agrega a la lista
        return tareas
    


def MenuOp():
    opciones = OpcionesEjecutar()
    
    while True:
        print("\nOpciones")
        print("1) Añadir tarea")
        print("2) Eliminar tarea")
        print("3) Marcar tarea como completada")
        print("4) Listar tareas pendientes")
        print("5) Guardar y salir")
        
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            titulo = input("Ingrese el titulo de su tarea: ")#coloca titulo
            opciones.NuevaTarea(titulo)  # Agrega la nueva tarea
        
        elif opcion == '2':
            id_tarea = int(input("ingrese el id de la tarea a borrar"))#pide id
            opciones.BorarTarea(id_tarea)  # Elimina la tarea
        
        elif opcion == '3':
            id_tarea = int(input("ingrese el id de la tarea completada "))#pide id
            opciones.TareasCompletadas(id_tarea)#marca la tarea
        
        elif opcion == '4':
            pendientes = opciones.TareasPendientes()#muestra los pendientes
            if pendientes:
                print("\nTareas Pendientes")
                for tarea in pendientes:
                    print(tarea)
            else:
                print("Sin pendientes")
        
        elif opcion == '5':
            opciones.GuardarTareas()#se guardan las tareas y termina
            print("Listo")
            break
        
        else:
            print("Opción inválida, intente otra vez")  

#gestión de tareas en consola
if __name__ == "__main__":
    MenuOp() #muestra las opciones al verificar el archivo









""" mi enfoque esta en dividir el problema en pequeñas partes que pueda resolver por separado,
el analisis inicia con las entradas y salidas del programa, seguido de los procesos que se llevaran a cabo,
y replanteamineto de la estrategia para cumplir con el requerimiento. """
