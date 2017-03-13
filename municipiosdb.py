# coding:utf-8
'''
Classe com os metodos responsaveis
pela manipulacao e persistencia dos
dados dos municipios.
A class MunicipiosDb eh utilizada
tanto pela aplicacao principal
quanto pela aplicacao de extracao.
'''
import sqlite3


class MunicipiosDb(object):

    _conn = None
    _cur = None


    def __init__(self, base):
        self._conn = sqlite3.connect(base, check_same_thread=False)
        self._conn.isolation_level = None
        self._cur = self._conn.cursor()


    def getAll(self):
        return self.query("", 1)


    def query(self, filtro="", pagina=1, limite=0):
        '''
        gera o comando SQL para buscar os
        municipios
        Recebe o cursor da consulta, as
        informacoes de busca, e o limite de
        registros por pagina
        Retorna o cursor com os resultados
        da busca
        '''
        try:
            sql = "SELECT ibge_code, nome, link FROM municipios "
            bind = []
            # se ha algum filtro, testa se eh
            # pelo codigo do IBGE ou qualquer
            # outra string
            if filtro != "":
                if filtro.isdigit() is True:
                    sql = sql + "WHERE ibge_code = ? "
                else:
                    sql = sql + "WHERE nome LIKE ? "
                    filtro = '%' + filtro + '%'
                bind.append(filtro)

            if limite>0:
                pagina = (pagina - 1) * limite
                bind.append(pagina)
                sql = sql + "LIMIT %d OFFSET ?;" % limite

            return self._cur.execute(sql, bind)
        except:
            print 'Falha na consulta ao banco de dados.'
            raise


    def createTable(self):
        '''
        Metodo para criacao da tabela que
        armazena os dados dos municipios.
        '''
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
        try:
            self._cur.execute("BEGIN")
            sql = ('''INSERT INTO municipios (ibge_code, nome, link)
             VALUES(?, ?, ?);''')
            if isinstance(ibge, list):
                self._cur.executemany(sql, ibge)
            else:
                self._cur.execute(sql, (ibge, nome, url))
            self._cur.execute('COMMIT')
        except:
            print 'Falha na inserção dos dados.'
            self._cur.execute('ROLLBACK')
            raise


    def __del__(self):
        self._conn.close()
