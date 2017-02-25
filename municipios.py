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
	conn = sqlite3.connect('base.sqlite')
	cur = conn.cursor()
	data = []
	r = query(cur, pagina, filtro)
	for row in r:
		data.append({'key':row[0],'ibge':row[1],'nome':row[2],'url':row[3]})
	cur.close();
	json_data = json.dumps(data)
	return json_data

def query(cur, pagina, filtro):
	'''
    gera o comando SQL para buscar os
	municipios
	Recebe o cursor da consulta, as
	informacoes de busca
	Retorna o cursor com os resultados
	da busca
    '''
	pagina = (pagina - 1) * 10;
	sql = "SELECT * FROM municipios "
	bind = [pagina]


	# se ha algum filtro, testa se eh
	# pelo codigo do IBGE ou qualquer
	# outra string
	if filtro!="":
		if filtro.isdigit()==True:
			sql = sql + "WHERE ibge_code = ? "
		else:
			sql = sql + "WHERE nome LIKE ? "
			filtro = '%' + filtro + '%'
		bind.insert(0, filtro)


	sql = sql + "LIMIT 10 OFFSET ?;"

	print sql;

	return cur.execute(sql, bind);


if __name__ == "__main__":
    app.run();
