import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#* Modificado: almacena hasta 4 estados; undo(posicion) recupera
#* el inmediato anterior (0) o los anteriores (1,2,3)
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		
		self.file = file
		self.content = content


class FileWriterUtility:

	def __init__(self, file):

		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string


	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:


	def __init__(self):
		self.historial = []

	def save(self, writer):
		if len(self.historial) >= 4:
			self.historial.pop(0)
		self.historial.append(writer.save())

	def undo(self, writer, posicion=0):
		if not self.historial:
			print("  No hay estados guardados.")
			return
		if posicion < 0 or posicion >= len(self.historial):
			print("  Posición {} fuera de rango (0-{})".format(posicion, len(self.historial)-1))
			return
		indice = len(self.historial) - 1 - posicion
		writer.undo(self.historial[indice])


if __name__ == '__main__':

	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar");
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional II")
	writer.write("Material adicional de la clase de patrones II\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional III")
	writer.write("Material adicional de la clase de patrones III\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se invoca undo(posicion=0) -> inmediato anterior")
	caretaker.undo(writer, 0)
	print("Estado actual:")
	print(writer.content + "\n\n")

	print("Se invoca undo(posicion=1) -> un estado más atrás")
	caretaker.undo(writer, 1)
	print("Estado actual:")
	print(writer.content + "\n\n")

	print("Se invoca undo(posicion=2) -> dos estados más atrás")
	caretaker.undo(writer, 2)
	print("Estado actual:")
	print(writer.content + "\n\n")

	print("Se invoca undo(posicion=3) -> tres estados más atrás")
	caretaker.undo(writer, 3)
	print("Estado actual:")
	print(writer.content + "\n\n")
