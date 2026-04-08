import unittest
import math
from rpn import RPNCalculator, RPNError

class TestRPNCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = RPNCalculator()

    def test_ejemplos_consigna(self):
        self.assertEqual(self.calc.evaluate("3 4 + -7 +"), 0.0) 
        self.assertEqual(self.calc.evaluate("5 1 2 + 4 * + 3 -"), 14.0)
        self.assertEqual(self.calc.evaluate("2 3 4 * +"), 14.0)

    def test_operaciones_basicas_y_floats(self):
        self.assertEqual(self.calc.evaluate("10.5 2.5 -"), 8.0)
        self.assertEqual(self.calc.evaluate("-3 4 *"), -12.0)
        self.assertEqual(self.calc.evaluate("10 2 /"), 5.0)

    def test_errores_comunes(self):
        with self.assertRaises(RPNError):
            self.calc.evaluate("3 0 /") 
        with self.assertRaises(RPNError):
            self.calc.evaluate("3 +") 
        with self.assertRaises(RPNError):
            self.calc.evaluate("3 4 XYZ") 
        with self.assertRaises(RPNError):
            self.calc.evaluate("3 4 5 +")

    def test_comandos_pila(self):
        self.assertEqual(self.calc.evaluate("5 DUP *"), 25.0)
        self.assertEqual(self.calc.evaluate("2 3 SWAP -"), 1.0)
        self.assertEqual(self.calc.evaluate("2 3 DROP 4 +"), 6.0)
        self.assertEqual(self.calc.evaluate("10 20 30 CLEAR 5"), 5.0)

    def test_constantes(self):
        self.assertAlmostEqual(self.calc.evaluate("PI"), math.pi)
        self.assertAlmostEqual(self.calc.evaluate("E"), math.e)
        self.assertAlmostEqual(self.calc.evaluate("PHI"), (1 + math.sqrt(5)) / 2)

    def test_funciones_matematicas(self):
        self.assertAlmostEqual(self.calc.evaluate("9 SQRT"), 3.0)
        self.assertAlmostEqual(self.calc.evaluate("100 LOG"), 2.0)
        self.assertAlmostEqual(self.calc.evaluate("2 3 Y^X"), 8.0)
        self.assertEqual(self.calc.evaluate("5 CHS"), -5.0)
        self.assertAlmostEqual(self.calc.evaluate("10 LN"), math.log(10))
        self.assertAlmostEqual(self.calc.evaluate("2 E^X"), math.exp(2))
        self.assertAlmostEqual(self.calc.evaluate("3 10^X"), 1000.0)
        self.assertEqual(self.calc.evaluate("4 1/X"), 0.25)
        
        with self.assertRaises(RPNError):
            self.calc.evaluate("0 1/X")

    def test_trigonometria(self):
        self.assertAlmostEqual(self.calc.evaluate("90 SIN"), 1.0)
        self.assertAlmostEqual(self.calc.evaluate("0 COS"), 1.0)
        self.assertAlmostEqual(self.calc.evaluate("45 TG"), 1.0)
        self.assertAlmostEqual(self.calc.evaluate("1 ASIN"), 90.0)
        self.assertAlmostEqual(self.calc.evaluate("1 ACOS"), 0.0)
        self.assertAlmostEqual(self.calc.evaluate("1 ATG"), 45.0)

    def test_memoria(self):
        self.assertEqual(self.calc.evaluate("5 STO00 10 RCL00 +"), 15.0)
        with self.assertRaises(RPNError):
            self.calc.evaluate("5 STO15") 
        with self.assertRaises(RPNError):
            self.calc.evaluate("RCL15")

if __name__ == '__main__':
    unittest.main()