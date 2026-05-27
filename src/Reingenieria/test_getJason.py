"""
Script de prueba para getJason.py y getJason_mod.py

Casos de prueba:
1. getJason.py (default token1)
2. getJason_mod.py (default token1)
3. getJason_mod.py token2
4. getJason_mod.py token1
5. getJason_mod.py con clave inexistente
6. getJason_mod.py sin archivo JSON
"""

import subprocess
import sys
import os

test_dir = os.path.dirname(os.path.abspath(__file__))

def run_test(nombre, script, args=None, cwd=None):
    if cwd is None:
        cwd = test_dir
    cmd = [sys.executable, os.path.join(test_dir, script)]
    if args:
        cmd.extend(args)
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    print(f"TEST: {nombre}")
    print(f"  Comando: {' '.join(cmd)}")
    if result.stdout:
        print(f"  Salida: {result.stdout.strip()}")
    if result.stderr:
        print(f"  Error: {result.stderr.strip()}")
    print()

# Prueba 1: getJason.py default
run_test("getJason.py default token1", "getJason.py")

# Prueba 2: getJason_mod.py default
run_test("getJason_mod.py default token1", "getJason_mod.py")

# Prueba 3: getJason_mod.py con token2
run_test("getJason_mod.py con token2", "getJason_mod.py", ["token2"])

# Prueba 4: getJason_mod.py con token1 explicito
run_test("getJason_mod.py con token1", "getJason_mod.py", ["token1"])

# Prueba 5: getJason_mod.py con clave inexistente
run_test("getJason_mod.py clave inexistente", "getJason_mod.py", ["clave_falsa"])

# Prueba 6: getJason_mod.py sin archivo (desde otro directorio)
temp_dir = os.path.join(test_dir, "..")
run_test("getJason_mod.py sin archivo JSON", "getJason_mod.py", cwd=temp_dir)

print("=== TODAS LAS PRUEBAS COMPLETADAS ===")
