import sqlite3


class MunicipiosDb(object):

    _conn = None
    _cur = None

    def __init__(self, base):
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
        pagina = (pagina - 1) * 10
        sql = "SELECT ibge_code, nome, link FROM municipios "
        bind = [pagina]

        # se ha algum filtro, testa se eh
        # pelo codigo do IBGE ou qualquer
        # outra string
        if filtro != "":
            if filtro.isdigit() is True:
                sql = sql + "WHERE ibge_code = ? "
            else:
                sql = sql + "WHERE nome LIKE ? "
                filtro = '%' + filtro + '%'
            bind.insert(0, filtro)

        sql = sql + "LIMIT 10 OFFSET ?;"

        return self._cur.execute(sql, bind)

    def createTable(self):
        self._cur.execute('''DROP TABLE IF EXISTS municipios;''')
        self._cur.execute('''CREATE TABLE `municipios` (
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,
        `ibge_code` VARCHAR(7) NOT NULL,
        `nome` VARCHAR(255) NOT NULL,
        `link` VARCHAR(255) NOT NULL);''')

    def insert(self, ibge, nome=None, url=None):
        '''
        Metodo para insercao de registros.
        Se for passado uma lista para ibge,
        insere todos os registros.
        Se todos parametros forem escalares
        insere apenas um registro.
        No final realiza commit.
        '''
        sql = ('''INSERT INTO municipios (ibge_code, nome, link)
         VALUES(?, ?, ?);''')

        if isinstance(ibge, list):
            self._cur.executemany(sql, ibge)
        else:
            self._cur.execute(sql, (ibge, nome, url))

        self._conn.commit()

    def __del__(self):
        self._conn.close()
