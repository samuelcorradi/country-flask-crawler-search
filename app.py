# coding:utf-8
'''
Realiza extracao dos dados de municipios
e salva em um banco de dados SQLite.
'''
from config import DB_PATH
from flask import Flask, render_template, request
import municipiosdb
import json


app = Flask(__name__)
db = municipiosdb.MunicipiosDb(DB_PATH)

def requer_json():
    '''
    Funcao para dizer se a requisicao espera
    que seja retornar um objeto json.
    '''
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']


@app.after_request
def after_request(resposta):
    '''
    Este decorator foi adicionado
    apenas para alterar o cabecalho
    da resposta e permitir crossdomain
    para testar a aplicacao em localhost.
    AO COMITAR PARA PRODUCAO, REMOVE-LO
    '''
    resposta.headers.add('Access-Control-Allow-Origin',
        '*')
    resposta.headers.add('Access-Control-Allow-Headers',
        'Content-Type,Authorization')
    resposta.headers.add('Access-Control-Allow-Methods', 
        'GET,PUT,POST,DELETE,OPTIONS')
    return resposta


@app.route('/')
def index():
    '''
    Metodo para pagina inicial.
    Carrega template com a
    pagina de busca.
    '''
    return render_template('busca.html'), 200


@app.route('/municipio/', methods=["GET"])
@app.route('/municipio/<string:filtro>/', methods=["GET"])
def municipio(filtro=""):
    '''
    endpoint para listar municipios
    '''
    pagina = request.args.get('pagina') or "1"
    data = []
    r = db.query(filtro, int(pagina), 10)
    for row in r:
        data.append({
            'ibge': row[0],
            'nome': row[1],
            'url': row[2]})
    if requer_json():
        return json.dumps(data), 200
    else:
        return "Formato da requisição inválido.", 400


@app.route('/municipios/', methods=['GET'])
def municipios():
    data = []
    r = db.getAll()
    for row in r:
        data.append({
            'ibge': row[0],
            'nome': row[1],
            'url': row[2]})
    if requer_json():
        return json.dumps(data), 200
    else:
        return "Formato da requisição inválido.", 400


if __name__ == "__main__":
    app.debug = True
    app.run()
