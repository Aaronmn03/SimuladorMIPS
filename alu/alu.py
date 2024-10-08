from instrucciones.instruccion_no_encontrada_excepcion import InstruccionNoEncontradaExcepcion


class ALU:
    pass

    def ejecutar_aritmetico_logica(self,operacion):
        if operacion.nombre == "add":
            return operacion.registro_uno + operacion.registro_dos
        elif operacion.nombre == "sub":
            return operacion.registro_uno - operacion.registro_dos
        elif operacion.nombre == "mul":
            return operacion.registro_uno * operacion.registro_dos
        elif operacion.nombre == "div":
            if operacion.registro_dos != 0:
                return operacion.registro_uno / operacion.registro_dos
            else: 
                return 0 
        elif operacion.nombre == "and":
            return operacion.registro_uno & operacion.registro_dos
        elif operacion.nombre == "or":
            return operacion.registro_uno | operacion.registro_dos
        elif operacion.nombre == "xor":
            return operacion.registro_uno ^ operacion.registro_dos
        elif operacion.nombre == "nor":
            return ~(operacion.registro_uno | operacion.registro_dos)
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
        print("Es un salto")
        return 0
