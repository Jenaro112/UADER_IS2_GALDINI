import sys
# Intentamos importar matplotlib, si no está instalado, informamos al usuario.
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Error: El paquete 'matplotlib' no está instalado.")
    print("Por favor, ejecute: pip install matplotlib")
    sys.exit(1)

def calcular_conjetura_collatz(n):
    """
    Implementa la lógica de la conjetura de Collatz:
    - Si n es par, el siguiente es n / 2.
    - Si n es impar, el siguiente es 3n + 1.
    Devuelve el número de iteraciones para llegar a 1.
    """
    if n <= 0: return 0
    iteraciones = 0
    # La secuencia converge al bucle (4, 2, 1) repetitivo.
    # Contamos iteraciones hasta llegar a 1.
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iteraciones += 1
    return iteraciones

# --- Configuración y Cálculos ---
RANGO_MAXIMO = 10000
numeros_inicio = []
lista_iteraciones = []

print(f"Iniciando cálculo de la conjetura de Collatz para n del 1 al {RANGO_MAXIMO}...")

# Calculamos iteraciones para cada número en el rango
for i in range(1, RANGO_MAXIMO + 1):
    numeros_inicio.append(i)
    lista_iteraciones.append(calcular_conjetura_collatz(i))

print("Cálculo finalizado. Generando gráfico...")

# --- Lógica del gráfico con Matplotlib ---
plt.figure(figsize=(10, 6))

# !!! IMPORTANTE: Sigue la consigna específica para los ejes:
# Eje X (Abscisas): Número de iteraciones
# Eje Y (Ordenadas): Número de inicio (n)
# Usamos un gráfico de dispersión (scatter) para visualizar los 10,000 puntos.
plt.scatter(lista_iteraciones, numeros_inicio, s=1, alpha=0.3, color='blue')

# Configuración de etiquetas y títulos
plt.title(f"Conjetura de Collatz ({RANGO_MAXIMO} números)")
plt.xlabel("Iteraciones para converger a 1 (Abscisas)")
plt.ylabel("Número 'n' de comienzo (Ordenadas)")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Guardar el gráfico en un archivo (para que sea más fácil de visualizar)
plt.savefig('grafico_collatz_UADER.png')

# Mostrar el gráfico por pantalla
print("Gráfico generado. Se abrirá una ventana nueva y se guardará como 'grafico_collatz_UADER.png'.")
plt.show()