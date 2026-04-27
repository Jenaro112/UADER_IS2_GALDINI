from abc import ABC, abstractmethod

# 1. Interfaz base que todas las hamburguesas deben respetar
class Hamburguesa(ABC):
    @abstractmethod
    def entregar(self):
        pass

# 2. Clases Concretas (Los diferentes tipos de entrega)
class HamburguesaMostrador(Hamburguesa):
    def entregar(self):
        print("-    Entregando hamburguesa en el mostrador.")

class HamburguesaRetiro(Hamburguesa):
    def entregar(self):
        print("-    Hamburguesa lista en empaque para ser retirada por el cliente.")

class HamburguesaDelivery(Hamburguesa):
    def entregar(self):
        print("-    Enviando hamburguesa por delivery a la dirección indicada.")

# 3. La Fábrica (Factory) que se encarga de instanciarlas
class HamburguesaFactory:
    @staticmethod
    def crear_hamburguesa(tipo_entrega: str) -> Hamburguesa:
        tipo = tipo_entrega.lower()
        
        if tipo == "mostrador":
            return HamburguesaMostrador()
        elif tipo == "retiro":
            return HamburguesaRetiro()
        elif tipo == "delivery":
            return HamburguesaDelivery()
        else:
            raise ValueError(f"El tipo de entrega '{tipo_entrega}' no es válido.")