import sqlite3
class base_de_datos:
	def __init__(self):
		self.nombre_base_de_datos = "pyVenta.db"
		self.conexion = sqlite3.connect(self.nombre_base_de_datos)
		self.cursor = self.conexion.cursor()
		self.crear_tablas()

	def crear_tablas(self):
		tablas = [
			"""
			CREATE TABLE IF NOT EXISTS `productos`
			(
				codigo TEXT,
				descripcion TEXT,
				existencia REAL,
				precio_de_compra REAL,
				precio_de_venta REAL
			);
			"""
		]
		for tabla in tablas:
			self.cursor.execute(tabla)

	def guardar_cambios(self):
		self.conexion.commit()

	def nuevo(self, nombre_tabla, valores):
		oracion = "INSERT INTO `{:s}` VALUES ({:s});".format( nombre_tabla, "?," * ( len( valores ) - 1) + "?")
		self.cursor.execute(oracion, valores)
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