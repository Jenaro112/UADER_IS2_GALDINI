#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Comportamiento - Memento
#* TP5 - Ejercicio 5
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Modifique el programa IS2_taller_memory.py para que la clase tenga la
capacidad de almacenar hasta 4 estados en el pasado y pueda recuperar
los mismos en cualquier orden de ser necesario. El método undo deberá
tener un argumento adicional indicando si se desea recuperar el inmediato
anterior (0) y los anteriores a el (1,2,3).
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Memento:
    estado: str
    fecha: datetime


class Originador:
    def __init__(self):
        self._estado = ""

    def establecer(self, estado):
        self._estado = estado

    def guardar_estado(self):
        return Memento(estado=self._estado, fecha=datetime.now())

    def restaurar(self, memento):
        self._estado = memento.estado
        print(f"  Restaurado: '{self._estado}' (guardado {memento.fecha})")

    def mostrar(self):
        print(f"  Estado actual: '{self._estado}'")


class Caretaker:
    def __init__(self):
        self._historial = []

    def guardar(self, originador):
        if len(self._historial) >= 4:
            self._historial.pop(0)
        self._historial.append(originador.guardar_estado())

    def undo(self, originador, posicion=0):
        if not self._historial:
            print("  No hay estados guardados.")
            return
        if posicion < 0 or posicion >= len(self._historial):
            print(f"  Posición {posicion} fuera de rango (0-{len(self._historial)-1})")
            return
        indice = len(self._historial) - 1 - posicion
        originador.restaurar(self._historial[indice])


def main():
    originador = Originador()
    caretaker = Caretaker()

    originador.establecer("Config A")
    caretaker.guardar(originador)
    print("  Guardado: 'Config A'")

    originador.establecer("Config B")
    caretaker.guardar(originador)
    print("  Guardado: 'Config B'")

    originador.establecer("Config C")
    caretaker.guardar(originador)
    print("  Guardado: 'Config C'")

    originador.establecer("Config D")
    caretaker.guardar(originador)
    print("  Guardado: 'Config D'")

    print("\n--- Deshaciendo estados ---")
    print("\nundo(posicion=0) -> inmediato anterior:")
    caretaker.undo(originador, 0)
    originador.mostrar()

    print("\nundo(posicion=1) -> un estado más atrás:")
    caretaker.undo(originador, 1)
    originador.mostrar()

    print("\nundo(posicion=2) -> dos estados más atrás:")
    caretaker.undo(originador, 2)
    originador.mostrar()

    print("\nundo(posicion=3) -> tres estados más atrás:")
    caretaker.undo(originador, 3)
    originador.mostrar()


if __name__ == "__main__":
    main()
