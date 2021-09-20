from unittest import TestCase, skip
# from unittest.case import SkipTest
from prueba import sumatoria

class TestPruebas(TestCase):
    @skip('Demostrando los test, no sirve este test')
    def testPrueba(self):
        nombre = 'Marigrace'
        self.assertEqual(nombre, 'marigrace')

    def testSumatoria(self):
        resultado = sumatoria(5,6)
        self.assertEqual(resultado,11)
        self.assertNotEqual(resultado, 10)

