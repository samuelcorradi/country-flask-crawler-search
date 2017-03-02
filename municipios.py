'''
Realiza extracao dos dados de municipios
e salva em um banco de dados SQLite.
'''
from flask import Flask, render_template
import municipiosdb
import json
app = Flask(__name__)

@app.after_request
def after_request(response):
	'''
	Este decorator foi adicionado
	apenas para alterar o cabecalho
	da resposta e permitir crossdomain
	para testar a aplicacao em localhost.
	AO COMITAR PARA PRODUCAO, REMOVE-LO
	'''
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response

@app.route('/')
def index():
	'''
	Metodo para pagina inicial.
	Carrega template com a
	pagina de busca.
	'''
    return render_template('busca.html')

@app.route('/municipio/', methods=["GET"])
@app.route('/municipio/<int:pagina>/', methods=["GET"])
@app.route('/municipio/<int:pagina>/<string:filtro>/', methods=["GET"])
def municipio(pagina=1, filtro=""):
	'''
    endpoint para listar municipios
    '''
	db = municipiosdb.MunicipiosDb('base.sqlite')

	data = []
	
	r = db.query(pagina, filtro)

	for row in r:
		data.append({'ibge':row[0],'nome':row[1],'url':row[2]})

	return json.dumps(data)



if __name__ == "__main__":
    app.run();
