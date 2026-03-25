import sys

class Factorial:
    def __init__(self):
        """Constructor de la clase Factorial."""
        pass

    def calcular(self, n):
        """Método privado/interno para el cálculo matemático."""
        if n < 0: return 0
        if n == 0 or n == 1: return 1
        res = 1
        for i in range(2, n + 1):
            res *= i
        return res

    def run(self, min_val, max_val):
        """
        Calcula y muestra los factoriales en el rango [min, max].
        Este es el método solicitado por la consigna.
        """
        for num in range(min_val, max_val + 1):
            resultado = self.calcular(num)
            print(f"Factorial de {num} es: {resultado}")

# --- Lógica de ejecución ---
if __name__ == "__main__":
    # Instanciamos la clase
    f_obj = Factorial()
    
    # Manejo de argumentos (reutilizando la lógica anterior)
    if len(sys.argv) < 2:
        entrada = input("Ingrese rango (ej: 4-8): ")
    else:
        entrada = sys.argv[1]

    try:
        # Lógica simple para extraer min y max del string
        if "-" in entrada:
            partes = entrada.split("-")
            p1 = 1 if partes[0] == "" else int(partes[0])
            p2 = 60 if partes[1] == "" else int(partes[1])
        else:
            p1 = p2 = int(entrada)
        
        # Llamada al método solicitado: run(min, max)
        f_obj.run(p1, p2)

    except ValueError:
        print("Error: Ingrese un formato válido.")