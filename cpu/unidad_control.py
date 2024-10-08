from cpu.segmentacion import Segmentacion


class UnidadControl:
    def __init__(self,unidad_procesamiento):
        self.unidad_procesamiento = unidad_procesamiento
        self.segmentacion = Segmentacion(self.unidad_procesamiento)

    def empezar_segmentacion(self):
        self.segmentacion.empezar_segmentacion()