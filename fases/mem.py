from instrucciones.instruccion_aritmetico_logica import InstruccionAritmeticaLogica
from instrucciones.intruccion_memoria import InstruccionMemoria
from registros_acoplamiento_segmentacion.mem_wb import MEM_WB
from registros_acoplamiento_segmentacion.registro_acoplamiento import RegistroAcoplamiento


class MEM:
    def __init__(self, memoria_datos):
        self.memoria_datos = memoria_datos

    def ejecutar(self,input):
        if input is not None:
            print("Lo que entra a mem: ",input.operacion.nombre)
            if isinstance(input.operacion,InstruccionAritmeticaLogica):
                valor = input                
            elif isinstance(input.operacion, InstruccionMemoria):
                    if input.operacion.nombre in ['lw','lb']:
                        valor = self.memoria_datos.devolver_dato(input)
                    else:
                        if input.operacion.nombre == 'sb':
                            self.memoria_datos.añadir_dato(input.operacion.direccion_memoria, 'byte',input.valor)
                            return None
                        elif input.operacion.nombre == 'sw':
                            
                            self.memoria_datos.añadir_dato(input.operacion.direccion_memoria, 'word',input.valor)
                            return None
            else: 
                return None       
            
            registro_acoplamiento = MEM_WB(valor, input.operacion)
            return registro_acoplamiento
        else:
            return None