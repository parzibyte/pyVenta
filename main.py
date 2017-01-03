from interfaz_inventario import interfaz_inventario
from interfaz_vender import interfaz_vender
from interfaz_menu import interfaz_menu
opciones = ["Inventario de productos", "Vender", "Salir"]
mi_menu = interfaz_menu(opciones)
while True:
	opcionSeleccionada = mi_menu.esperarOpcionSeleccionada()
	if opcionSeleccionada == 0:
		interfaz_inventario().mostrar()
	if opcionSeleccionada == 1:
		interfaz_vender().mostrar()
	elif opcionSeleccionada == len(opciones) - 1:
		exit()