from memoria.memoria import Memoria


class MemoriaInstrucciones(Memoria):
    def __init__(self):
        super().__init__()
        print("de instrucciones")