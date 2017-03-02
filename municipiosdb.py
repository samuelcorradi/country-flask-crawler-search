import sqlite3

class MunicipiosDb(object):
	
	_conn = None
	
	_cur = None

	def __init__(self, base):

		print base

		self._conn = sqlite3.connect(base)
		
		self._cur = self._conn.cursor()

	def query(self, pagina=1, filtro=""):
		'''
	    gera o comando SQL para buscar os
		municipios
		Recebe o cursor da consulta, as
		informacoes de busca
		Retorna o cursor com os resultados
		da busca
	    '''
		pagina = (pagina - 1) * 10;
		sql = "SELECT ibge_code, nome, link FROM municipios "
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

		return self._cur.execute(sql, bind);

	def __del__ (self):

		self._conn.close()
