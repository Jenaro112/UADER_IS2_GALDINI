# pylint: disable=invalid-name
"""
Copyright UADER-FCyT-IS2 ©2024 todos los derechos reservados

getJason_refactor.py - Versión refactorizada con patrón Singleton

Re-factoría sobre getJason.py (TP6) aplicando:
  - Programación orientada a objetos con patrón Singleton
  - Branching by abstraction (coexistencia de vieja y nueva implementación)
  - Manejo robusto de argumentos de línea de comandos
  - Control de errores sin excepciones de sistema

Ejecución:
  python getJason_refactor.py            -> usa clave por defecto "token1"
  python getJason_refactor.py token2      -> usa la clave indicada
  python getJason_refactor.py -v          -> muestra versión
  python getJason_refactor.py --help      -> muestra ayuda
"""

import json
import sys

VERSION = "1.1"


class TokenReader:
    """Abstracción del lector de tokens (Branching by abstraction)."""

    def read_token(self, key):
        """Lee el valor asociado a una clave desde el archivo JSON."""
        raise NotImplementedError("Debe implementarse en subclases")

    def get_keys(self):
        """Devuelve las claves disponibles en el archivo JSON."""
        raise NotImplementedError("Debe implementarse en subclases")


class SingletonTokenReader(TokenReader):
    """Implementación Singleton que extrae tokens de un archivo JSON."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, jsonfile="sitedata.json"):
        if hasattr(self, "_initialized"):
            return
        self._jsonfile = jsonfile
        self._data = None
        self._initialized = True

    def load(self, jsonfile=None):
        """Carga y parsea el archivo JSON.

        Args:
            jsonfile: Ruta al archivo JSON. Si es None, usa la del constructor.
        """
        if jsonfile is not None:
            self._jsonfile = jsonfile
        try:
            with open(self._jsonfile, "r", encoding="utf-8") as f:
                self._data = json.loads(f.read())
        except FileNotFoundError:
            print(f"Error: No se encuentra el archivo '{self._jsonfile}'")
            sys.exit(1)
        except json.JSONDecodeError as exc:
            print(f"Error: El archivo JSON no es válido: {exc}")
            sys.exit(1)
        return self

    def read_token(self, key):
        """Lee el valor asociado a una clave.

        Args:
            key: Nombre de la clave a buscar.

        Returns:
            El valor de la clave como string.
        """
        if self._data is None:
            self.load()
        if key in self._data:
            return str(self._data[key])
        disponibles = ", ".join(self._data.keys())
        print(f"Error: La clave '{key}' no existe. Claves disponibles: {disponibles}")
        sys.exit(1)

    def get_keys(self):
        """Devuelve las claves disponibles en el JSON cargado."""
        if self._data is None:
            self.load()
        return list(self._data.keys())


def leer_token_procedural(jsonfile, key):
    """Implementación procedural original (branching by abstraction).

    Args:
        jsonfile: Ruta al archivo JSON.
        key: Clave a buscar.

    Returns:
        Valor de la clave como string.
    """
    reader = SingletonTokenReader(jsonfile)
    return reader.read_token(key)


def mostrar_ayuda():
    """Muestra el mensaje de ayuda del programa."""
    print("Uso: python getJason_refactor.py [clave]")
    print("  clave       Clave a buscar en el archivo JSON (default: token1)")
    print("  -v          Muestra la versión del programa")
    print("  --help      Muestra esta ayuda")
    print()
    print("Ejemplos:")
    print("  python getJason_refactor.py              -> busca 'token1'")
    print("  python getJason_refactor.py token2       -> busca 'token2'")


def main():
    """Punto de entrada principal.

    Analiza los argumentos de línea de comandos, instancia el reader
    Singleton y recupera el token solicitado.
    """
    if len(sys.argv) > 2:
        print("Error: Demasiados argumentos. Use --help para ayuda.")
        sys.exit(1)

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg == "-v":
            print(f"getJason_refactor.py versión {VERSION}")
            sys.exit(0)
        if arg == "--help":
            mostrar_ayuda()
            sys.exit(0)
        jsonkey = arg
    else:
        jsonkey = "token1"

    reader = SingletonTokenReader()
    try:
        token = reader.read_token(jsonkey)
    except SystemExit:
        sys.exit(1)
    print(token)


if __name__ == "__main__":
    main()
