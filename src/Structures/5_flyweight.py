# 1. Flyweight (El objeto compartido)
class CaracterFlyweight:
    """
    Guarda el ESTADO INTRÍNSECO. 
    Esta información es inmutable y se comparte entre muchos contextos.
    """
    def __init__(self, simbolo, fuente, tamano):
        self.simbolo = simbolo
        self.fuente = fuente
        self.tamano = tamano

    def dibujar(self, x, y):
        """
        Recibe el ESTADO EXTRÍNSECO (x, y) por parámetro justo cuando lo necesita.
        """
        print(f"Dibujando '{self.simbolo}' (Fuente: {self.fuente} {self.tamano}pt) en la posición X:{x}, Y:{y}")


# 2. Flyweight Factory (La fábrica que gestiona los objetos compartidos)
class FabricaCaracteres:
    """
    Asegura que no creemos la misma letra dos veces.
    """
    _caracteres_compartidos = {}

    @classmethod
    def obtener_caracter(cls, simbolo, fuente, tamano):
        # Creamos una clave única para esta combinación visual
        clave = (simbolo, fuente, tamano)
        
        # Si no existe, la creamos y la guardamos en el diccionario
        if clave not in cls._caracteres_compartidos:
            print(f"[*] Instanciando en memoria nueva letra: '{simbolo}' en {fuente} {tamano}pt")
            cls._caracteres_compartidos[clave] = CaracterFlyweight(simbolo, fuente, tamano)
            
        # Retornamos la instancia compartida
        return cls._caracteres_compartidos[clave]

    @classmethod
    def mostrar_total_instancias(cls):
        print(f"\nTotal de objetos 'Caracter' en memoria: {len(cls._caracteres_compartidos)}")


# 3. Cliente (El Editor de Texto)
class EditorDeTexto:
    """
    Guarda el contexto y el estado extrínseco.
    """
    def __init__(self):
        # Guardaremos tuplas de (referencia_al_flyweight, coordenada_x, coordenada_y)
        self.texto_formateado = []

    def escribir_letra(self, simbolo, fuente, tamano, x, y):
        # Pedimos el caracter a la fábrica en lugar de crear uno nuevo con un 'new'
        caracter = FabricaCaracteres.obtener_caracter(simbolo, fuente, tamano)
        self.texto_formateado.append((caracter, x, y))

    def renderizar_pantalla(self):
        print("\n--- Renderizando Documento ---")
        for caracter, x, y in self.texto_formateado:
            # Le pasamos el estado extrínseco al momento de dibujar
            caracter.dibujar(x, y)


# --- PRUEBA DE LA IMPLEMENTACIÓN ---

editor = EditorDeTexto()

# Simulamos que el usuario escribe la palabra "HOLA" y luego "ALA"
print("--- Escribiendo texto ---")

# Letras H, O, L, A
editor.escribir_letra("H", "Arial", 12, x=10, y=10)
editor.escribir_letra("O", "Arial", 12, x=20, y=10)
editor.escribir_letra("L", "Arial", 12, x=30, y=10)
editor.escribir_letra("A", "Arial", 12, x=40, y=10)

# Espacio
editor.escribir_letra(" ", "Arial", 12, x=50, y=10)

# Letras A, L, A (Aquí es donde se nota el patrón: reutilizará las instancias)
editor.escribir_letra("A", "Arial", 12, x=60, y=10) # Reutiliza la 'A'
editor.escribir_letra("L", "Arial", 12, x=70, y=10) # Reutiliza la 'L'
editor.escribir_letra("A", "Arial", 12, x=80, y=10) # Reutiliza la 'A'

# Mostrar la representación en pantalla
editor.renderizar_pantalla()

# Verificar ahorro de memoria
FabricaCaracteres.mostrar_total_instancias()