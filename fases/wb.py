from instrucciones.instruccion_aritmetico_logica import InstruccionAritmeticaLogica
from instrucciones.intruccion_memoria import InstruccionMemoria


class WB:
    def __init__(self, registros):
        self.registros = registros
        self.operacion = None

    def ejecutar(self, input):
        if input is not None:
            self.operacion = input
            if isinstance(input.operacion,InstruccionMemoria):
                if input.operacion.nombre in ['lw', 'lb']:
                    self.registros.cargar_dato(input.operacion.registro,input.valor['valor']) 
                    self.registros.mostrar_registros()
            
            if isinstance(input.operacion,InstruccionAritmeticaLogica):
                self.registros.cargar_dato(input.operacion.registro_destino,input.valor.valor) 
                self.registros.mostrar_registros()
