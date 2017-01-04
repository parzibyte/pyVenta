from msvcrt import getch
from teclas import teclas
from os import system
from base_de_datos import base_de_datos
from colores import colores

class interfaz_vender:
	def __init__(self):
		self.ayudante_base_de_datos = base_de_datos()
		self.carrito_de_compras = []
		self.refrescar_datos()

	def imprimir_mensaje_codigo_inexistente(self):
		print(colores.ERROR + "EL CÓDIGO NO EXISTE" + colores.FINAL)
		getch()

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


	def imprimir_opciones(self):
		print(
			colores.VERDE + "+" + colores.FINAL +" AUMENTAR CANTIDAD\t" + 
			colores.VERDE + "-" + colores.FINAL +" DISMINUIR CANTIDAD\t" + 
			colores.VERDE + "F1" + colores.FINAL +" BUSCAR\t" + 
			colores.VERDE + "SUPR" + colores.FINAL +" ELIMINAR\t" + 
			colores.VERDE + "ESC" + colores.FINAL +" Cancelar venta"
			)


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
	def refrescar_datos(self):
		self.numero_de_elementos_de_la_tabla = len(self.carrito_de_compras)
		self.indice_del_elemento_actualmente_seleccionado = self.numero_de_elementos_de_la_tabla - 1

	def limpiar_pantalla(self):
			system('cls')
	def quitar_producto(self, indice_del_producto):
		if self.numero_de_elementos_de_la_tabla > 0:
			del self.carrito_de_compras[indice_del_producto]
			self.refrescar_datos()

	def aumentar_cantidad_de_producto(self, indice_del_producto):
		self.carrito_de_compras[indice_del_producto][0] += 1
		self.refrescar_datos()

	def disminuir_cantidad_de_producto(self, indice_del_producto):
		if self.carrito_de_compras[indice_del_producto][0] > 1:
			self.carrito_de_compras[indice_del_producto][0] -= 1
			self.refrescar_datos()

	def agregar_producto_no_existente_al_carrito(self, nuevo_producto):
		producto_convertido = list(nuevo_producto)
		producto_convertido.insert(0,1)
		self.carrito_de_compras.append(producto_convertido)
		self.refrescar_datos()

	def agregar_al_carrito(self, nuevo_producto):
		rowid_nuevo_producto = nuevo_producto[-1]
		for x in range(0, self.numero_de_elementos_de_la_tabla):
			if self.carrito_de_compras[x][-1] == rowid_nuevo_producto:
				self.aumentar_cantidad_de_producto(x)
				return
		self.agregar_producto_no_existente_al_carrito(nuevo_producto)

	def imprimir_carrito_de_compras(self):
		if self.numero_de_elementos_de_la_tabla > 0:
			# Imprimimos el encabezado...
			print("+{:-<10}+{:-<20}+{:-<30}+{:-<15}+{:-<17}+{:-<17}+".format("", "", "", "", "", ""))
			print("|{:<10}|{:<20}|{:<30}|{:<15}|{:<17}|{:<17}|".format("CANT. ", "  Código", "  Descripción", "  Existencia", "  P. compra", "  P.venta"))
			print("+{:-<10}+{:-<20}+{:-<30}+{:-<15}+{:-<17}+{:-<17}+".format("", "", "", "", "", ""))
			
			# Imprimimos los valores...
			contador = 0
			for cantidad, codigo, descripcion, existencia, precio_compra, precio_venta, rowid in self.carrito_de_compras:
				if contador == self.indice_del_elemento_actualmente_seleccionado:
					# Imprimimos una flecha para que el usuario sepa en dónde está
					print(colores.AZUL + "|{:<10}|{: <20}|{:<30}|{:<15}|$ {:<15}|$ {:<15}|<==".format(cantidad, codigo, descripcion, existencia, precio_compra, precio_venta) + colores.FINAL)
				else:
					print("|{:<10}|{:<20}|{:<30}|{:<15}|$ {:<15}|$ {:<15}|".format(cantidad, codigo, descripcion, existencia, precio_compra, precio_venta))
				contador += 1

			# Imprimimos el pie de la tabla
			print("+{:-<10}+{:-<20}+{:-<30}+{:-<15}+{:-<17}+{:-<17}+".format("", "", "", "", "", ""))

	#def esperar_accion_del_usuario(self):

	def mostrar(self):
		codigo_del_producto = ""
		while True:
			self.limpiar_pantalla()
			self.imprimir_opciones()
			self.imprimir_carrito_de_compras()
			print("Escribe el código:")
			print(colores.VERDE + codigo_del_producto + colores.FINAL)
			# Necesitamos saber qué caracter presionaron (por ejemplo la 'a', la 'b' etc)
			caracter_presionado = getch()
			# También queremos el código para saber si presionaron ENTER, ESC u otras teclas
			codigo_del_caracter_presionado = ord(caracter_presionado)

			# Si presionan enter, significa que ya escribieron el código de barras y ahora quieren buscar
			if codigo_del_caracter_presionado == teclas.ENTER:
				if len(codigo_del_producto) > 0:
					coincidencias = self.ayudante_base_de_datos.todos_con_condicion("productos", "codigo", codigo_del_producto)
					codigo_del_producto = ""
					if len(coincidencias) >= 1:
						self.agregar_al_carrito(coincidencias[0])
					else:
						self.imprimir_mensaje_codigo_inexistente()
			elif codigo_del_caracter_presionado == teclas.ESC:
				break
			elif codigo_del_caracter_presionado == teclas.F1:
				print("Buscar...")
			elif codigo_del_caracter_presionado == teclas.RETROCESO:
				codigo_del_producto = codigo_del_producto[:-1]
			elif codigo_del_caracter_presionado == teclas.SUMAR:
				self.aumentar_cantidad_de_producto(self.indice_del_elemento_actualmente_seleccionado)
			elif codigo_del_caracter_presionado == teclas.RESTAR:
				self.disminuir_cantidad_de_producto(self.indice_del_elemento_actualmente_seleccionado)
			elif codigo_del_caracter_presionado == teclas.ALGUNA_TECLA_QUE_NO_ES_CARACTER:
				codigo_tecla = ord(getch())
				if codigo_tecla == teclas.FLECHA_ARRIBA:
					if self.indice_del_elemento_actualmente_seleccionado <= 0:
						self.indice_del_elemento_actualmente_seleccionado = self.numero_de_elementos_de_la_tabla - 1
					else:
						self.indice_del_elemento_actualmente_seleccionado -= 1
				elif codigo_tecla == teclas.FLECHA_ABAJO:
					if self.indice_del_elemento_actualmente_seleccionado >= self.numero_de_elementos_de_la_tabla - 1:
						self.indice_del_elemento_actualmente_seleccionado = 0
					else:
						self.indice_del_elemento_actualmente_seleccionado += 1
				elif codigo_tecla == teclas.SUPR:
					self.quitar_producto(self.indice_del_elemento_actualmente_seleccionado)
			else:
				try:
					codigo_del_producto += caracter_presionado.decode("utf-8")
				except UnicodeDecodeError:
					input("Caracter no permitido!")

			
			