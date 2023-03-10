from app import app
import unittest

class TestBugRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.result = self.app.get('/bug')

    def test_bug_route(self):
        self.assertEqual(self.result.status_code, 500) # O TypeError resulta em um erro interno do servidor (500)

    def test_error_message(self):
        self.assertIn(b"TypeError", self.result.data) # Espera-se que a mensagem de erro apareça na resposta
        self.assertNotIn(b"Duplicado", self.result.data) # Garante que a mensagem de duplicidade não apareça na resposta
