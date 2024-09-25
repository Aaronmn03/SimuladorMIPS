from cpu.segmentacion import Segmentacion


class UnidadControl:
    def __init__(self,unidad_procesamiento):
        self.unidad_procesamiento = unidad_procesamiento
        self.segmentacion = Segmentacion(self.unidad_procesamiento)
        print("Se ha creado la Unidad de control")