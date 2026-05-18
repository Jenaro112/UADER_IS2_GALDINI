#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Comportamiento - Chain of Responsibility
#* TP5 - Ejercicio 1
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Cadena de responsabilidad donde los números del 1 al 100 son pasados
a las clases subscriptas en secuencia. Una clase consume números primos,
otra consume números pares. Si ningún consumidor lo procesa, se marca
como no consumido.
"""

class Manejador:
    def __init__(self):
        self._siguiente = None

    def set_siguiente(self, manejador):
        self._siguiente = manejador
        return manejador

    def manejar(self, numero):
        if self._siguiente:
            return self._siguiente.manejar(numero)
        return False


class ManejadorPrimos(Manejador):
    def manejar(self, numero):
        if self.es_primo(numero):
            print(f"  ManejadorPrimos consumió {numero}")
            return True
        return super().manejar(numero)

    @staticmethod
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


class ManejadorPares(Manejador):
    def manejar(self, numero):
        if numero % 2 == 0:
            print(f"  ManejadorPares consumió {numero}")
            return True
        return super().manejar(numero)


def main():
    cadena = Manejador()
    cadena.set_siguiente(ManejadorPrimos()).set_siguiente(ManejadorPares())

    for numero in range(1, 101):
        print(f"Número {numero}:")
        if not cadena.manejar(numero):
            print(f"  -> No consumido")


if __name__ == "__main__":
    main()
