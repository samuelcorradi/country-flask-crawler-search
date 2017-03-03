
import sys
import json
import unittest
sys.path.insert(0, "..")
from diariosAssociados import config
from diariosAssociados.app import app, db

class MunicipioTestCase(unittest.TestCase):

    def test_status(self):
        teste = app.test_client(self)
        resposta = teste.get('/municipio/')
        self.assertEqual(resposta.status_code, 200)

    def test_ibge(self):
        teste = app.test_client(self)
        resposta = teste.get('/municipio/1/3100104/')
        resultado = json.loads(resposta.data)
        print resultado
        self.assertEqual(resultado[0]['ibge'], '3100104')


if __name__ == '__main__':
    unittest.main()
