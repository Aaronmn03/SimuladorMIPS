from instrucciones.instruccion import Instruccion


class InstruccionAritmeticaLogica(Instruccion):
    def __init__(self, nombre, operandos):
        super().__init__(nombre)
        self.registro_destino = operandos[0]
        self.registro_uno = operandos[1]
        self.registro_dos = operandos[2]
        self.valor_uno = operandos[3]
        self.valor_dos = operandos[4]

    def imprimir(self):
        return super().imprimir() + ' ' + self.registro_destino + ' ' + str(self.registro_uno) + ' ' + str(self.registro_dos)
    
    def esta_registro_en_destino(self, lregistros):
        if lregistros is not None:
            for registro_aux in lregistros:
                if registro_aux == self.registro_destino:
                    print("tenemos raw con: "+ str(registro_aux) + str(self.registro_destino))
                    return True
        return False
    
    def registros_operandos(self):
        return [self.registro_uno,self.registro_dos]