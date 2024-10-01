from instrucciones.instruccion import Instruccion


class InstruccionAritmeticaLogica(Instruccion):
    def __init__(self, nombre, operandos):
        super().__init__(nombre)
        self.registro_destino = operandos[0]
        self.registro_uno = operandos[1]
        self.registro_dos = operandos[2]

    def imprimir(self):
        return super().imprimir() + ' ' + self.registro_destino + ' ' + self.registro_uno + ' ' + self.registro_dos