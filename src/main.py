from Patterns.Singleton.factorial_calculator import FactorialCalculator
from Patterns.Singleton.tax_calculator import TaxCalculator
from Patterns.Factory.burger_factory import HamburguesaFactory
from Patterns.Factory.invoice_factory import FacturaFactory
from Patterns.Builder.avion_builder import Director, AvionComercialBuilder
from Patterns.Prototype.dashboard_component import ComponenteDashboard
from Patterns.Abstract_Factory.gui_factory import TemaClaroFactory, TemaOscuroFactory

def ejercicio_1():
    print("--- Ejercicio 1: Singleton (Factorial) ---")
    instancia_a = FactorialCalculator()
    instancia_b = FactorialCalculator()
    if instancia_a is instancia_b:
        print("OK: Ambas variables apuntan a la misma instancia.")
    n = 5
    print(f"Resultado: El factorial de {n} es {instancia_a.calcular_factorial(n)}")
    print("-" * 50 + "\n")


def ejercicio_2():
    print("--- Ejercicio 2: Singleton (Impuestos) ---")
    calculador = TaxCalculator()
    otro_calculador = TaxCalculator()
    if calculador is otro_calculador:
        print("OK: El calculador de impuestos es una instancia única.")
    base = 1000.0
    impuestos = calculador.calcular_impuestos(base)
    print(f"Base: ${base:.2f} | Impuestos: ${impuestos:.2f} | Total: ${base + impuestos:.2f}")
    print("-" * 50 + "\n")


def ejercicio_3():
    print("--- Ejercicio 3: Factory (Hamburguesas) ---")
    try:
        pedido_1 = HamburguesaFactory.crear_hamburguesa("mostrador")
        pedido_2 = HamburguesaFactory.crear_hamburguesa("retiro")
        pedido_3 = HamburguesaFactory.crear_hamburguesa("delivery")
        pedido_1.entregar()
        pedido_2.entregar()
        pedido_3.entregar()
    except ValueError as error:
        print(f"Error: {error}")
    print("-" * 50 + "\n")


def ejercicio_4():
    print("--- Ejercicio 4: Factory (Facturas) ---")
    importe_compra = 5400.50
    try:
        factura_1 = FacturaFactory.crear_factura("responsable", importe_compra)
        factura_2 = FacturaFactory.crear_factura("no inscripto", importe_compra)
        factura_3 = FacturaFactory.crear_factura("exento", importe_compra)
        factura_1.generar()
        factura_2.generar()
        factura_3.generar()
    except ValueError as error:
        print(f"Error detectado: {error}")
    print("-" * 50 + "\n")


def ejercicio_5():
    print("--- Ejercicio 5: Builder (Aviones) ---")
    director = Director()
    builder_comercial = AvionComercialBuilder()
    director.builder = builder_comercial
    director.construir_avion_basico()
    mi_avion = builder_comercial.get_resultado()
    print(mi_avion)
    print("-" * 50 + "\n")


def ejercicio_6():
    print("--- Ejercicio 6: Prototype (Copias iterativas) ---")
    original = ComponenteDashboard("Métrica Principal", "Azul", "Blanco")
    primera_copia = original.clonar()
    segunda_copia = primera_copia.clonar()
    
    segunda_copia.nombre = "Métrica Secundaria"
    segunda_copia.color_fondo = "Gris"
    
    print("Original      ->", original)
    print("Copia 1       ->", primera_copia)
    print("Copia 2       ->", segunda_copia)
    print("-" * 50 + "\n")


def ejercicio_7():
    """
    Ejercicio 7: Abstract Factory.
    Situación: Generar la UI de un Dashboard según el tema elegido (Claro/Oscuro).
    """
    print("--- Ejercicio 7: Abstract Factory (Dashboard UI) ---")
    
    tema_elegido = "oscuro"
    print(f"Sistema inicializado con el tema: {tema_elegido.upper()}")
    
    if tema_elegido == "claro":
        fabrica_ui = TemaClaroFactory()
    else:
        fabrica_ui = TemaOscuroFactory()
        
    boton_interfaz = fabrica_ui.crear_boton()
    panel_interfaz = fabrica_ui.crear_panel()
    
    print("Renderizando componentes de la interfaz...")
    print(panel_interfaz.renderizar())
    print(boton_interfaz.renderizar())
    print("-" * 50 + "\n")


def main():
    print("=" * 50)
    print("TRABAJO PRÁCTICO: PATRONES DE DISEÑO CREACIONALES")
    print("=" * 50 + "\n")
    
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
    ejercicio_5()
    ejercicio_6()
    ejercicio_7()

if __name__ == "__main__":
    main()