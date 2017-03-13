# coding:utf-8
'''
Realiza uma serie de testes
que garatirao o funcionamento
dos recursos basicos da
aplicacao.
'''
import sys
import json
import unittest
sys.path.insert(0, "..")
from diariosAssociados import config
from diariosAssociados.app import app, db


class MunicipioTestCase(unittest.TestCase):

    def test_status(self):
        '''
        Um teste geral. Apenas para
        verificar se o servidor irah
        responder caso faca uma
        requisicao que aceite JSON
        para o endpoint /municipio/
        '''
        teste = app.test_client(self)
        resposta = teste.get('/municipio/', headers={"Accept":"application/json; q=1.0, text/json"})
        self.assertEqual(resposta.status_code, 200)

    def test_ibge(self):
        '''
        Verifica a resposta do se
        confere com o número de
        IBGE indicado (3100104)
        '''
        teste = app.test_client(self)
        resposta = teste.get('/municipio/3100104/', headers={"Accept":"application/json; q=1.0, text/json"})
        resultado = json.loads(resposta.data)
        self.assertEqual(resultado[0]['ibge'], '3100104')

    def test_somentjson(self):
        '''
        Faz uma requisicao que DEVE
        falhar para mostrar que apenas
        requisicoes que aceitam JSON
        terao uma resposta de sucesso
        do servidor.
        '''
        teste = app.test_client(self)
        resposta = teste.get('/municipio/3100104/')
        self.assertEqual(resposta.status_code, 400)

    def test_quantidade(self):
        '''
        Verifica a quantidade total
        dos registros de municipios
        retornados pelo endpoint
        /municipios/
        '''
        teste = app.test_client(self)
        resposta = teste.get('/municipios/', headers={"Accept":"application/json; q=1.0, text/json"})
        resultado = json.loads(resposta.data)
        qtd = len(resultado)
        self.assertEqual(qtd, 853)


if __name__ == '__main__':

    unittest.main()
