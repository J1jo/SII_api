import unittest
from api import get_uf_value

class TestApi(unittest.TestCase):
    def test_get_uf_value(self):
        result = get_uf_value('2023-04-25')
        self.assertIsNotNone(result)
