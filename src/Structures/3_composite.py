# --- Componente Base ---
class Componente:
    def mostrar(self, nivel=0):
        pass

# --- Hoja (Pieza individual) ---
class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Pieza: {self.nombre}")

# --- Compuesto (Sub-conjuntos / Producto Principal) ---
class SubConjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente: Componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"[{self.nombre}]")
        for comp in self.componentes:
            comp.mostrar(nivel + 1)

# --- Prueba de la implementación ---
# Producto principal [cite: 14]
producto_principal = SubConjunto("Producto Principal")

# Formado por tres sub-conjuntos los que a su vez tendrán cuatro piezas cada uno [cite: 14]
for i in range(1, 4):
    sub = SubConjunto(f"Sub-conjunto {i}")
    for j in range(1, 5):
        sub.agregar(Pieza(f"Pieza {i}.{j}"))
    producto_principal.agregar(sub)

# Agregar un sub-conjunto opcional adicional también formado por cuatro piezas [cite: 15]
sub_opcional = SubConjunto("Sub-conjunto Opcional")
for j in range(1, 5):
    sub_opcional.agregar(Pieza(f"Pieza Op.{j}"))
producto_principal.agregar(sub_opcional)

# Mostrar la configuración [cite: 15]
print("Configuración del Ensamblado:")
producto_principal.mostrar()