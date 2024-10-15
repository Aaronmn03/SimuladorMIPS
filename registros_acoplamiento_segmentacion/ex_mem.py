from instrucciones.instruccion_salto import InstruccionSalto
from registros_acoplamiento_segmentacion.registro_acoplamiento import RegistroAcoplamiento


class EX_MEM(RegistroAcoplamiento):
    def __init__(self, valor, operacion):
        super().__init__(valor)
        self.operacion = operacion

    def devolver_string(self):
        if isinstance(self.operacion, InstruccionSalto):
            return "Salto a: " + super().devolver_string() + "Operacion ejecutada: "+ self.operacion.devolver_string()
        else:
            return "Operacion ejecutada: "+ self.operacion.devolver_string()