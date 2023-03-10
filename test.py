import unittest
from app import app

class TestBugRoute(unittest.TestCase):
    def test_bug_route(self):
        with app.test_client() as client:
            response = client.get('/bug')
            self.assertEqual(response.status_code, 500) # Um TypeError resulta em um erro interno do servidor (500)
            # Garante que apenas um dos blocos except seja executado
            self.assertIn(b"TypeError", response.data) # Espera-se que a mensagem de erro apareça na resposta
            self.assertNotIn(b"Duplicado", response.data) # Garante que a mensagem de duplicidade não apareça na resposta
