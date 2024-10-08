class PC:
    def __init__(self):
        self.valor = 0

    def avanzar_un_paso(self):
        self.valor += 4

    def cambiar_pc(self, valor):
        self.valor = valor