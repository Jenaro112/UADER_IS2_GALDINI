#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Comportamiento - Scanner con Memorias
#* TP5 - Ejercicio 4
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Modifique el programa IS2_taller_scanner.py para que además la secuencia de
barrido de radios que tiene incluya la sintonía de una serie de frecuencias
memorizadas tanto de AM como de FM. Las frecuencias estarán etiquetadas
como M1, M2, M3 y M4. Cada memoria podrá corresponder a una radio de AM
o de FM en sus respectivas frecuencias específicas. En cada ciclo de barrido
se barrerán las cuatro memorias.
"""

class Banda:
    AM = "AM"
    FM = "FM"


class Memoria:
    def __init__(self, etiqueta, banda, frecuencia):
        self.etiqueta = etiqueta
        self.banda = banda
        self.frecuencia = frecuencia

    def sintonizar(self):
        print(f"  {self.etiqueta}: {self.banda} {self.frecuencia:.1f} {'MHz' if self.banda == Banda.FM else 'kHz'}")


class Scanner:
    def __init__(self):
        self._memorias = []

    def agregar_memoria(self, etiqueta, banda, frecuencia):
        self._memorias.append(Memoria(etiqueta, banda, frecuencia))

    def barrer_memorias(self):
        print("\n--- Barrido de memorias ---")
        for memoria in self._memorias:
            memoria.sintonizar()

    def ciclo_barrido(self):
        print("\n========== Ciclo de barrido completo ==========")
        self.barrer_memorias()


def main():
    scanner = Scanner()

    scanner.agregar_memoria("M1", Banda.FM, 99.5)
    scanner.agregar_memoria("M2", Banda.AM, 710)
    scanner.agregar_memoria("M3", Banda.FM, 102.3)
    scanner.agregar_memoria("M4", Banda.AM, 830)

    for _ in range(3):
        scanner.ciclo_barrido()


if __name__ == "__main__":
    main()
