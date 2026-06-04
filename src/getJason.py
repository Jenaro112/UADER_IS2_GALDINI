# pylint: disable=invalid-name
"""Lee un archivo JSON y extrae el valor de la clave 'token1'.

Decompilado de getJason.pyc.
"""

import json

JSONFILE = "sitedata.json"
JSONKEY = "token1"

with open(JSONFILE, "r", encoding="utf-8") as myfile:
    DATA = myfile.read()

OBJ = json.loads(DATA)
print(str(OBJ[JSONKEY]))
