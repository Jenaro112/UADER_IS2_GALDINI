import time

# Clase base original
class Ping:
    def execute(self, ip_address):
        # Solo funciona si la dirección IP provista comienza con "192." 
        if ip_address.startswith("192."):
            print(f"--- Iniciando ping seguro a {ip_address} ---")
            for i in range(10): # Realiza 10 intentos de ping 
                print(f"Ping a {ip_address} - Intento {i+1}")
        else:
            print(f"Error de seguridad: La IP '{ip_address}' no comienza con '192.'")

    def executefree(self, ip_address):
        # Hace lo mismo pero sin el control de dirección 
        print(f"--- Iniciando ping LIBRE a {ip_address} ---")
        for i in range(10):
            print(f"Ping libre a {ip_address} - Intento {i+1}")

# Patrón Proxy
class PingProxy:
    def __init__(self):
        self.ping_real = Ping()

    def execute(self, ip_address):
        # Si la dirección es "192.168.0.254" realice un ping a www.google.com usando executefree [cite: 10]
        if ip_address == "192.168.0.254":
            print("Proxy detectó IP reservada. Redirigiendo a www.google.com...")
            self.ping_real.executefree("www.google.com")
        else:
            # Re-envíe a execute de la clase ping en cualquier otro caso [cite: 10]
            self.ping_real.execute(ip_address)

# --- Prueba de la implementación ---
proxy = PingProxy()
print("Escenario A: IP común válida")
proxy.execute("192.168.1.10")

print("\nEscenario B: IP interceptada por el Proxy")
proxy.execute("192.168.0.254")

print("\nEscenario C: IP rechazada (Fuera de rango)")
proxy.execute("10.0.0.1")