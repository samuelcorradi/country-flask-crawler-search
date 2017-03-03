'''
Realiza extracao dos dados de municipios
e salva em um banco de dados SQLite.
'''
import sqlite3
import json
import urllib
import ssl

def extracao():
    '''
    Limpa a tabela municipios, faz a consulta
    da API e salva os dados na mesma tabela.
    '''
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    conn = sqlite3.connect('base.sqlite')
    cur = conn.cursor()
    cur.execute('''DROP TABLE IF EXISTS municipios;''')
    cur.execute('''CREATE TABLE `municipios` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `ibge_code`    VARCHAR(7) NOT NULL,
    `nome`    VARCHAR(255) NOT NULL,
    `link`    VARCHAR(255) NOT NULL);''')
    hdlr = urllib.urlopen("http://api.brasil.io/mg", context=ctx)
    data = hdlr.read()
    j = json.loads(data)
    for muni in j["municipios"]:
        cur.execute('''INSERT INTO municipios (ibge_code, nome, link) VALUES(?, ?, ?);''', (muni["codigo-ibge"], muni["nome"], muni["url"]))
    conn.commit();
    cur.close();

if __name__ == "__main__":
    extracao()