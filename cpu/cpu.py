from cpu.unidad_control import UnidadControl
from cpu.unidad_procesamiento import UnidadProcesamiento


class CPU:
    def __init__(self):
        self.unidad_procesamiento = UnidadProcesamiento()
        self.unidad_control = UnidadControl(self.unidad_procesamiento)
        print("Se ha creado la CPU")

    def leer_fichero(self, archivo):
        fichero = open(archivo)
        contenido_fichero = fichero.read()
        self.dividir_contenido_archivo(contenido_fichero)
        fichero.close()

    def dividir_contenido_archivo(self,datos):
        datos_memoria = datos.split('.text',1)[0]
        instrucciones = datos.split('.text',1)[1]
        self.cargar_memoria_datos(datos_memoria)
        pass

    def cargar_memoria_datos(self, datos):
        self.unidad_procesamiento.cargar_memoria_datos(datos)
