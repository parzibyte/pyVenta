from msvcrt import getch
from teclas import teclas
from os import system
from base_de_datos import base_de_datos
from colores import colores
class interfaz_inventario:

	def __init__(self):
		self.ayudante_base_de_datos = base_de_datos()
		self.refrescar_datos()
		self.SALIR = 0
		self.ELIMINAR = 1
		self.NUEVO = 2

	def refrescar_datos(self):
		self.indice_del_elemento_actualmente_seleccionado = 0
		self.productos = self.ayudante_base_de_datos.todos("productos")
		self.numero_de_elementos_de_la_tabla = len(self.productos)

	def agregar_nuevo_producto(self):
		while True:
			self.limpiar_pantalla()
			datos_nuevo_producto = []
			datos_nuevo_producto.append( input("Código de barras:\n\t") )
			datos_nuevo_producto.append( input("Descripción:\n\t") )
			datos_nuevo_producto.append( float(input("Existencia:\n\t")) )
			datos_nuevo_producto.append( float(input("Precio de compra:\n\t$")) )
			datos_nuevo_producto.append( float(input("Precio de venta:\n\t$")) )
			self.ayudante_base_de_datos.nuevo("productos", datos_nuevo_producto)
			print("Presione ENTER para agregar otro\nPresione ESC para volver al menú")
			tecla_presionada = ord(getch())
			if tecla_presionada == teclas.ESC:
				break
		self.refrescar_datos()


	def eliminar_producto_pidiendo_confirmacion(self):
		producto_seleccionado = self.productos[self.indice_del_elemento_actualmente_seleccionado]
		print("¿Realmente deseas eliminar {:s} con el código {:s}?".format(producto_seleccionado[1],producto_seleccionado[0]))
		print("\tENTER: Confirmar\tESC: Cancelar")
		teclaConfirmacion = ord(getch())
		if teclaConfirmacion == teclas.ENTER:
			self.ayudante_base_de_datos.eliminar("productos", "rowid", producto_seleccionado[5])
			self.refrescar_datos()


	def confirmacion(self, mensaje):
		print(mensaje + "\n")
		teclaConfirmacion = ord(getch())
		return teclaConfirmacion == teclas.ENTER

	def imprimir_opciones(self):
		print("ESC: Volver al menú\tF1: Nuevo\tF2: Eliminar seleccionado")


	def navegar_por_la_tabla(self, tecla_presionada):
		if tecla_presionada == teclas.ALGUNA_TECLA_QUE_NO_ES_CARACTER:
			tecla_presionada = ord(getch())
			if tecla_presionada == teclas.FLECHA_ARRIBA:
				if self.indice_del_elemento_actualmente_seleccionado <= 0:
					self.indice_del_elemento_actualmente_seleccionado = self.numero_de_elementos_de_la_tabla - 1
				else:
					self.indice_del_elemento_actualmente_seleccionado -= 1
			if tecla_presionada == teclas.FLECHA_ABAJO:
				if self.indice_del_elemento_actualmente_seleccionado >= self.numero_de_elementos_de_la_tabla - 1:
					self.indice_del_elemento_actualmente_seleccionado = 0
				else:
					self.indice_del_elemento_actualmente_seleccionado += 1
			#if tecla_presionada == teclas.FLECHA_DERECHA:
				#Código por aquí
			#if tecla_presionada == teclas.FLECHA_IZQUIERDA:
				#Código por aquí
				

	def limpiar_pantalla(self):
		system('cls')


	def imprimir_productos(self):
		self.limpiar_pantalla()
		# Imprimimos el encabezado...
		print("+{:-<20}+{:-<30}+{:-<15}+{:-<17}+{:-<17}+".format("", "", "", "", ""))
		print("|{:<20}|{:<30}|{:<15}|{:<17}|{:<17}|".format("  Código", "  Descripción", "  Existencia", "  P. compra", "  P.venta"))
		print("+{:-<20}+{:-<30}+{:-<15}+{:-<17}+{:-<17}+".format("", "", "", "", ""))
		
		# Imprimimos los valores...
		contador = 0
		for codigo, descripcion, existencia, precio_compra, precio_venta, rowid in self.productos:
			if contador == self.indice_del_elemento_actualmente_seleccionado:
				# Imprimimos una flecha para que el usuario sepa en dónde está
				print(colores.AZUL + "|{: <20}|{:<30}|{:<15}|$ {:<15}|$ {:<15}|<==".format(codigo, descripcion, existencia, precio_compra, precio_venta) + colores.FINAL)
			else:
				print("|{:<20}|{:<30}|{:<15}|$ {:<15}|$ {:<15}|".format(codigo, descripcion, existencia, precio_compra, precio_venta))
			contador += 1

		# Imprimimos el pie de la tabla
		print("+{:-<20}+{:-<30}+{:-<15}+{:-<17}+{:-<17}+".format("", "", "", "", ""))

	def mostrar(self):
		while True:
			self.imprimir_productos()
			self.imprimir_opciones()
			tecla_presionada = ord(getch())
			self.navegar_por_la_tabla(tecla_presionada)
			eleccion = self.esperar_que_el_usuario_elija(tecla_presionada)
			if eleccion == self.SALIR:
				break
			elif eleccion == self.ELIMINAR:
				self.eliminar_producto_pidiendo_confirmacion()
			elif eleccion == self.NUEVO:
				self.agregar_nuevo_producto()


	def esperar_que_el_usuario_elija(self, tecla_presionada):
		if tecla_presionada == teclas.ESC:
			return self.SALIR
		elif tecla_presionada == teclas.ALGUNA_TECLA_DE_FUNCION:
			tecla_presionada = ord(getch())
			if tecla_presionada == teclas.F1:
				return self.NUEVO
			if tecla_presionada == teclas.F2:
				return self.ELIMINAR
		return -1
