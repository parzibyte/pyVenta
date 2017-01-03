from msvcrt import getch
from teclas import teclas
from os import system
from base_de_datos import base_de_datos
from colores import colores
class interfaz_menu:
	def __init__(self, opciones):
		self.opciones = opciones
		self.numeroDeOpciones = len(self.opciones)
		self.indiceOpcionSeleccionada = 0

	def imprimir(self):
		system('cls')
		print("""
				\t\t\t--BIENVENIDO--\t\t\t
				\t\t\tELIGE UNA OPCIÓN\t\t\t
				""")
		for (indice,opcion) in enumerate(self.opciones):
			if indice == self.indiceOpcionSeleccionada:
				print("\t\t[x]" + opcion)
			else:
				print("\t\t[ ]" + opcion)

	def esperarOpcionSeleccionada(self):
		while True:
			self.imprimir()
			tecla = ord(getch())
			if tecla == teclas.ENTER:
				return self.indiceOpcionSeleccionada
			elif tecla == teclas.ALGUNA_TECLA_QUE_NO_ES_CARACTER:
				tecla = ord(getch())
				if tecla == teclas.FLECHA_ARRIBA:
					#Tecla de arriba
					if self.indiceOpcionSeleccionada <= 0:
						self.indiceOpcionSeleccionada = self.numeroDeOpciones - 1
					else:
						self.indiceOpcionSeleccionada -= 1
				elif tecla == teclas.FLECHA_ABAJO:
					#Mover abajo
					if self.indiceOpcionSeleccionada >= self.numeroDeOpciones - 1:
						self.indiceOpcionSeleccionada = 0
					else:
						self.indiceOpcionSeleccionada += 1			