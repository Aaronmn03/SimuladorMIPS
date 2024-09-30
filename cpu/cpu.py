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
        self.unidad_procesamiento.dividir_contenido_archivo(contenido_fichero)
        fichero.close()