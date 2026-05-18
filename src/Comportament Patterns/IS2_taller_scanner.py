import os
#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#* Modificado: se agregan 4 memorias (M1-M4) que se barren en cada ciclo
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:

	def scan(self):
		
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

	def __init__(self, radio):
		
		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos = 0
		self.name = "AM"

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
"""Separate class for FM state"""
class FmState(State):

	def __init__(self, radio):

		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = 0
		self.name = "FM"

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

#*------- Memoria para almacenar una frecuencia (AM o FM)
class Memoria:
	def __init__(self, etiqueta, banda, frecuencia):
		self.etiqueta = etiqueta
		self.banda = banda
		self.frecuencia = frecuencia

	def sintonizar(self):
		unidad = "MHz" if self.banda == "FM" else "kHz"
		print("  {}: {} {:.1f} {}".format(self.etiqueta, self.banda, self.frecuencia, unidad))

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:


	def __init__(self):
		
		self.fmstate = FmState(self)
		self.amstate = AmState(self)

#*--- Inicialmente en FM

		self.state = self.fmstate

#*--- Memorias M1 a M4 (cada una puede ser AM o FM)
		self.memorias = [
			Memoria("M1", "FM", 99.5),
			Memoria("M2", "AM", 710),
			Memoria("M3", "FM", 102.3),
			Memoria("M4", "AM", 830),
		]

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		self.state.scan()

	def barrer_memorias(self):
		print("--- Barriendo memorias ---")
		for m in self.memorias:
			m.sintonizar()

#*---------------------

if __name__ == "__main__":
	os.system("clear")
	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()
	actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
	actions *= 2

#*---- Recorre las acciones ejecutando la acción

	print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
	for action in actions:
		action()

#*---- Al final de cada ciclo de barrido, barrer las 4 memorias
	print("\n--- Ciclo de barrido de memorias ---")
	radio.barrer_memorias()
