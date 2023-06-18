import unittest
from faltante import Conjunto

class TestConjunto(unittest.TestCase):
    def setUp(self):
        self.conjunto = Conjunto()

    def test_extraer(self):
        self.conjunto.extraer(1)
        self.assertNotIn(1, self.conjunto.conjunto)

    def test_calcular_faltante(self):
        self.conjunto.extraer(1)
        self.assertEqual(self.conjunto.calcular_faltante(),1)

    def test_extraer_invalid_number(self):
        with self.assertRaises(Exception):
            self.conjunto.extraer(101)

    def test_calcular_faltante_no_missing(self):
        with self.assertRaises(Exception):
            self.conjunto.calcular_faltante()

if __name__ == '__main__':
    unittest.main()