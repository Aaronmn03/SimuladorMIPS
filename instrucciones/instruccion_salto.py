from instrucciones.instruccion import Instruccion


class InstruccionSalto(Instruccion):

    def __init__(self, nombre, operandos):
        super().__init__(nombre)
        if len(operandos) != 1:
            self.registro_uno = operandos[0]
            self.registro_dos = operandos[1]
            self.etiqueta = operandos[2]
        else:
            self.etiqueta = operandos[0]

    def imprimir(self):
        if not hasattr(self, 'registro_uno'):
            return super().imprimir() + ' ' + self.etiqueta
        else:
            return super().imprimir() + ' ' + self.registro_uno + ' ' + self.registro_dos + ' ' + self.etiqueta


