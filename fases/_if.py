from registros_acoplamiento_segmentacion.registro_acoplamiento import RegistroAcoplamiento


class IF:
    def __init__(self, pc, memoria_instrucciones):
        self.memoria_instrucciones = memoria_instrucciones
        self.pc = pc
        

    def ejecutar(self):
        if self.pc.valor in self.memoria_instrucciones.elementos:
            aux = self.memoria_instrucciones.elementos[self.pc.valor]
            self.pc.avanzar_un_paso()
            return RegistroAcoplamiento(aux)
        return None