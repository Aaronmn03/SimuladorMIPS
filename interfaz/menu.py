import curses

class Menu:
    def __init__(self, unidad_procesamiento, segmentacion):
        
        self.unidad_procesamiento = unidad_procesamiento
        self.segmentacion = segmentacion    #quiero que muestre de alguna forma como va la segmentacion.
        curses.wrapper(self.inicializar_menu)

    def inicializar_menu(self, stdscr):
        curses.curs_set(0)  # Ocultar el cursor
        stdscr.clear()
        stdscr.refresh()

        height, width = stdscr.getmaxyx()
        menu = ["Avanzar un paso", "Avanzar Todo", "Salir"]
        seleccion = 0

        while True:
            stdscr.clear()
            self.mostrar_menu(stdscr, menu, seleccion)
            self.mostrar_registros(stdscr, width)
            self.mostrar_segmentacion(stdscr)
            stdscr.refresh()

            key = stdscr.getch()
            seleccion = self.navegar_menu(key, seleccion, len(menu))

            if key in [curses.KEY_ENTER, 10, 13]:  # Si se presiona "Enter"
                if seleccion == len(menu) - 1:
                    break  # Salir del programa
                else:
                    self.mostrar_seleccion(stdscr, menu[seleccion])

    def mostrar_menu(self, stdscr, menu, seleccion):
        """Imprime el menú en la consola."""
        for idx, opcion in enumerate(menu):
            if idx == seleccion:
                stdscr.addstr(0, idx * 20, f"> {opcion}", curses.A_REVERSE)
            else:
                stdscr.addstr(0, idx * 20, f"  {opcion}")

    def mostrar_registros(self, stdscr, width):
        num_registros = len(self.unidad_procesamiento.registros.elementos)
        # Asegúrate de que hay espacio suficiente en la ventana
        if num_registros + 1 < stdscr.getmaxyx()[0]:  # +1 para la línea del menú
            for idx, value in enumerate(self.unidad_procesamiento.registros.elementos):
                etiqueta = "| " + str(value) + " -> " + str(self.unidad_procesamiento.registros.elementos[value]) + " |"
                pos_x = width - len(etiqueta) - 1
                stdscr.addstr(idx + 1, pos_x, etiqueta)  # Ajustar la posición para que no se superponga con el menú
        else:
            stdscr.addstr(1, 0, "No hay suficiente espacio para mostrar los registros.")

    def mostrar_registros(self, stdscr, width):
        num_registros = len(self.unidad_procesamiento.registros.elementos)
        # Asegúrate de que hay espacio suficiente en la ventana
        if num_registros + 1 < stdscr.getmaxyx()[0]:  # +1 para la línea del menú
            for idx, value in enumerate(self.unidad_procesamiento.registros.elementos):
                etiqueta = "| " + str(value) + " -> " + str(self.unidad_procesamiento.registros.elementos[value]) + " |"
                pos_x = width - len(etiqueta) - 1
                stdscr.addstr(idx + 1, pos_x, etiqueta)  # Ajustar la posición para que no se superponga con el menú
        else:
            stdscr.addstr(1, 0, "No hay suficiente espacio para mostrar los registros.")
            

    def mostrar_segmentacion(self, stdscr):
        stdscr.addstr(3, 20, "PC = " + str(self.segmentacion.unidad_procesamiento.pc.valor))


    def navegar_menu(self, key, seleccion, num_opciones):
        """Navega por el menú y devuelve la nueva selección."""
        if key == curses.KEY_LEFT and seleccion > 0:
            seleccion -= 1 
        elif key == curses.KEY_RIGHT and seleccion < num_opciones - 1:
            seleccion += 1 
        return seleccion

    def mostrar_seleccion(self, stdscr, seleccion):
        """Muestra la opción seleccionada."""
        stdscr.addstr(2, 0, f"Has seleccionado {seleccion}")
        stdscr.refresh()
        stdscr.getch()  # Esperar a que el usuario presione una tecla
