#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Comportamiento - Iterator
#* TP5 - Ejercicio 2
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Implemente una clase bajo el patrón iterator que almacene una cadena de
caracteres y permita recorrerla en sentido directo y reverso.
"""

from collections.abc import Iterator


class IteradorCadena:
    def __init__(self, cadena, reverso=False):
        self._cadena = cadena
        self._reverso = reverso
        self._posicion = len(cadena) - 1 if reverso else 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._reverso:
            if self._posicion < 0:
                raise StopIteration
            resultado = self._cadena[self._posicion]
            self._posicion -= 1
            return resultado
        else:
            if self._posicion >= len(self._cadena):
                raise StopIteration
            resultado = self._cadena[self._posicion]
            self._posicion += 1
            return resultado


class Cadena:
    def __init__(self, texto):
        self._texto = texto

    def __iter__(self):
        return IteradorCadena(self._texto)

    def iterar_reverso(self) -> Iterator:
        return IteradorCadena(self._texto, reverso=True)


def main():
    texto = "Hola Mundo"
    cadena = Cadena(texto)

    print(f"Cadena original: '{texto}'")
    print("\nRecorrido directo:")
    for c in cadena:
        print(f"  '{c}'", end=" ")
    print()

    print("\nRecorrido reverso:")
    for c in cadena.iterar_reverso():
        print(f"  '{c}'", end=" ")
    print()


if __name__ == "__main__":
    main()
