
#REMOVER AS LINHAS
import unittest
from flask import Flask
app = Flask(__name__)

@app.route('/bug')
def bad():
    try:
        raise TypeError()
    except TypeError as e:
        print(e)
    except TypeError as e:
        print("Duplicado, ou seja, nunca vai entrar aqui.")

class TestBugRoute(unittest.TestCase):
    def test_bad_route(self):
        with app.test_client() as client:
            response = client.get('/bug')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
