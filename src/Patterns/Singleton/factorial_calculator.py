class FactorialCalculator:
    # 1. Variable de clase (estática) para guardar la única instancia
    _instance = None

    # 2. Sobrescribimos __new__ para controlar la creación del objeto
    def __new__(cls):
        # Si la instancia aún no existe, usamos super() para crearla
        if cls._instance is None:
            cls._instance = super(FactorialCalculator, cls).__new__(cls)
        
        # Si ya existe, simplemente retornamos la que guardamos
        return cls._instance

    # 3. La lógica de negocio: el cálculo del factorial
    def calcular_factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
            
        return resultado