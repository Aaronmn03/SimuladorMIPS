from registros_acoplamiento_segmentacion.registro_acoplamiento import RegistroAcoplamiento


class MEM_WB(RegistroAcoplamiento):
    def __init__(self, valor, operacion):
        super().__init__(valor)
        self.operacion = operacion
    
    def devolver_string(self):
        if isinstance(super().devolver_string(),dict):
            aux = super().devolver_string()
            return "Tipo: " + aux['tipo'] +" valor: "+ str(aux['valor']) + " operacion: "+ self.operacion.devolver_string()
        else:
            return self.valor.devolver_string() + " " + self.operacion.devolver_string()