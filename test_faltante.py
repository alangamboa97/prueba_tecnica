import unittest
from faltante import Conjunto

import unittest

class ConjuntoTests(unittest.TestCase):

    def setUp(self):
        self.conjunto = Conjunto()

    def test_extraer_numero_valido(self):
        self.conjunto.extraer(50)
        self.assertNotIn(50, self.conjunto.conjunto)

    def test_extraer_numero_mayor_a_100(self):
        with self.assertRaises(Exception):
            self.conjunto.extraer(150)

    def test_calcular_faltante_conjunto_completo(self):
        with self.assertRaises(Exception):
            self.conjunto.calcular_faltante()

    def test_calcular_faltante_conjunto_incompleto(self):
        self.conjunto.extraer(10)
        self.assertEqual(self.conjunto.calcular_faltante(), 10)

if __name__ == '__main__':
    unittest.main()
