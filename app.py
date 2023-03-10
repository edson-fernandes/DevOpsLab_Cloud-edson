
import unittest
from flask import Flask
app = Flask(__name__)

@app.route('/bug')
def bad():
    try:
        raise TypeError()
    except TypeError as e:
        return str(e), 500

class TestBugRoute(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_bad_route(self):
        response = self.client.get('/bug')
        self.assertEqual(response.status_code, 500)
        self.assertIn(b"TypeError", response.data)

if __name__ == '__main__':
    unittest.main()
