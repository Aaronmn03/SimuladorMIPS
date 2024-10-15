from instrucciones.instruccion import Instruccion


class InstruccionMemoria(Instruccion):
    
    def __init__(self, nombre, operandos):
        super().__init__(nombre)
        self.registro = operandos[0]
        self.direccion_memoria = operandos[1]

    def devolver_string(self):
        return super().devolver_string() + ' ' + str(self.registro) + ' ' + str(self.direccion_memoria)
    
    def esta_registro_en_destino(self, lregistros):
        for registro_aux in lregistros:
            if registro_aux == self.registro:
                print("tenemos raw con(memoria): "+ str(registro_aux) + str(self.registro))
                return True
        return False
        
    def registros_operandos(self):
        return [self.registro]