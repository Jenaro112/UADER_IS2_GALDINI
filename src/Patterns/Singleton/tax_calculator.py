class TaxCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaxCalculator, cls).__new__(cls)
        return cls._instance

    def calcular_impuestos(self, base_imponible: float) -> float:
        """
        Calcula el total de impuestos sobre una base imponible.
        IVA: 21% | IIBB: 5% | Contribuciones municipales: 1.2%
        """
        if base_imponible < 0:
            raise ValueError("El importe base no puede ser negativo.")

        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012

        total_impuestos = iva + iibb + contribuciones
        
        return total_impuestos