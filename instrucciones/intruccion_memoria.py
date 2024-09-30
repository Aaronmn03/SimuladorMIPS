from instrucciones.instruccion import Instruccion


class InstruccionMemoria(Instruccion):
    
    def __init__(self, nombre, operandos):
        super().__init__(nombre)
        self.registro = operandos[0]
        self.direccion_memoria = operandos[1]
