import sqlite3
from msvcrt import getch
from os import system
class BaseDeDatos:
	def __init__(self):
		self.nombre_base_de_datos = "pyVenta.db"
		self.conexion = sqlite3.connect(self.nombre_base_de_datos)
		self.cursor = self.conexion.cursor()

	def guardar_cambios(self):
		self.conexion.commit()

	def nuevo(self, nombre_tabla, valores):
		oracion = "INSERT INTO `{:s}` VALUES ({:s});".format( nombre_tabla, "?," * ( len( valores ) - 1) + "?")
		a = self.cursor.execute(oracion, valores)
		self.guardar_cambios()

	def eliminar(self, nombre_tabla, donde, igual_a):
		oracion = "DELETE FROM `{:s}` WHERE `{:s}` = ?;".format( nombre_tabla, donde)
		self.cursor.execute(oracion, [igual_a])
		self.guardar_cambios();

	def todos(self, nombre_tabla):
		oracion = "SELECT *, rowid FROM `{:s}`;".format( nombre_tabla )
		self.cursor.execute(oracion)
		return self.cursor.fetchall()

	def todos_con_condicion(self, nombre_tabla, donde, igual_a):
		oracion = "SELECT *, rowid FROM `{:s}` WHERE `{:s}` = ?;".format( nombre_tabla, donde)
		self.cursor.execute(oracion, [igual_a])
		return self.cursor.fetchall()
		
class Teclas:
	FLECHA_ABAJO = 80
	FLECHA_ARRIBA = 72
	FLECHA_DERECHA = 77
	FLECHA_IZQUIERDA = 75
	ENTER = 13
	ESC = 27
	ALGUNA_TECLA_QUE_NO_ES_CARACTER = 224
	SUPR = 83
	ALGUNA_TECLA_DE_FUNCION = 0
	F1 = 59
	F2 = 60
	F3 = 61
	F4 = 62

class Colores:
    ENCABEZADO = '\033[95m'
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    PELIGRO = '\033[93m'
    ERROR = '\033[91m'
    FINAL = '\033[0m'
    NEGRITA = '\033[1m'
    SUBRAYADO = '\033[4m'

class Menu:
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
			if tecla == Teclas.ENTER:
				return self.indiceOpcionSeleccionada
			elif tecla == Teclas.ALGUNA_TECLA_QUE_NO_ES_CARACTER:
				tecla = ord(getch())
				if tecla == Teclas.FLECHA_ARRIBA:
					#Tecla de arriba
					if self.indiceOpcionSeleccionada <= 0:
						self.indiceOpcionSeleccionada = self.numeroDeOpciones - 1
					else:
						self.indiceOpcionSeleccionada -= 1
				elif tecla == Teclas.FLECHA_ABAJO:
					#Mover abajo
					if self.indiceOpcionSeleccionada >= self.numeroDeOpciones - 1:
						self.indiceOpcionSeleccionada = 0
					else:
						self.indiceOpcionSeleccionada += 1