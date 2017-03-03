'''
Realiza extracao dos dados de municipios
e salva em um banco de dados SQLite.
'''
import sqlite3
import json
import urllib
import ssl
import municipiosdb
from config import DB_PATH


def extracao():
    '''
    Limpa a tabela municipios, faz a consulta
    da API e salva os dados na mesma tabela.
    '''
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        db = municipiosdb.MunicipiosDb(DB_PATH);
        db.createTable()

        hdlr = urllib.urlopen("http://api.brasil.io/mg", context=ctx)
        data = hdlr.read()
        j = json.loads(data)
        for muni in j["municipios"]:
            db.insert(muni["codigo-ibge"], muni["nome"], muni["url"])
        print "Extracao realizada com sucesso!\n"
    except:
        print "Extracao NAO realizada:", sys.exc_info()[0]
        raise


if __name__ == "__main__":
    extracao()