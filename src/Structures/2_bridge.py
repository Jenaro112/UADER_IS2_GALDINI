# --- Implementador (Trenes Laminadores) ---
class TrenLaminador:
    def producir(self):
        pass

class TrenLaminador5Mts(TrenLaminador):
    def producir(self):
        return "Generando plancha de 5 mts." # Tren que genera planchas de 5 mts 

class TrenLaminador10Mts(TrenLaminador):
    def producir(self):
        return "Generando plancha de 10 mts." # Tren que genera planchas de 10 mts 

# --- Abstracción (Láminas) ---
class LaminaAcero:
    def __init__(self, tren_laminador: TrenLaminador):
        self.espesor = '0.5"' # Láminas de acero de 0.5" de espesor 
        self.ancho = '1.5 metros' # Y 1,5 metros de ancho 
        self.tren_laminador = tren_laminador

    def fabricar(self):
        print(f"Fabricando lámina (Espesor: {self.espesor}, Ancho: {self.ancho}).")
        print(f"-> Acción: {self.tren_laminador.producir()}")

# --- Prueba de la implementación ---
tren_5 = TrenLaminador5Mts()
tren_10 = TrenLaminador10Mts()

# Clase que represente a las láminas en forma genérica al cual se le pueda indicar el tren 
lamina_a = LaminaAcero(tren_5)
lamina_a.fabricar()

lamina_b = LaminaAcero(tren_10)
lamina_b.fabricar()