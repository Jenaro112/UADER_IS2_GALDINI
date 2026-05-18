#*------------------------------------------------------------------------
#* Ingeniería de Software II
#* Patrones de Comportamiento - Observer
#* TP5 - Ejercicio 3
#* UADER - Ingeniería de Software II
#* Dr. Pedro E. Colla
#*------------------------------------------------------------------------
"""
Observer donde una serie de clases están subscriptas. Cada clase espera que
su propio ID (una secuencia arbitraria de 4 caracteres) sea expuesta y emitirá
un mensaje cuando el ID emitido y el propio coinciden. Se implementan 4 clases
con IDs específicos. Se emiten 8 IDs asegurando que al menos cuatro coincidan.
"""


class Observador:
    def __init__(self, id_):
        self._id = id_

    def actualizar(self, id_emitido):
        if self._id == id_emitido:
            print(f"  Observador [{self._id}] -> ID recibido coincide!")
            return True
        return False


class Sujeto:
    def __init__(self):
        self._observadores = []

    def suscribir(self, observador):
        self._observadores.append(observador)

    def emitir(self, id_):
        print(f"\nEmitiendo ID: '{id_}'")
        alguno_coincidio = False
        for obs in self._observadores:
            if obs.actualizar(id_):
                alguno_coincidio = True
        if not alguno_coincidio:
            print(f"  -> Ningún observador coincide con '{id_}'")


def main():
    sujeto = Sujeto()

    obs_a = Observador("ABCD")
    obs_b = Observador("EFGH")
    obs_c = Observador("IJKL")
    obs_d = Observador("MNOP")

    sujeto.suscribir(obs_a)
    sujeto.suscribir(obs_b)
    sujeto.suscribir(obs_c)
    sujeto.suscribir(obs_d)

    ids_a_emitir = ["ABCD", "WXYZ", "EFGH", "1234", "IJKL", "5678", "MNOP", "90AB"]
    for id_ in ids_a_emitir:
        sujeto.emitir(id_)


if __name__ == "__main__":
    main()
