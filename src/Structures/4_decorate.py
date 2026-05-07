# --- Componente Base ---
class NumeroBase:
    def get_valor(self):
        pass

# --- Componente Concreto ---
class Numero(NumeroBase):
    def __init__(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor

# --- Decorador Base ---
class DecoradorOperacion(NumeroBase):
    def __init__(self, numero: NumeroBase):
        self.numero = numero

    def get_valor(self):
        return self.numero.get_valor()

# --- Decoradores Concretos ---
class SumarDos(DecoradorOperacion):
    def get_valor(self):
        return self.numero.get_valor() + 2 # a. Sumarle 2. [cite: 18]

class MultiplicarPorDos(DecoradorOperacion):
    def get_valor(self):
        return self.numero.get_valor() * 2 # b. Multiplicarle por 2. [cite: 19]

class DividirPorTres(DecoradorOperacion):
    def get_valor(self):
        return self.numero.get_valor() / 3 # c. Dividirlo por 3. [cite: 20]

# --- Prueba de la implementación ---
# Implemente una clase que permita a un número cualquiera imprimir su valor [cite: 17]
numero_inicial = Numero(10)
print(f"Valor sin agregados: {numero_inicial.get_valor()}") # Mostrar los resultados de la clase sin agregados [cite: 21]

# Invocación anidada a las clases con las diferentes operaciones [cite: 21]
# Equivalente a: ((10 + 2) * 2) / 3
numero_decorado = DividirPorTres(
                    MultiplicarPorDos(
                        SumarDos(numero_inicial)
                    )
                  )

print(f"Valor con operaciones anidadas ((10 + 2) * 2) / 3: {numero_decorado.get_valor()}")