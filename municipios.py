'''
Realiza extracao dos dados de municipios
e salva em um banco de dados SQLite.
'''
from flask import Flask, render_template
import sqlite3
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('busca.html')

@app.route('/municipio/', methods=["GET"])
@app.route('/municipio/<int:pagina>/', methods=["GET"])
@app.route('/municipio/<int:pagina>/<string:filtro>/', methods=["GET"])
def municipio(pagina=1, filtro=""):
	'''
    endpoint para listar municipios
    '''
	data = []
	conn = sqlite3.connect('base.sqlite')
	cur = conn.cursor()
	pagina = (pagina - 1) * 10;

	r = cur.execute(query(pagina, filtro));
	for row in r:
		data.append({'key':row[0],'ibge':row[1],'nome':row[2],'url':row[3]})
	cur.close();
	json_data = json.dumps(data)
	return json_data

def query(pagina, filtro):
	'''
    gera o comando SQL para buscar os
	municipios
    '''
	query = "SELECT * FROM municipios";
	if filtro.isdigit()==True:
		query = query + " WHERE ibge_code='" + filtro + "'";
	elif filtro!="":
		query = query + " WHERE nome LIKE '%" + filtro + "%'";
	query = query + " LIMIT 10 OFFSET " + str(pagina) + ";";
	print query;
	return query;

if __name__ == "__main__":
    app.run();