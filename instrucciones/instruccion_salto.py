from instrucciones.instruccion import Instruccion


class InstruccionSalto(Instruccion):

    def __init__(self, nombre, operandos):
        super().__init__(nombre)
        if len(operandos) != 0:
            self.registro_uno = operandos[0]
            self.registro_dos = operandos[1]
            self.etiqueta = operandos[2]

