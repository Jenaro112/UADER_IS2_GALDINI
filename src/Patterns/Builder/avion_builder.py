from abc import ABC, abstractmethod

# 1. El Producto Final
class Avion:
    def __init__(self):
        self.body = None
        self.turbinas = 0
        self.alas = 0
        self.tren_aterrizaje = None

    def __str__(self):
        return (f"Avión listo: Body '{self.body}', "
                f"{self.turbinas} turbinas, {self.alas} alas y "
                f"tren de aterrizaje '{self.tren_aterrizaje}'.")

# 2. La Interfaz Builder
class AvionBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass
        
    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_turbinas(self):
        pass

    @abstractmethod
    def build_alas(self):
        pass

    @abstractmethod
    def build_tren_aterrizaje(self):
        pass

# 3. El Builder Concreto (implementa los pasos para un avión específico)
class AvionComercialBuilder(AvionBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._avion = Avion()

    def build_body(self):
        self._avion.body = "Fuselaje comercial estándar"

    def build_turbinas(self):
        self._avion.turbinas = 2

    def build_alas(self):
        self._avion.alas = 2

    def build_tren_aterrizaje(self):
        self._avion.tren_aterrizaje = "Retráctil de 3 ejes"

    def get_resultado(self) -> Avion:
        # Guardamos el resultado, reseteamos el builder para el próximo, y lo devolvemos
        resultado = self._avion
        self.reset() 
        return resultado

# 4. El Director (conoce el orden en el que se deben ejecutar los pasos)
class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> AvionBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: AvionBuilder):
        self._builder = builder

    def construir_avion_basico(self):
        """Orquesta los pasos definidos por el taller/consigna"""
        self.builder.build_body()
        self.builder.build_alas()
        self.builder.build_turbinas()
        self.builder.build_tren_aterrizaje()