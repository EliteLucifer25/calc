import unittest
from calc import Calculator, CalculatorError
import math

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_basic_arithmetic(self):
        self.assertEqual(self.calc.evaluate("5 + 3"), 8)
        self.assertEqual(self.calc.evaluate("10 - 4"), 6)
        self.assertEqual(self.calc.evaluate("6 * 7"), 42)
        self.assertEqual(self.calc.evaluate("20 / 5"), 4.0)

    def test_advanced_math(self):
        self.assertAlmostEqual(self.calc.evaluate("sin(pi/2)"), 1.0)
        self.assertAlmostEqual(self.calc.evaluate("sqrt(16)"), 4.0)
        self.assertAlmostEqual(self.calc.evaluate("log(e)"), 1.0)
        self.assertEqual(self.calc.evaluate("abs(-15)"), 15)
        
    def test_exponents(self):
        self.assertEqual(self.calc.evaluate("2**3"), 8)
        self.assertEqual(self.calc.evaluate("pow(2, 3)"), 8)

    def test_order_of_operations(self):
        self.assertEqual(self.calc.evaluate("5 + 3 * 2"), 11)
        self.assertEqual(self.calc.evaluate("(5 + 3) * 2"), 16)
        self.assertEqual(self.calc.evaluate("10 - 4 / 2"), 8.0)

    def test_error_handling(self):
        with self.assertRaisesRegex(CalculatorError, "Division by zero is not allowed."):
            self.calc.evaluate("10 / 0")
            
        with self.assertRaisesRegex(CalculatorError, "Invalid syntax"):
            self.calc.evaluate("5 + + * 3")
            
        with self.assertRaisesRegex(CalculatorError, "Unsupported function or variable"):
            self.calc.evaluate("__import__('os').system('ls')")

    def test_history(self):
        self.assertEqual(self.calc.evaluate("50 + 50"), 100)
        self.assertEqual(self.calc.evaluate("_ + 10"), 110)
        self.assertEqual(self.calc.evaluate("ans * 2"), 220)

if __name__ == '__main__':
    unittest.main()
