from registros_acoplamiento_segmentacion.if_id import IF_ID


class IF:
    def __init__(self, pc, memoria_instrucciones):
        self.memoria_instrucciones = memoria_instrucciones
        self.instruccion = None
        self.pc = pc
        

    def ejecutar(self):
        self.instruccion = None
        if self.pc.valor in self.memoria_instrucciones.elementos:
            self.instruccion = self.memoria_instrucciones.elementos[self.pc.valor]
            self.pc.avanzar_un_paso()
            return IF_ID(self.instruccion)
        return None
    