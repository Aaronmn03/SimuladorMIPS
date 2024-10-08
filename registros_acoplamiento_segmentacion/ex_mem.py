from registros_acoplamiento_segmentacion.registro_acoplamiento import RegistroAcoplamiento


class EX_MEM(RegistroAcoplamiento):
    def __init__(self, valor, operacion):
        super().__init__(valor)
        self.operacion = operacion