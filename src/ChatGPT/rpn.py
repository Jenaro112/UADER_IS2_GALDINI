"""Módulo de Calculadora RPN (Reverse Polish Notation) con operaciones avanzadas."""

# =====================================================================
# NOTAS DE IMPLEMENTACIÓN DE LA CALCULADORA RPN
# =====================================================================
# La Notación Polaca Inversa (RPN) es un método algebraico de entrada
# de datos en el que los operadores siguen a sus operandos.
#
# Ventajas principales de esta arquitectura:
# 1. No requiere el uso de paréntesis para definir la precedencia.
# 2. Es extremadamente eficiente para la evaluación mediante una Pila (Stack).
#
# Funcionamiento del algoritmo en este programa:
# - Leemos la expresión como una cadena de texto y la separamos por espacios.
# - Si el elemento (token) es un número, lo apilamos (Push).
# - Si el elemento es un operador (+, -, *, /) o función:
#     a. Desapilamos (Pop) la cantidad de números necesarios.
#     b. Realizamos el cálculo correspondiente.
#     c. Apilamos el resultado de vuelta.
# - Al terminar de leer toda la expresión, la pila debe contener
#   exactamente un número, que es el resultado final.
# =====================================================================

import math
import sys


class RPNError(Exception):
    """Excepción personalizada para un manejo de errores claro."""


class RPNCalculator:
    """Clase principal que maneja la lógica de la pila y las memorias."""

    def __init__(self):
        self.stack = []
        self.memory = {f"{i:02d}": 0.0 for i in range(10)}

    def pop_n(self, n):
        """Extrae múltiples valores de la pila asegurando que haya suficientes elementos."""
        if len(self.stack) < n:
            raise RPNError("Error: pila insuficiente para operar")

        if n == 1:
            return self.stack.pop()

        res = self.stack[-n:]
        self.stack = self.stack[:-n]
        return res

    def push(self, val):
        """Convierte e inserta un valor en la parte superior de la pila."""
        self.stack.append(float(val))

    def evaluate(self, expression):
        """Itera sobre los tokens de la expresión RPN y ejecuta las operaciones matemáticas."""
        tokens = expression.split()

        for token in tokens:
            token = token.upper()

            try:
                self.push(float(token))
                continue
            except ValueError:
                pass

            if token == "+":
                a, b = self.pop_n(2)
                self.push(a + b)
            elif token == "-":
                a, b = self.pop_n(2)
                self.push(a - b)
            elif token == "*":
                a, b = self.pop_n(2)
                self.push(a * b)
            elif token == "/":
                a, b = self.pop_n(2)
                if b == 0:
                    raise RPNError("Error: división por cero")
                self.push(a / b)

            elif token == "DUP":
                a = self.pop_n(1)
                self.push(a)
                self.push(a)
            elif token == "SWAP":
                a, b = self.pop_n(2)
                self.push(b)
                self.push(a)
            elif token == "DROP":
                self.pop_n(1)
            elif token == "CLEAR":
                self.stack.clear()

            elif token == "PI":
                self.push(math.pi)
            elif token in ("E", "PHI"):
                if token == "E":
                    self.push(math.e)
                if token == "PHI":
                    self.push((1 + math.sqrt(5)) / 2)

            elif token == "SQRT":
                self.push(math.sqrt(self.pop_n(1)))
            elif token == "LOG":
                self.push(math.log10(self.pop_n(1)))
            elif token == "LN":
                self.push(math.log(self.pop_n(1)))
            elif token == "E^X":
                self.push(math.exp(self.pop_n(1)))
            elif token == "10^X":
                self.push(math.pow(10, self.pop_n(1)))
            elif token == "Y^X":
                y, x = self.pop_n(2)
                self.push(math.pow(y, x))
            elif token == "1/X":
                a = self.pop_n(1)
                if a == 0:
                    raise RPNError("Error: división por cero")
                self.push(1 / a)
            elif token == "CHS":
                self.push(-self.pop_n(1))

            elif token == "SIN":
                self.push(math.sin(math.radians(self.pop_n(1))))
            elif token == "COS":
                self.push(math.cos(math.radians(self.pop_n(1))))
            elif token == "TG":
                self.push(math.tan(math.radians(self.pop_n(1))))
            elif token == "ASIN":
                self.push(math.degrees(math.asin(self.pop_n(1))))
            elif token == "ACOS":
                self.push(math.degrees(math.acos(self.pop_n(1))))
            elif token == "ATG":
                self.push(math.degrees(math.atan(self.pop_n(1))))

            elif token.startswith("STO"):
                mem_idx = token[3:]
                if mem_idx in self.memory:
                    self.memory[mem_idx] = self.pop_n(1)
                else:
                    raise RPNError("Error: memoria inválida")
            elif token.startswith("RCL"):
                mem_idx = token[3:]
                if mem_idx in self.memory:
                    self.push(self.memory[mem_idx])
                else:
                    raise RPNError("Error: memoria inválida")
            else:
                raise RPNError(f"Error: token inválido '{token}'")

        if len(self.stack) != 1:
            raise RPNError("Error: al final debe quedar exactamente 1 valor en la pila")

        return self.stack.pop()

# =====================================================================
# MANEJO DE MEMORIA Y ESTADO DEL PROGRAMA
# =====================================================================
# El diccionario 'memory' emula los registros de almacenamiento
# de las calculadoras científicas clásicas (como las HP).
# Posee 10 espacios indexados del 00 al 09.
# - STO (Store): Guarda el valor actual de la pila en el registro.
# - RCL (Recall): Recupera el valor del registro y lo pone en la pila.
# Todo acceso a un índice no inicializado o fuera de rango (ej. 15)
# dispara una excepción RPNError para evitar caídas del sistema.
# =====================================================================

# =====================================================================
# PUNTO DE ENTRADA Y FLUJO DE EJECUCIÓN (CLI)
# =====================================================================
# La función main() provee una Interfaz de Línea de Comandos (CLI).
# Permite dos modalidades de uso:
# 1. Pasando la expresión como argumentos al llamar al script
#    desde la terminal (ej: python rpn.py 3 4 +).
# 2. Modo interactivo: Si no hay argumentos, el programa
#    solicita al usuario la expresión mediante input().
# Los errores son capturados por el bloque try/except,
# asegurando una salida elegante sin mostrar tracebacks al usuario.
# =====================================================================
def main():
    """Punto de entrada principal para recibir argumentos o pedir input por consola."""
    calc = RPNCalculator()
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
    else:
        expr = input("Ingrese expresión RPN: ")

    try:
        resultado = calc.evaluate(expr)
        print(f"Resultado: {resultado}")
    except RPNError as e:
        print(e)


if __name__ == "__main__":
    main()
