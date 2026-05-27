# Decompiled from getJason.pyc
import json
import sys

jsonfile = "sitedata.json"
jsonkey = "token1"

with open(jsonfile, "r") as myfile:
    data = myfile.read()

obj = json.loads(data)
print(str(obj[jsonkey]))
