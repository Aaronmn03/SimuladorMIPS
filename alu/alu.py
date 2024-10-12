from instrucciones.instruccion_no_encontrada_excepcion import InstruccionNoEncontradaExcepcion


class ALU:
    pass

    def ejecutar_aritmetico_logica(self,operacion):
        if operacion.nombre == "add":
            return operacion.valor_uno + operacion.valor_dos
        elif operacion.nombre == "sub":
            return operacion.valor_uno - operacion.valor_dos
        elif operacion.nombre == "mul":
            return operacion.valor_uno * operacion.valor_dos
        elif operacion.nombre == "div":
            if operacion.valor_dos != 0:
                return operacion.valor_uno / operacion.valor_dos
            else: 
                return 0 
        elif operacion.nombre == "and":
            return operacion.valor_uno & operacion.valor_dos
        elif operacion.nombre == "or":
            return operacion.valor_uno | operacion.valor_dos
        elif operacion.nombre == "xor":
            return operacion.valor_uno ^ operacion.valor_dos
        elif operacion.nombre == "nor":
            return ~(operacion.valor_uno | operacion.valor_dos)
        else:
            raise InstruccionNoEncontradaExcepcion("No se ha encontrado el tipo de aritmetico-logica")
        
    def ejecutar_memoria(self,operacion): #Preguntar esto, y como seria la diferencia entre el lw y el lb
        if operacion.nombre == "lw":
            return operacion.direccion_memoria
        elif operacion.nombre == "lb":
            return operacion.direccion_memoria
        elif operacion.nombre == "sw":
            return operacion.registro
        elif operacion.nombre == "sb":
            return operacion.registro
        else:
            raise InstruccionNoEncontradaExcepcion("No se ha encontrado el tipo de operacion de memoria")
    
    def ejecutar_salto(self,operacion):
        if operacion.nombre == "j":
            resultado_salto = {
                'salto': True,
                'direccion': operacion.etiqueta
            }
        elif operacion.nombre == "bne":
            if operacion.registro_uno - operacion.registro_dos != 0:
                resultado_salto = {
                    'salto': True,
                    'direccion': operacion.etiqueta
                }
            else:
                return None
        elif operacion.nombre == "beq":
            if operacion.registro_uno - operacion.registro_dos == 0:
                resultado_salto = {
                    'salto': True,
                    'direccion': operacion.etiqueta
                }
            else:
                return None
        else:
            raise InstruccionNoEncontradaExcepcion("No se ha encontrado el tipo de operacion de salto")
        return resultado_salto
