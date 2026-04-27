from abc import ABC, abstractmethod

# 1. Interfaz base para todas las facturas
class Factura(ABC):
    def __init__(self, importe: float):
        self.importe = importe

    @abstractmethod
    def generar(self):
        pass

# 2. Clases Concretas (Los distintos tipos de factura)
class FacturaIVAResponsable(Factura):
    def generar(self):
        print(f"Factura Tipo A - Condición: IVA Responsable | Total: ${self.importe:.2f}")

class FacturaIVANoInscripto(Factura):
    def generar(self):
        print(f"Factura Tipo B - Condición: IVA No Inscripto | Total: ${self.importe:.2f}")

class FacturaIVAExento(Factura):
    def generar(self):
        print(f"Factura Tipo C - Condición: IVA Exento | Total: ${self.importe:.2f}")

# 3. La Fábrica (Factory) que evalúa y crea
class FacturaFactory:
    @staticmethod
    def crear_factura(condicion_impositiva: str, importe: float) -> Factura:
        condicion = condicion_impositiva.lower().strip()
        
        if condicion == "responsable":
            return FacturaIVAResponsable(importe)
        elif condicion == "no inscripto":
            return FacturaIVANoInscripto(importe)
        elif condicion == "exento":
            return FacturaIVAExento(importe)
        else:
            raise ValueError(f"La condición impositiva '{condicion_impositiva}' no es válida.")