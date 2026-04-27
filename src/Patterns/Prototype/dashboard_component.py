import copy
from abc import ABC, abstractmethod

# 1. La interfaz Prototipo
class Prototipo(ABC):
    @abstractmethod
    def clonar(self):
        """Método que las clases hijas deben implementar para clonarse."""
        pass

# 2. El Prototipo Concreto
class ComponenteDashboard(Prototipo):
    def __init__(self, nombre: str, color_fondo: str, color_texto: str):
        self.nombre = nombre
        self.color_fondo = color_fondo
        self.color_texto = color_texto

    def clonar(self):
        # copy.deepcopy genera una copia idéntica pero totalmente independiente en la memoria
        return copy.deepcopy(self)

    def __str__(self):
        return f"Componente: '{self.nombre}' | Colores: {self.color_fondo} y {self.color_texto}"