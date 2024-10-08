from instrucciones.intruccion_memoria import InstruccionMemoria


class WB:
    def __init__(self, registros):
        self.registros = registros

    def ejecutar(self, input):
        if input is not None:
            if isinstance(input.operacion,InstruccionMemoria):
                if input.operacion.nombre in ['lw', 'lb']:
                    print("Estamos en WB: ", input.valor)
                    self.registros.cargar_dato(input.operacion.registro,input.valor['valor']) 
                    self.registros.mostrar_registros()