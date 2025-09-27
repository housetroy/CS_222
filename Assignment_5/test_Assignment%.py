import unittest
from Assignment5 import fahrenheit_to_celsius, fibonaci

class TestAssignment5(unittest.TestCase):

    def test_f_to_c_freezing(test):
        test.assertAlmostEqual(fahrenheit_to_celsius(32),0.0)

    def test_f_to_c_boiling(test):
        test.assertAlmostEqual(fahrenheit_to_celsius(212),100.0)

    def test_fib_bases(test):
        test.assertAlmostEqual(fibonaci(0),0)
        test.assertAlmostEqual(fibonaci(1),1)

    def test_fib_normal(test):
        test.assertAlmostEqual(fibonaci(10),55)

    def test_fib_neg(test):
        with test.assertRaises(ValueError):
            fibonaci(-5)

    def test_fib_type(test):
        with test.assertRaises(TypeError):
            fibonaci(3.5)

unittest.main()