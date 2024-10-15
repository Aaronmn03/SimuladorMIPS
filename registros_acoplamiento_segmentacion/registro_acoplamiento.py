class RegistroAcoplamiento:
    def __init__(self,valor):
        self.valor = valor
    
    def añadir_valor(self, valor):
        self.valor = valor

    def devolver_string(self):
        return self.valor