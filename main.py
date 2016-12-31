from Encabezado import Menu
from Interfaces import Inventario, Vender
opciones = ["Inventario de productos", "Vender", "Salir"]
mi_menu = Menu(opciones)
while True:
	opcionSeleccionada = mi_menu.esperarOpcionSeleccionada()
	if opcionSeleccionada == 0:
		Inventario().mostrar()
	if opcionSeleccionada == 1:
		Vender().mostrar()
	elif opcionSeleccionada == len(opciones) - 1:
		exit()