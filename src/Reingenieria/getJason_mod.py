"""
getJason_mod.py - Versión modificada de getJason.py

Lee un archivo JSON con claves y valores, y recupera el valor asociado
a una clave indicada como argumento (default "token1").

Modificaciones respecto a getJason.py:
- Acepta cualquier clave como argumento (sys.argv[1])
- Manejo de errores: archivo no encontrado, clave inexistente
- Documentación actualizada
"""

import json
import sys

jsonfile = "sitedata.json"
jsonkey = sys.argv[1] if len(sys.argv) > 1 else "token1"

try:
    with open(jsonfile, "r") as myfile:
        data = myfile.read()
except FileNotFoundError:
    print(f"Error: No se encuentra el archivo '{jsonfile}'")
    sys.exit(1)

obj = json.loads(data)

if jsonkey in obj:
    print(str(obj[jsonkey]))
else:
    print(f"Error: La clave '{jsonkey}' no existe en el archivo JSON")
    print(f"Claves disponibles: {', '.join(obj.keys())}")
    sys.exit(1)
