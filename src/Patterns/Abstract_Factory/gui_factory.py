from abc import ABC, abstractmethod

# ==========================================
# 1. Interfaces de los Productos (La familia)
# ==========================================
class Boton(ABC):
    @abstractmethod
    def renderizar(self):
        pass

class Panel(ABC):
    @abstractmethod
    def renderizar(self):
        pass

# ==========================================
# 2. Productos Concretos (Tema Claro)
# ==========================================
class BotonClaro(Boton):
    def renderizar(self):
        return "Botón Claro [Fondo blanco, texto negro]"

class PanelClaro(Panel):
    def renderizar(self):
        return "Panel Claro [Fondo gris claro, sombras suaves]"

# ==========================================
# 3. Productos Concretos (Tema Oscuro)
# ==========================================
class BotonOscuro(Boton):
    def renderizar(self):
        return "Botón Oscuro [Fondo gris oscuro, texto blanco]"

class PanelOscuro(Panel):
    def renderizar(self):
        return "Panel Oscuro [Fondo negro, sin sombras]"

# ==========================================
# 4. La Interfaz Abstract Factory
# ==========================================
class GUIFactory(ABC):
    @abstractmethod
    def crear_boton(self) -> Boton:
        pass

    @abstractmethod
    def crear_panel(self) -> Panel:
        pass

# ==========================================
# 5. Las Fábricas Concretas
# ==========================================
class TemaClaroFactory(GUIFactory):
    def crear_boton(self) -> Boton:
        return BotonClaro()

    def crear_panel(self) -> Panel:
        return PanelClaro()

class TemaOscuroFactory(GUIFactory):
    def crear_boton(self) -> Boton:
        return BotonOscuro()

    def crear_panel(self) -> Panel:
        return PanelOscuro()