from cpu.unidad_control import UnidadControl
from cpu.unidad_procesamiento import UnidadProcesamiento


class CPU:
    def __init__(self):
        self.unidad_procesamiento = UnidadProcesamiento()
        self.unidad_control = UnidadControl(self.unidad_procesamiento)
        print("Se ha creado la CPU")