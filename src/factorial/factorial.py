#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def calcular_factorial(n):
    """Calcula el factorial de un número entero."""
    if n < 0: return 0
    if n == 0 or n == 1: return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def procesar_rango(entrada):
    """Analiza la entrada (ej: '10', '4-8', '-10', '55-') y devuelve el rango."""
    desde, hasta = 1, 1
    
    if "-" in entrada:
        partes = entrada.split("-")
        # Caso "-hasta" (ej: -10)
        if partes[0] == "":
            desde = 1
            hasta = int(partes[1])
        # Caso "desde-" (ej: 55-)
        elif partes[1] == "":
            desde = int(partes[0])
            hasta = 60
        # Caso "desde-hasta" (ej: 4-8)
        else:
            desde = int(partes[0])
            hasta = int(partes[1])
    else:
        # Caso número único
        desde = hasta = int(entrada)
        
    return desde, hasta

# --- Lógica Principal ---

# 1. Verificar si hay argumento, si no, solicitarlo
if len(sys.argv) < 2:
    entrada_usuario = input("Por favor, ingrese un número o rango (ej: 10, 4-8, -10, 50-): ")
else:
    entrada_usuario = sys.argv[1]

try:
    inicio, fin = procesar_rango(entrada_usuario)
    
    # Validar que el rango sea lógico
    if inicio > fin:
        print("Error: El inicio del rango no puede ser mayor al fin.")
    else:
        # 2. Calcular y mostrar resultados
        for num in range(inicio, fin + 1):
            print(f"Factorial de {num} es: {calcular_factorial(num)}")

except ValueError:
    print("Error: Ingrese números válidos.")