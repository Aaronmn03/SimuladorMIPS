import curses
from cpu.cpu import CPU

class Menu:
    def __init__(self):
        cpu = CPU()
        cpu.leer_fichero("archivos_auxiliares/instrucciones.txt")
        self.unidad_procesamiento = cpu.unidad_procesamiento
        self.segmentacion = cpu.unidad_control.segmentacion    
        curses.wrapper(self.inicializar_menu)
        self.ciclo = 0

    def inicializar_menu(self, stdscr):
        self.ciclo = 0
        curses.curs_set(0)
        stdscr.clear()
        stdscr.refresh()

        height, width = stdscr.getmaxyx()
        menu = ["Avanzar un paso", "Avanzar Todo", "Salir"]
        seleccion = 0
        while True:
            try:
                stdscr.clear()
                self.mostrar_menu(stdscr, menu, seleccion)
                self.mostrar_registros(stdscr, width)
                self.mostrar_datos(stdscr, width)
                self.mostrar_segmentacion(stdscr)
                self.mostrar_instrucciones(stdscr)
                stdscr.refresh()

                key = stdscr.getch()
                seleccion = self.navegar_menu(key, seleccion, len(menu))

                if key in [curses.KEY_ENTER, 10, 13]:
                    if seleccion == len(menu) - 1:
                        break
                    else:
                        self.procesar_seleccion(stdscr, menu[seleccion])
            except curses.error:
                stdscr.addstr(0, 0, "El terminal es demasiado pequeño. Agrándalo e inténtalo de nuevo.")
                stdscr.refresh()
                
    def mostrar_menu(self, stdscr, menu, seleccion):
        for idx, opcion in enumerate(menu):
            if idx == seleccion:
                stdscr.addstr(0, idx * 20, f"> {opcion}", curses.A_REVERSE)
            else:
                stdscr.addstr(0, idx * 20, f"  {opcion}")

    def mostrar_registros(self, stdscr, width):
        num_registros = len(self.unidad_procesamiento.registros.elementos)
        pos_x = width - 35
        stdscr.addstr(1,pos_x, "***Banco de Registros***")
        if num_registros + 1 < stdscr.getmaxyx()[0]:
            for idx, value in enumerate(self.unidad_procesamiento.registros.elementos):
                etiqueta = "| " + str(value) + " -> " + str(self.unidad_procesamiento.registros.elementos[value]) + " |"
                pos_x = width - len(etiqueta) - 17
                stdscr.addstr(idx + 2, pos_x, etiqueta)  
        else:
            stdscr.addstr(1, 0, "No hay suficiente espacio para mostrar los registros.") 

    def mostrar_datos(self, stdscr, width):
        num_datos = len(self.unidad_procesamiento.memoria_datos.elementos)
        if num_datos + 1 < stdscr.getmaxyx()[0]:  
            pos_x = width - 35
            stdscr.addstr(10 + len(self.unidad_procesamiento.registros.elementos),pos_x, "***Memoria de Datos***")
            for idx, value in enumerate(self.unidad_procesamiento.memoria_datos.elementos):
                etiqueta = "| " + str(value) + " -> " + str(self.unidad_procesamiento.memoria_datos.elementos[value]) + " |"
                pos_x = width - len(etiqueta) - 1
                stdscr.addstr(idx + 11 + len(self.unidad_procesamiento.registros.elementos), pos_x, etiqueta)  
        else:
            stdscr.addstr(1, 0, "No hay suficiente espacio para mostrar los registros.")            

    def mostrar_segmentacion(self, stdscr):
        stdscr.addstr(2, 65, "PC = " + str(self.segmentacion.unidad_procesamiento.pc.valor))
        stdscr.addstr(2, 80, "Ciclo de reloj= " + str(self.ciclo))
        self.mostrar_registros_acoplamiento(stdscr)

    def mostrar_registros_acoplamiento(self, stdscr):
        registros_acoplamiento = {
        0: (self.segmentacion.if_id, "if_id"),
        1: (self.segmentacion.id_ex, "id_ex"),
        2: (self.segmentacion.ex_mem, "ex_mem"),
        3: (self.segmentacion.mem_wb, "mem_wb")
        }
        stdscr.addstr(4,8, "***Registros Acoplamiento***")
        for i in range(4):
            registro_acoplamiento, nombre_registro = registros_acoplamiento[i]
            stdscr.addstr(i + 5,2, self.segmentacion.devolver_registro_acoplamiento_string(registro_acoplamiento, nombre_registro))
    
    def mostrar_instrucciones(self,stdscr):
        instrucciones = self.unidad_procesamiento.memoria_instrucciones.devolver_instrucciones()
        i = 0
        stdscr.addstr(12,2, "***Memoria Instrucciones***")
        for instruccion in instrucciones:
            stdscr.addstr(i + 13,6, instruccion)
            i+=1

    def navegar_menu(self, key, seleccion, num_opciones):
        if key == curses.KEY_LEFT and seleccion > 0:
            seleccion -= 1 
        elif key == curses.KEY_RIGHT and seleccion < num_opciones - 1:
            seleccion += 1 
        return seleccion

    def procesar_seleccion(self, stdscr, seleccion):
        if(seleccion == "Avanzar Todo"):
            self.ciclo += self.segmentacion.empezar_segmentacion(False)
        elif(seleccion == "Avanzar un paso"):
            self.ciclo += self.segmentacion.empezar_segmentacion(True)
        stdscr.refresh()
