from registros_acoplamiento_segmentacion.registro_acoplamiento import RegistroAcoplamiento


class ID_EX(RegistroAcoplamiento):
    def __init__(self,valor):
        super().__init__(valor)
    
    def añadir_valor(self, valor):
        super.añadir_valor(valor)

    def devolver_string(self):
        return str(self.valor.devolver_string())