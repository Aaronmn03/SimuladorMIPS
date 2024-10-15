from instrucciones.instruccion_aritmetico_logica import InstruccionAritmeticaLogica
from instrucciones.instruccion_no_encontrada_excepcion import InstruccionNoEncontradaExcepcion
from instrucciones.instruccion_salto import InstruccionSalto
from instrucciones.intruccion_memoria import InstruccionMemoria
from registros_acoplamiento_segmentacion.ex_mem import EX_MEM


class EX:
    def __init__(self,alu):
        self.alu = alu
        self.operacion = None
        

    def ejecutar(self, operacion):
        self.operacion = None
        if operacion is not None:
            self.operacion = operacion.valor
            if isinstance(self.operacion,InstruccionAritmeticaLogica):
                return EX_MEM(self.alu.ejecutar_aritmetico_logica(self.operacion), self.operacion) 
            elif isinstance(self.operacion,InstruccionMemoria):
                return EX_MEM(self.alu.ejecutar_memoria(self.operacion), self.operacion)
            elif isinstance(self.operacion,InstruccionSalto):
                return self.alu.ejecutar_salto(self.operacion)
            else:
                raise InstruccionNoEncontradaExcepcion("Ese tipo de instruccion no existe")
        else:
            return None
        