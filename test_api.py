import unittest
from uf import get_uf_value

class TestAPI(unittest.TestCase):

    def test_get_uf_value(self):
        # Probar un caso válido
        result = get_uf_value('10-04-2022')
        self.assertEqual(result, {'value': '29.763,45'})

        # Probar un caso con fecha inválida
        result = get_uf_value('31-02-2022')
        self.assertEqual(result, {'error': 'Fecha no válida.'})

        # Probar un caso con página no encontrada
        result = get_uf_value('10-04-2023')
        self.assertEqual(result, {'error': 'No se pudo descargar la página.'})

        # Probar un caso con valor no encontrado
        result = get_uf_value('01-01-2013')
        self.assertEqual(result, {'error': 'No se encontró el valor de la UF correspondiente a la fecha ingresada.'})

if __name__ == '__main__':
    unittest.main()
